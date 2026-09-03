# dhxpyt.grid

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### GridColumnConfig
Configuration class for Grid columns.

```python
GridColumnConfig(
    id: str,
    header: List[Dict[str, Any]],
    type: str = None,
    width: int = None,
    align: str = None,
    adjust: bool = False,
    hidden: bool = False,
    sortable: bool = True,
    resizable: bool = True,
    tooltip: Union[bool, Dict[str, Any]] = True,
    css: str = None,
    htmlEnable: bool = False,
    editable: bool = False,
    filter: Dict[str, Any] = None,
    format: str = None,
    template: Callable[[Dict[str, Any]], str] = None,
    editorType: str = None,
    options: List[Dict[str, Any]] = None,
    gravity: int = None,
)
```

### GridConfig
Configuration class for the Grid widget.

```python
GridConfig(
    columns: List[GridColumnConfig],
    data: List[Dict[str, Any]] = None,
    adjust: Union[str, bool] = False,
    autoEmptyRow: bool = False,
    autoHeight: bool = False,
    autoWidth: bool = False,
    bottomSplit: int = None,
    collapsed: bool = False,
    css: str = None,
    type: str = None,
    dragCopy: bool = None,
    dragItem: str = None,
    dragMode: str = None,
    editable: bool = False,
    eventHandlers: Dict[str, Any] = None,
    exportStyles: Union[bool, List[str]] = False,
    footerAutoHeight: bool = False,
    footerRowHeight: int = 0,
    footerTooltip: Union[bool, Dict[str, Any]] = True,
    headerAutoHeight: bool = False,
    headerRowHeight: int = 40,
    headerTooltip: Union[bool, Dict[str, Any]] = True,
    height: Union[int, str] = None,
    htmlEnable: bool = False,
    keyNavigation: bool = True,
    leftSplit: int = None,
    multiselection: bool = False,
    resizable: bool = False,
    rightSplit: int = None,
    rowCss: Callable[[Dict[str, Any]], str] = None,
    rowHeight: int = 40,
    selection: Union[bool, str] = False,
    sortable: bool = True,
    spans: List[Dict[str, Any]] = None,
    tooltip: Union[bool, Dict[str, Any]] = True,
    topSplit: int = None,
    width: int = None,
)
```

## Widget classes

### Grid

```python
add_cell_css(row_id: Union[str, int], col_id: Union[str, int], css: str) -> None
add_row_css(row_id: Union[str, int], css: str) -> None
add_span(span_obj: Dict[str, Any]) -> None
adjust_column_width(col_id: Union[str, int], adjust: Union[str, bool] = None) -> None
destructor() -> None
edit_cell(row_id: Union[str, int], col_id: Union[str, int], editor_type: str = None) -> None
edit_end(without_save: bool = False) -> None
get_cell_rect(row_id: Union[str, int], col_id: Union[str, int]) -> Dict[str, Any]
get_column(col_id: Union[str, int]) -> Dict[str, Any]
get_header_filter(col_id: Union[str, int]) -> Any
get_scroll_state() -> Dict[str, int]
get_sorting_state() -> Dict[str, Any]
get_span(row_id: Union[str, int], col_id: Union[str, int]) -> Dict[str, Any]
hide_column(col_id: Union[str, int]) -> None
hide_row(row_id: Union[str, int]) -> None
is_column_hidden(col_id: Union[str, int]) -> bool
is_row_hidden(row_id: Union[str, int]) -> bool
paint() -> None
remove_cell_css(row_id: Union[str, int], col_id: Union[str, int], css: str) -> None
remove_row_css(row_id: Union[str, int], css: str) -> None
remove_span(row_id: Union[str, int], col_id: Union[str, int]) -> None
scroll(x: int = None, y: int = None) -> None
scroll_to(row_id: Union[str, int], col_id: Union[str, int]) -> None
set_columns(columns: List[Dict[str, Any]]) -> None
show_column(col_id: Union[str, int]) -> None
show_row(row_id: Union[str, int]) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_edit_end(handler: Callable[[Any, Dict[str, Any], Dict[str, Any]], None]) -> None
on_cell_click(handler: Callable[[Dict[str, Any], Dict[str, Any], Any], None]) -> None
on_cell_dbl_click(handler: Callable[[Dict[str, Any], Dict[str, Any], Any], None]) -> None
on_cell_mouse_down(handler: Callable[[Dict[str, Any], Dict[str, Any], Any], None]) -> None
on_cell_mouse_over(handler: Callable[[Dict[str, Any], Dict[str, Any], Any], None]) -> None
on_cell_right_click(handler: Callable[[Dict[str, Any], Dict[str, Any], Any], None]) -> None
on_before_row_drag(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_after_row_drag(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_before_column_drag(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_after_column_drag(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_row_drop(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_column_drop(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_drag_row_in(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_drag_row_out(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_drag_column_in(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_drag_column_out(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_drag_row_start(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_drag_column_start(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
select_cell(row: Union[Dict[str, Any], str, int] = None, column: Union[Dict[str, Any], str, int] = None, ctrl_up: bool = False, shift_up: bool = False) -> None
get_selected_cells() -> List[Dict[str, Any]]
unselect_cell(row_id: Union[str, int] = None, col_id: Union[str, int] = None) -> None
export_to_csv(config: Dict[str, Any] = None) -> str
export_to_pdf(config: Dict[str, Any] = None) -> None
export_to_png(config: Dict[str, Any] = None) -> None
export_to_xlsx(config: Dict[str, Any] = None) -> None
```
