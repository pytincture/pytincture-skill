# dhxpyt.listbox

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### ListboxConfig
Configuration class for the ListBox widget.

```python
ListboxConfig(
    data: list = None,
    css: str = None,
    dragCopy: bool = False,
    dragMode: str = None,
    editable: bool = False,
    eventHandlers: Dict[str, Dict[str, Callable]] = None,
    height: Union[int, str] = 'auto',
    htmlEnable: bool = False,
    itemHeight: Union[int, str] = 37,
    keyNavigation: Union[bool, Callable[[], bool]] = True,
    multiselection: Union[bool, str] = False,
    selection: bool = True,
    template: Callable[[Dict[str, Any]], str] = None,
    virtual: bool = False,
)
```

## Widget classes

### Listbox

```python
destructor() -> None
edit_item(item_id: Union[str, int]) -> None
get_focus() -> Union[str, int]
get_focus_item() -> Dict[str, Any]
paint() -> None
reset_focus() -> None
set_focus(item_id: Union[str, int]) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_drag(handler: Callable[[Dict[str, Any], Any], None]) -> None
on_after_drop(handler: Callable[[Dict[str, Any], Any], None]) -> None
on_after_edit_end(handler: Callable[[str, Union[str, int]], None]) -> None
on_after_edit_start(handler: Callable[[Union[str, int]], None]) -> None
on_before_drag(handler: Callable[[Dict[str, Any], Any], Union[bool, None]]) -> None
on_before_drop(handler: Callable[[Dict[str, Any], Any], Union[bool, None]]) -> None
on_before_edit_end(handler: Callable[[str, Union[str, int]], Union[bool, None]]) -> None
on_before_edit_start(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_cancel_drop(handler: Callable[[Dict[str, Any], Any], None]) -> None
on_can_drop(handler: Callable[[Dict[str, Any], Any], None]) -> None
on_click(handler: Callable[[Union[str, int], Any], None]) -> None
on_double_click(handler: Callable[[Union[str, int], Any], None]) -> None
on_drag_in(handler: Callable[[Dict[str, Any], Any], Union[bool, None]]) -> None
on_drag_out(handler: Callable[[Dict[str, Any], Any], None]) -> None
on_drag_start(handler: Callable[[Dict[str, Any], Any], None]) -> None
on_focus_change(handler: Callable[[int, Union[str, int]], None]) -> None
on_item_mouse_over(handler: Callable[[Union[str, int], Any], None]) -> None
on_item_right_click(handler: Callable[[Union[str, int], Any], None]) -> None
```
