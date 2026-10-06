"""
Browser entrypoint: a wapyt MainWindow with a Tree, a DataTable and a Form
in a ModalWindow, fed by the InventoryData BFF.

This module is shipped to the browser and runs in Pyodide. Server-only code
belongs in service.py and inventory_data.py.
"""
from __future__ import annotations

import asyncio
import traceback

import js
from pyodide.ffi import create_proxy

import widget  # noqa: F401 -- the backend resolves the widgetset from this import
from inventory_data import InventoryData
from wapyt import (
    CellConfig,
    ColumnConfig,
    DataTableConfig,
    FieldConfig,
    Form,
    FormConfig,
    LayoutConfig,
    MainWindow,
    ModalConfig,
    ModalWindow,
    SelectOption,
    TableAction,
    TreeConfig,
    TreeItem,
)

# pytincture's MainWindow detection only recognises dhxpyt's MainWindow, and
# the class is not named after the module, so declare the entrypoint or the
# app answers HTTP 422.
APP_ENTRYPOINT = "Inventory"

ALL = "all"

# wapyt sets no base font: layout headers and the modal title fall back to the
# browser's serif default unless the app styles them.
CSS = """
body, .wapyt-modal { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
"""


def spawn(coro, label: str):
    """asyncio.ensure_future swallows exceptions; report them instead."""

    async def guarded():
        try:
            await coro
        except Exception:  # noqa: BLE001 - last line of defence
            js.console.error(f"[inventory] {label} failed:\n{traceback.format_exc()}")

    return asyncio.ensure_future(guarded())


class Inventory(MainWindow):
    # A class-level layout_config replaces MainWindow's default
    # header + "mainwindow" cells. Cell ids are what every add_* helper takes.
    layout_config = LayoutConfig(
        rows=[
            CellConfig(id="header", height="auto"),
            CellConfig(
                id="body",
                grow=1,
                cols=[
                    CellConfig(id="nav", width="220px", header="Categories"),
                    CellConfig(id="items", width="100%"),
                ],
            ),
        ]
    )

    # No __init__: the LoadUICaller metaclass calls load_ui() after
    # construction, and defining both builds the UI twice.
    def load_ui(self) -> None:
        self.set_theme("dark")
        style = js.document.createElement("style")
        style.textContent = CSS
        js.document.head.appendChild(style)

        self.category = ALL
        self.categories: list[dict] = []

        self.attach_html(
            "header",
            '<div style="display:flex;gap:1rem;align-items:center;padding:.5rem 1rem">'
            "<strong>Inventory</strong>"
            '<button id="add-item" type="button">Add item</button></div>',
        )
        # attach_html markup is raw HTML: escape anything that came from data.
        js.document.getElementById("add-item").addEventListener(
            "click", self._proxy(lambda _event: self.open_add_dialog())
        )

        self.tree = self.add_tree(
            "nav",
            TreeConfig(items=[TreeItem(id=ALL, label="All items", icon="mdi-package-variant")],
                       selected=ALL),
        )
        self.tree.on_select(lambda payload: self.select_category(payload["id"]))

        self.table = self.add_datatable(
            "items",
            DataTableConfig(
                columns=[
                    ColumnConfig(id="name", header="Name"),
                    ColumnConfig(id="qty", header="Qty", align="right", width=80),
                    # Pre-format for display, sort on the raw number.
                    ColumnConfig(id="price_text", header="Price", align="right",
                                 width=100, sort_by="price"),
                ],
                filterable=True,
                empty_text="No items",
                context_actions=[TableAction("restock", "Restock", "mdi-truck")],
            ),
        )
        self.table.on_action(lambda payload: js.console.log(
            f"{payload['action']} -> {payload['id']}"))

        spawn(self.refresh(), "initial load")

    # -- helpers -----------------------------------------------------------

    def _proxy(self, fn):
        proxy = create_proxy(fn)
        self.__dict__.setdefault("_proxies", []).append(proxy)  # keep alive
        return proxy

    async def refresh(self) -> None:
        self.table.set_busy(True)
        try:
            if not self.categories:
                self.categories = await InventoryData().categories_async()
                self.tree.set_items([
                    TreeItem(id=ALL, label="All items", icon="mdi-package-variant",
                             items=[TreeItem(id=c["id"], label=c["label"], icon="mdi-tag")
                                    for c in self.categories]),
                ])
                self.tree.expand(ALL)
            category = "" if self.category == ALL else self.category
            rows = await InventoryData().items_async(category)
            for row in rows:
                row["price_text"] = f"${row['price']:,.2f}"
            self.table.set_rows(rows)
        finally:
            self.table.set_busy(False)

    def select_category(self, node_id: str) -> None:
        self.category = node_id
        spawn(self.refresh(), "category change")

    def open_add_dialog(self) -> None:
        # Built per use, so dispose_on_close removes it on x / Escape / backdrop
        # instead of leaving a hidden overlay in the DOM.
        # The declared height is honest: content taller than it scrolls inside
        # the body, so size it to fit the fields plus the button row.
        modal = ModalWindow(ModalConfig(title="Add item", width=420, height=460,
                                        dispose_on_close=True))
        form = Form(
            FormConfig(
                fields=[
                    FieldConfig(id="category", label="Category", type="select", required=True,
                                options=[SelectOption(c["id"], c["label"]) for c in self.categories],
                                value=self.category if self.category != ALL else None),
                    FieldConfig(id="name", label="Name", required=True),
                    FieldConfig(id="qty", label="Quantity", type="number", value=1, min=0),
                    FieldConfig(id="price", label="Price", type="number", value=0, min=0, step=0.01),
                ],
                submit_text="Add",
                cancel_text="Cancel",
            ),
            container=modal.body,  # mount into the body; set_content would replace it
        )
        form.on_cancel(lambda _values: modal.close())
        form.on_submit(lambda values: spawn(self.submit_item(modal, form, values), "add item"))
        modal.show()
        form.focus_first()

    async def submit_item(self, modal: ModalWindow, form: Form, values: dict) -> None:
        form.set_busy(True)
        try:
            result = await InventoryData().add_item_async(
                values["category"], values["name"], values["qty"], values["price"])
        finally:
            form.set_busy(False)
        if not result.get("ok"):
            form.set_error(result.get("field"), result.get("error", "Failed"))
            return
        modal.close()
        await self.refresh()
