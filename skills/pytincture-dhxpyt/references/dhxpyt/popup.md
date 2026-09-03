# dhxpyt.popup

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### PopupConfig
Configuration class for the Popup widget.

```python
PopupConfig(
    css: str = None,
)
```

### PopupShowConfig
Configuration class for the 'show' method of the Popup widget.

```python
PopupShowConfig(
    centering: bool = True,
    auto: bool = False,
    mode: str = 'bottom',
    indent: int = 0,
)
```

## Widget classes

### Popup

```python
attach(name: Union[str, Any], config: Dict[str, Any] = None) -> Any
attach_html(html: str) -> None
destructor() -> None
get_container() -> Any
get_widget() -> Any
hide() -> None
is_visible() -> bool
paint() -> None
show(node: Any, config: PopupShowConfig = None) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_hide(handler: Callable[[Any], None]) -> None
on_after_show(handler: Callable[[Any], None]) -> None
on_before_hide(handler: Callable[[bool, Any], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Any], Union[bool, None]]) -> None
on_click(handler: Callable[[Any], None]) -> None
```
