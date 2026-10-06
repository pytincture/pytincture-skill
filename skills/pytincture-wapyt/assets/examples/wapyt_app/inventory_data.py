"""
Backend-for-frontend data class.

The implementation stays on the server; Pytincture packages a generated stub
with the same public methods for the browser, where each one is called through
its awaitable `name_async()` companion. Keep secrets, database clients and file
access in here -- never in browser modules.
"""
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from pytincture.dataclass import backend_for_frontend, bff_policy

# Pytincture executes this module's source afresh for every BFF call, so a
# module-level list would reset on each request. State lives in storage -- a
# JSON file here, a database in a real app -- and never in module globals.
# Outside the modules folder, which production mounts read-only.
STORE = Path(os.getenv("INVENTORY_STORE", Path(tempfile.gettempdir()) / "wapyt-inventory.json"))
SEED = [
    {"id": "1", "category": "tools", "name": "Hammer", "qty": 12, "price": 14.5},
    {"id": "2", "category": "tools", "name": "Screwdriver set", "qty": 4, "price": 22.0},
    {"id": "3", "category": "garden", "name": "Hose, 25 m", "qty": 7, "price": 31.0},
    {"id": "4", "category": "garden", "name": "Trowel", "qty": 0, "price": 6.75},
]
CATEGORIES = {"tools": "Tools", "garden": "Garden"}


def _load() -> list[dict]:
    try:
        return json.loads(STORE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return [dict(row) for row in SEED]


def _save(rows: list[dict]) -> None:
    tmp = STORE.with_suffix(".tmp")
    tmp.write_text(json.dumps(rows), encoding="utf-8")
    tmp.replace(STORE)


# `application` is compared against the running application, so it holds under
# every auth mode -- including this no-login service -- and stops another app
# reusing the export. Any @bff_policy makes a policy hook mandatory: see
# service.py. Never declare `roles` on an export a no-login service must serve;
# a caller with no identity has no roles, so that is an unconditional 403.
@backend_for_frontend
@bff_policy(application="inventory")
class InventoryData:
    def categories(self) -> list[dict]:
        return [{"id": key, "label": label} for key, label in CATEGORIES.items()]

    def items(self, category: str = "") -> list[dict]:
        return [row for row in _load() if not category or row["category"] == category]

    def add_item(self, category: str, name: str, qty: int, price: float) -> dict:
        # Client-side Form validation is a convenience; the server revalidates.
        name = (name or "").strip()
        if category not in CATEGORIES:
            return {"ok": False, "field": "category", "error": "Unknown category"}
        if not name:
            return {"ok": False, "field": "name", "error": "Name is required"}
        try:
            qty, price = int(qty), float(price)
        except (TypeError, ValueError):
            return {"ok": False, "field": None, "error": "Quantity and price must be numbers"}
        # Not safe under concurrent writers -- a real app uses its database's
        # transactions. (A module-level lock would not help: it is recreated
        # with the module on every call.)
        rows = _load()
        row = {"id": str(max((int(r["id"]) for r in rows), default=0) + 1),
               "category": category, "name": name, "qty": qty, "price": price}
        rows.append(row)
        _save(rows)
        return {"ok": True, "item": row}
