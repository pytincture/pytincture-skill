# dhxpyt.cardflow

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### CardFlowColumnConfig
Configuration class for CardFlow columns.

```python
CardFlowColumnConfig(
    id: str,
    header: Union[str, Dict[str, Any]],
    width: Union[int, str] = '100px',
    align: str = None,
    hidden: bool = False,
    css: str = None,
    dataType: str = 'str',
    dataFormat: str = '',
    applyFormat: bool = False,
    coltype: str = '',
)
```

### CardFlowConfig
Configuration class for the CardFlow widget.

```python
CardFlowConfig(
    columns: List[Union[Dict[str, Any], CardFlowColumnConfig]] = None,
    data: List[Dict[str, Any]] = None,
    editable: bool = True,
    group: Dict[str, Any] = None,
    groupable: bool = True,
    hideExpandCollapse: bool = False,
    autoCollapse: bool = False,
    optionItems: List[Dict[str, Any]] = None,
    sortDisabled: bool = False,
    showHeader: bool = True,
    showSort: bool = True,
    sortHeader: str = '',
    showDataHeaders: bool = True,
    showOptions: bool = True,
    fontSize: str = '',
    toolbar_font_family: str = '',
    cardHeight: str = None,
    stacked: bool = False,
    defaultExpandedHeight: str = '300px',
    gpu: bool = False,
    gpu_widget_id: str = '',
)
```

## Widget classes

### CardFlow
Wrapper class for the CardFlow widget.

```python
on_sort(handler: Callable) -> None
on_card_options(handler: Callable) -> None
on_card_expand(handler: Callable) -> None
on_card_collapse(handler: Callable) -> None
on_options(handler: Callable) -> None
update_header()
set_row_color(row_id, color)
set_row_font_size(row_id, font_size)
set_row_data_value(row_id, column_id, value)
toggle_header(show = None)
toggle_sort(show = None)
toggle_data_headers(show = None)
set_card_expanded_height(card_id: str, height: str) -> None
set_theme(theme: Union[str, Dict[str, Any]], css_vars: Optional[Dict[str, Dict[str, Any]]] = None) -> None
export_to_json() -> str
collapse_all() -> None
expand_all() -> None
add_layout(id: str = 'mainwindow', layout_config = None)
attach_to_card_content(cardid: str, widget: Any) -> None
detach_from_card_content(cardid: str) -> None
```
