# wapyt.datatable

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### ColumnConfig
One table column.

Args:
    id: Row key whose value this column displays.
    header: Header text; defaults to ``id``.
    width: Pixel width (int) or any CSS width (str).
    align: ``left`` · ``center`` · ``right``.
    sortable: Allow click-to-sort on this column.
    sort_by: Row key to sort on instead of ``id``. Use it when ``id`` holds
        a display string — sort a "1.2 MB" column by its byte count, or a
        formatted date by its epoch, so pre-formatting in Python does not
        break ordering.
    type: ``text`` (default) or ``icon``. An ``icon`` column takes an MDI
        class name as its value and renders it as a glyph.
    ellipsis: Truncate with an ellipsis and set a title tooltip
        (default True for text columns).
    icon_by: Row key holding an MDI class name drawn as a small glyph
        before a text cell's value -- a per-cell type or status marker.
        ``<icon_by>_title``, when the row has it, is the glyph's tooltip.

```python
ColumnConfig(
    id: str,
    header: Optional[str] = None,
    width: Optional[Union[int, str]] = None,
    align: Optional[str] = None,
    sortable: bool = True,
    sort_by: Optional[str] = None,
    type: str = 'text',
    ellipsis: bool = True,
    icon_by: Optional[str] = None,
)
```

### DataTableConfig
Layout and behaviour for :class:`DataTable`.

Args:
    columns: Column definitions in render order.
    rows: Initial rows (list of dicts).
    id_field: Row key holding the stable row id.
    selection: ``none`` · ``single`` · ``multi``. ``multi`` adds a checkbox
        column and supports ctrl/cmd and shift range clicks.
    sortable: Master switch for click-to-sort.
    sort_by / sort_dir: Initial sort column and direction.
    filterable: Show a filter box that matches across every column.
    filter_placeholder: Placeholder for that box.
    empty_text: Shown when there are no rows.
    loading_text: Shown while ``set_busy(True)``.
    drop_upload: Accept dropped files and emit ``on_drop``.
    context_actions: Right-click menu entries.
    group_dirs_first: Row key (typically ``is_dir``) whose truthy rows are
        kept above the rest whatever the active sort is.
    resizable_columns: Drag a header's right edge to resize its column.
        Once any column is resized every column gets a pixel width, and
        the table takes their sum (scrolling sideways when wider than
        its panel) instead of stretching them to fill it.
    reorderable_columns: Drag a header onto another to move its column.
    min_column_width: Narrowest a resize may make a column, in pixels.
    extra: Additional properties forwarded to JS verbatim.

```python
DataTableConfig(
    columns: List[ColumnConfig] = field(default_factory=list),
    rows: List[Dict[str, Any]] = field(default_factory=list),
    id_field: str = 'id',
    selection: str = 'single',
    sortable: bool = True,
    sort_by: Optional[str] = None,
    sort_dir: str = 'asc',
    filterable: bool = False,
    filter_placeholder: Optional[str] = None,
    empty_text: Optional[str] = None,
    loading_text: Optional[str] = None,
    drop_upload: bool = False,
    context_actions: List[TableAction] = field(default_factory=list),
    group_dirs_first: Optional[str] = None,
    resizable_columns: bool = False,
    reorderable_columns: bool = False,
    min_column_width: int = 48,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### TableAction
One entry in the right-click menu.

Args:
    id: Emitted as ``action`` by ``on_action``.
    label: Visible text.
    icon: MDI class name (``mdi-download``) or a Material Symbols ligature
        name, which ``wapyt.icons`` maps onto MDI.
    danger: Render in the destructive style.
    separator: When True, renders a divider and ignores every other field.

```python
TableAction(
    id: str = '',
    label: Optional[str] = None,
    icon: Optional[str] = None,
    danger: bool = False,
    separator: bool = False,
)
```

## Widget classes

### DataTable
A tabular list of dict rows.

Quick start::

    table = DataTable(
        DataTableConfig(
            columns=[
                ColumnConfig(id="name", header="Name"),
                ColumnConfig(id="size", header="Size", align="right",
                             sort_by="size_bytes"),
            ],
            selection="multi",
            group_dirs_first="is_dir",
            context_actions=[TableAction("download", "Download", "mdi-download")],
        ),
        container=tabs.get_cell("files"),
    )
    table.set_rows(entries)
    table.on_activate(lambda payload: navigate(payload["row"]))

Sorting and filtering run entirely in the browser against the rows already
loaded — no round trip. Pre-format values in Python (``size`` as "1.2 MB")
and point ``sort_by`` at the raw field so ordering stays correct.

```python
DataTable(config: Optional[DataTableConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_select(handler: Callable[[Dict[str, Any]], Any]) -> None  # Selection changed: ``{"ids": [...], "id": ..., "rows": [...]}``.
on_activate(handler: Callable[[Dict[str, Any]], Any]) -> None  # Row double-clicked: ``{"id": ..., "row": {...}}``.
on_action(handler: Callable[[Dict[str, Any]], Any]) -> None  # Context-menu entry chosen: ``{"action", "id", "row", "selected"}``.
on_sort(handler: Callable[[Dict[str, Any]], Any]) -> None
on_filter(handler: Callable[[Dict[str, Any]], Any]) -> None
on_columns(handler: Callable[[Dict[str, Any]], Any]) -> None  # A column was resized or moved (``resizable_columns`` / ``reorderable_columns``). Payload: ``{reason: "resize"|"reorder", column, columns: [{id, width}]}`` in display order; ``width`` is None for a column that has no pixel width yet.
on_drop(handler: Callable[[Dict[str, Any]], Any]) -> None  # Files dropped onto the table: ``{"files": [{"name", "size", "type"}]}``.
set_rows(rows: List[Dict[str, Any]]) -> None
get_rows() -> List[Dict[str, Any]]
get_row(row_id: str) -> Optional[Dict[str, Any]]
set_columns(columns: List[ColumnConfig]) -> None
get_column_state() -> List[Dict[str, Any]]  # ``[{id, width}]`` in display order (see :meth:`on_columns`).
move_column(column_id: str, target_id: str, after: bool = False) -> None  # Move a column before (or ``after``) another. Emits ``columns``.
get_dropped_files() -> Any  # The raw JS ``File`` handles from the most recent drop.
get_selected_ids() -> List[str]
get_selected_rows() -> List[Dict[str, Any]]
select(ids: Union[str, List[str]]) -> None
clear_selection() -> None
sort(column_id: str, direction: Optional[str] = None) -> None
set_filter(value: str) -> None
set_busy(busy: bool = True) -> None
set_empty_text(text: str) -> None
destroy() -> None  # Tear down the context menu and its document-level listeners.
```
