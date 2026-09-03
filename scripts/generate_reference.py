#!/usr/bin/env python3
"""
Generate the dhxpyt API reference under skills/pytincture-dhxpyt/references/dhxpyt/.

Reads the dhxpyt source with `ast` (no import, no Pyodide needed) and emits one
compact Markdown page per module plus an index. Replaces the old pdoc HTML dump,
which was 4.4 MB for a single module and carried no content in its index page.

Usage:
    python3 scripts/generate_reference.py /path/to/dhx_pytincture_widgetset
"""
from __future__ import annotations

import ast
import os
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "pytincture-dhxpyt"
OUT = SKILL / "references" / "dhxpyt"


def unparse(node) -> str:
    try:
        return ast.unparse(node)
    except Exception:
        return "?"


def signature(fn: ast.FunctionDef) -> list[str]:
    """Render one `name: type = default` line per parameter, skipping self."""
    args = fn.args
    positional = args.posonlyargs + args.args
    defaults: list = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    lines = []
    for arg, default in zip(positional, defaults):
        if arg.arg == "self":
            continue
        part = arg.arg
        if arg.annotation is not None:
            part += f": {unparse(arg.annotation)}"
        if default is not None:
            part += f" = {unparse(default)}"
        lines.append(part)
    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        part = arg.arg
        if arg.annotation is not None:
            part += f": {unparse(arg.annotation)}"
        if default is not None:
            part += f" = {unparse(default)}"
        lines.append(part)
    if args.vararg:
        lines.append(f"*{args.vararg.arg}")
    if args.kwarg:
        lines.append(f"**{args.kwarg.arg}")
    return lines


def first_doc_line(node) -> str:
    doc = ast.get_docstring(node) or ""
    for line in doc.splitlines():
        line = line.strip()
        if line:
            return line
    return ""


def method_line(fn: ast.FunctionDef) -> str:
    params = ", ".join(signature(fn))
    ret = f" -> {unparse(fn.returns)}" if fn.returns else ""
    return f"{fn.name}({params}){ret}"


def collect(src_root: Path):
    modules: dict[str, dict] = {}
    pkg = src_root / "dhxpyt"
    for path in sorted(pkg.rglob("*.py")):
        if "__pycache__" in path.parts or "dhxsrc" in path.parts:
            continue
        rel = path.relative_to(pkg)
        module = rel.parts[0] if len(rel.parts) > 1 else rel.stem
        if module in {"__init__", "python_code_mapping"}:
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        entry = modules.setdefault(module, {"configs": [], "widgets": []})
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            init = next(
                (f for f in node.body
                 if isinstance(f, ast.FunctionDef) and f.name == "__init__"),
                None,
            )
            if init is not None:
                params = signature(init)
            else:
                # @dataclass configs declare annotated fields instead of __init__.
                params = []
                for field_node in node.body:
                    if not isinstance(field_node, ast.AnnAssign):
                        continue
                    if not isinstance(field_node.target, ast.Name):
                        continue
                    part = f"{field_node.target.id}: {unparse(field_node.annotation)}"
                    if field_node.value is not None:
                        part += f" = {unparse(field_node.value)}"
                    params.append(part)
            public = [
                f for f in node.body
                if isinstance(f, ast.FunctionDef) and not f.name.startswith("_")
            ]
            record = {
                "name": node.name,
                "doc": first_doc_line(node),
                "params": params,
                "methods": [method_line(f) for f in public],
                "file": str(path.relative_to(src_root)),
            }
            if node.name.endswith("Config"):
                entry["configs"].append(record)
            else:
                entry["widgets"].append(record)
    return modules


def write_module_page(module: str, entry: dict, version: str) -> int:
    lines = [
        f"# dhxpyt.{module}",
        "",
        f"Generated from dhxpyt {version} source by `scripts/generate_reference.py`.",
        "",
    ]
    if entry["configs"]:
        lines += ["## Config classes", ""]
        for cfg in sorted(entry["configs"], key=lambda c: c["name"]):
            lines.append(f"### {cfg['name']}")
            if cfg["doc"]:
                lines.append(f"{cfg['doc']}")
            lines.append("")
            if cfg["params"]:
                lines.append("```python")
                lines.append(f"{cfg['name']}(")
                for param in cfg["params"]:
                    lines.append(f"    {param},")
                lines.append(")")
                lines.append("```")
            else:
                lines.append("_No keyword parameters._")
            lines.append("")
    if entry["widgets"]:
        lines += ["## Widget classes", ""]
        for widget in sorted(entry["widgets"], key=lambda w: w["name"]):
            lines.append(f"### {widget['name']}")
            if widget["doc"]:
                lines.append(f"{widget['doc']}")
            lines.append("")
            if widget["methods"]:
                lines.append("```python")
                for method in widget["methods"]:
                    lines.append(method)
                lines.append("```")
            lines.append("")
    text = "\n".join(lines).rstrip() + "\n"
    (OUT / f"{module}.md").write_text(text, encoding="utf-8")
    return len(text)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src_root = Path(sys.argv[1]).resolve()
    if not (src_root / "dhxpyt").is_dir():
        print(f"error: {src_root} does not contain a dhxpyt/ package")
        return 2

    version = "unknown"
    init = (src_root / "dhxpyt" / "__init__.py").read_text(encoding="utf-8")
    for node in ast.parse(init).body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__version__":
                    version = node.value.value

    modules = collect(src_root)
    if OUT.exists():
        for stale in OUT.iterdir():
            if stale.is_file():
                stale.unlink()
    OUT.mkdir(parents=True, exist_ok=True)

    total = 0
    for module, entry in sorted(modules.items()):
        total += write_module_page(module, entry, version)

    # Index: module list plus every add_* helper, which is the API the skill
    # steers toward (helpers create a valid container; bare widgets do not).
    # Only the container-mounting helpers: `add_<widget>(id, <widget>_config=...)`.
    # add_event_handler/add_card/add_row_css and friends are ordinary methods and
    # belong on the module pages, not here.
    helpers: list[tuple[str, str]] = []
    for module, entry in sorted(modules.items()):
        for widget in entry["widgets"]:
            for method in widget["methods"]:
                if method.startswith("add_") and "_config" in method:
                    helpers.append((f"{module}.{widget['name']}", method))

    index = [
        f"# dhxpyt {version} API reference",
        "",
        "One page per module, generated from source. Load only the module you need.",
        "",
        "## Modules",
        "",
    ]
    for module, entry in sorted(modules.items()):
        counts = f"{len(entry['configs'])} config, {len(entry['widgets'])} widget"
        index.append(f"- [`{module}`]({module}.md) — {counts}")
    index += [
        "",
        "## `add_*` helpers",
        "",
        "Prefer these over constructing a widget directly: they mount the widget",
        "into a container that already exists. The `id` is an **existing cell id**",
        "in the layout/tabbar you are calling, not a new name.",
        "",
        "```python",
    ]
    for owner, method in sorted(set(helpers)):
        index.append(f"{owner}.{method}")
    index += ["```", ""]
    text = "\n".join(index)
    (OUT / "index.md").write_text(text, encoding="utf-8")
    total += len(text)

    print(f"wrote {len(modules) + 1} files, {total:,} bytes into {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
