#!/usr/bin/env python3
"""
Generate a widgetset API reference under skills/<skill>/references/<package>/.

Reads the widgetset source with `ast` (no import, no Pyodide needed) and emits
one compact Markdown page per module plus an index. Replaces the old pdoc HTML
dump, which was 4.4 MB for a single module and carried no content in its index
page.

The package is detected from the checkout: a `dhxpyt/` package regenerates the
pytincture-dhxpyt skill, a `wapyt/` package regenerates pytincture-wapyt.

Usage:
    python3 scripts/generate_reference.py /path/to/dhx_pytincture_widgetset
    python3 scripts/generate_reference.py /path/to/wa_pytincture_widgetset
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent / "skills"

# Per-widgetset settings. dhxpyt keeps the exact output it always had; wapyt
# turns on the extras its source needs:
#   dataclass_configs  @dataclass item types (TreeItem, ColumnConfig's siblings
#                      TableAction, SelectOption, ...) are config, not widgets
#   full_docs          whole class docstrings and per-method doc lines; wapyt's
#                      Args blocks and event-payload shapes live there
#   functions          module-level functions (wapyt.filetransfer is all
#                      functions and no widget)
PACKAGES = {
    "dhxpyt": {
        "skill": "pytincture-dhxpyt",
        "skip_parts": {"__pycache__", "dhxsrc"},
        "skip_modules": {"__init__", "python_code_mapping"},
        "dataclass_configs": False,
        "full_docs": False,
        "functions": False,
    },
    "wapyt": {
        "skill": "pytincture-wapyt",
        "skip_parts": {"__pycache__", "assets"},
        "skip_modules": {"__init__", "_runtime", "assets"},
        "dataclass_configs": True,
        "full_docs": True,
        "functions": True,
    },
}


def unparse(node) -> str:
    try:
        return ast.unparse(node)
    except Exception:
        return "?"


def signature(fn) -> list[str]:
    """Render one `name: type = default` line per parameter, skipping self."""
    args = fn.args
    positional = args.posonlyargs + args.args
    defaults: list = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    lines = []
    for arg, default in zip(positional, defaults):
        if arg.arg in {"self", "cls"}:
            continue
        part = arg.arg
        if arg.annotation is not None:
            part += f": {unparse(arg.annotation)}"
        if default is not None:
            part += f" = {unparse(default)}"
        lines.append(part)
    if args.vararg:
        lines.append(f"*{args.vararg.arg}")
    elif args.kwonlyargs:
        lines.append("*")
    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        part = arg.arg
        if arg.annotation is not None:
            part += f": {unparse(arg.annotation)}"
        if default is not None:
            part += f" = {unparse(default)}"
        lines.append(part)
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


def first_paragraph(node) -> str:
    """The docstring's opening paragraph on one line; a first line alone often
    stops mid-sentence."""
    doc = (ast.get_docstring(node) or "").strip()
    return " ".join(doc.split("\n\n", 1)[0].split()) if doc else ""


def method_line(fn, with_doc: bool = False) -> str:
    params = ", ".join(signature(fn))
    ret = f" -> {unparse(fn.returns)}" if fn.returns else ""
    prefix = "async " if isinstance(fn, ast.AsyncFunctionDef) else ""
    line = f"{prefix}{fn.name}({params}){ret}"
    if with_doc:
        doc = first_paragraph(fn)
        if doc:
            line += f"  # {doc}"
    return line


def is_dataclass(node: ast.ClassDef) -> bool:
    for deco in node.decorator_list:
        target = deco.func if isinstance(deco, ast.Call) else deco
        if unparse(target).split(".")[-1] == "dataclass":
            return True
    return False


def collect(src_root: Path, package: str, settings: dict):
    modules: dict[str, dict] = {}
    pkg = src_root / package
    functions = (ast.FunctionDef, ast.AsyncFunctionDef)
    for path in sorted(pkg.rglob("*.py")):
        if settings["skip_parts"] & set(path.parts):
            continue
        rel = path.relative_to(pkg)
        module = rel.parts[0] if len(rel.parts) > 1 else rel.stem
        if module in settings["skip_modules"]:
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        entry = modules.setdefault(module, {"configs": [], "widgets": [], "functions": []})
        for node in tree.body:
            if settings["functions"] and isinstance(node, functions):
                if not node.name.startswith("_"):
                    entry["functions"].append(
                        {"line": method_line(node), "doc": first_paragraph(node)}
                    )
                continue
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
                if isinstance(f, functions) and not f.name.startswith("_")
            ]
            full_doc = (ast.get_docstring(node) or "") if settings["full_docs"] else ""
            record = {
                "name": node.name,
                "doc": full_doc.strip() or first_doc_line(node),
                "params": params,
                "methods": [method_line(f, settings["full_docs"]) for f in public],
                "file": str(path.relative_to(src_root)),
            }
            is_config = node.name.endswith("Config") or (
                settings["dataclass_configs"] and is_dataclass(node)
            )
            if is_config:
                entry["configs"].append(record)
            else:
                entry["widgets"].append(record)
    return modules


def write_module_page(out: Path, package: str, module: str, entry: dict,
                      version: str, settings: dict) -> int:
    lines = [
        f"# {package}.{module}",
        "",
        f"Generated from {package} {version} source by `scripts/generate_reference.py`.",
        "",
    ]
    if entry["configs"]:
        heading = "Config and data classes" if settings["dataclass_configs"] else "Config classes"
        lines += [f"## {heading}", ""]
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
            if settings["full_docs"] and widget["params"]:
                lines.append("```python")
                lines.append(f"{widget['name']}({', '.join(widget['params'])})")
                lines.append("```")
                lines.append("")
            if widget["methods"]:
                lines.append("```python")
                for method in widget["methods"]:
                    lines.append(method)
                lines.append("```")
            lines.append("")
    if entry["functions"]:
        lines += ["## Functions", "", "```python"]
        for function in entry["functions"]:
            lines.append(function["line"])
            if function["doc"]:
                lines.append(f"    # {function['doc']}")
        lines += ["```", ""]
    text = "\n".join(lines).rstrip() + "\n"
    (out / f"{module}.md").write_text(text, encoding="utf-8")
    return len(text)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src_root = Path(sys.argv[1]).resolve()
    package = next((name for name in PACKAGES if (src_root / name).is_dir()), None)
    if package is None:
        print(f"error: {src_root} contains none of: {', '.join(PACKAGES)}")
        return 2
    settings = PACKAGES[package]
    out = SKILLS / settings["skill"] / "references" / package

    version = "unknown"
    init = (src_root / package / "__init__.py").read_text(encoding="utf-8")
    for node in ast.parse(init).body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__version__":
                    version = node.value.value

    modules = collect(src_root, package, settings)
    if out.exists():
        for stale in out.iterdir():
            if stale.is_file():
                stale.unlink()
    out.mkdir(parents=True, exist_ok=True)

    total = 0
    for module, entry in sorted(modules.items()):
        total += write_module_page(out, package, module, entry, version, settings)

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
                    helpers.append((f"{module}.{widget['name']}", method.split("  # ")[0]))

    index = [
        f"# {package} {version} API reference",
        "",
        "One page per module, generated from source. Load only the module you need.",
        "",
        "## Modules",
        "",
    ]
    for module, entry in sorted(modules.items()):
        counts = f"{len(entry['configs'])} config, {len(entry['widgets'])} widget"
        if entry["functions"]:
            counts += f", {len(entry['functions'])} function"
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
    (out / "index.md").write_text(text, encoding="utf-8")
    total += len(text)

    print(f"wrote {len(modules) + 1} files, {total:,} bytes into {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
