# dhxpyt.timepicker

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### TimepickerConfig
Configuration class for the TimePicker widget.

```python
TimepickerConfig(
    value: Union[Dict[str, int], str, int, list, object] = None,
    controls: bool = False,
    css: str = None,
    timeFormat: int = 24,
    valueFormat: str = None,
)
```

## Widget classes

### Timepicker

```python
clear() -> None
destructor() -> None
get_value(as_object: bool = False) -> Union[Dict[str, int], str]
paint() -> None
set_value(value: Union[Dict[str, int], str, int, list, object]) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_apply(handler: Callable[[Union[str, Dict[str, int]]], None]) -> None
on_after_close(handler: Callable[[Union[str, Dict[str, int]]], None]) -> None
on_before_apply(handler: Callable[[Union[str, Dict[str, int]]], Union[bool, None]]) -> None
on_before_change(handler: Callable[[Union[str, Dict[str, int]]], Union[bool, None]]) -> None
on_before_close(handler: Callable[[Union[str, Dict[str, int]]], Union[bool, None]]) -> None
on_change(handler: Callable[[Union[str, Dict[str, int]]], None]) -> None
```
