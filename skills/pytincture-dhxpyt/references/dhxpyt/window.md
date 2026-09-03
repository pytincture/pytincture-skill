# dhxpyt.window

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### WindowConfig
Configuration class for the Window widget.

```python
WindowConfig(
    closable: Optional[bool] = False,
    css: Optional[str] = None,
    footer: Optional[bool] = None,
    header: Optional[bool] = None,
    height: Optional[Union[int, str]] = '50%',
    html: Optional[str] = None,
    left: Optional[int] = None,
    minHeight: Optional[int] = 100,
    minWidth: Optional[int] = 100,
    modal: Optional[bool] = False,
    movable: Optional[bool] = False,
    node: Optional[Union[Any, str]] = None,
    resizable: Optional[bool] = False,
    title: Optional[str] = None,
    top: Optional[int] = None,
    viewportOverflow: Optional[bool] = False,
    width: Optional[Union[int, str]] = '50%',
)
```

## Widget classes

### Window

```python
attach(name: Union[str, Any], config: dict = None) -> None
attach_html(html: str) -> None
destructor() -> None
get_container() -> Any
get_position() -> Dict[str, int]
get_size() -> Dict[str, int]
get_widget() -> Any
hide() -> None
is_full_screen() -> bool
is_visible() -> bool
paint() -> None
set_full_screen() -> None
set_position(left: int, top: int) -> None
set_size(width: int, height: int) -> None
show(left: Optional[int] = None, top: Optional[int] = None) -> None
unset_full_screen() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_hide(handler: Callable[[Dict[str, int], Optional[Any]], None]) -> None
on_after_show(handler: Callable[[Dict[str, int]], None]) -> None
on_before_hide(handler: Callable[[Dict[str, int], Optional[Any]], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Dict[str, int]], Union[bool, None]]) -> None
on_header_double_click(handler: Callable[[Any], None]) -> None
on_move(handler: Callable[[Dict[str, int], Dict[str, int], Dict[str, bool]], None]) -> None
on_resize(handler: Callable[[Dict[str, int], Dict[str, int], Dict[str, bool]], None]) -> None
```
