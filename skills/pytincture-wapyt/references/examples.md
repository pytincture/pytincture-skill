# Bundled example

## Service-mode app

`assets/examples/wapyt_app/`

| File | Role |
|---|---|
| `service.py` | ASGI entrypoint: `create_app` + `PytinctureConfig`, policy hook by dotted path |
| `inventory.py` | browser entrypoint: `APP_ENTRYPOINT`, `MainWindow` with a Tree, a DataTable, and a Form in a ModalWindow |
| `inventory_data.py` | `@backend_for_frontend` class; state in a JSON file, never module globals |
| `widget.py` | literal `__widgetset__`/`__version__` for the backend |

Run it:

```bash
cd assets/examples/wapyt_app
/path/to/wa_pytincture_widgetset/scripts/dev_wheel.sh .   # the browser wheel
python -m uvicorn service:app --port 8070                 # then open http://127.0.0.1:8070/inventory
```

Data lives in `$INVENTORY_STORE` (default `<tmp>/wapyt-inventory.json`).

What to copy from it:

- `load_ui()` builds the widgets and returns; `spawn(self.refresh(), ...)`
  then awaits `InventoryData().items_async()` and fills the table. `spawn`
  logs exceptions that `asyncio.ensure_future` would otherwise swallow.
- The Tree is re-filled with `set_items()` using the same node ids, so its
  expansion state survives.
- The price column shows a pre-formatted string and sorts on the raw number
  through `ColumnConfig(sort_by="price")`.
- The Form is mounted into `modal.body`; the modal is built per use with
  `dispose_on_close=True` and closed explicitly on success and cancel.
- The BFF revalidates every field and returns `{"ok": False, "field", "error"}`,
  which the browser shows with `form.set_error(...)`.
