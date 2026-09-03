# dhxpyt.slider

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### SliderConfig
Configuration class for the Slider widget.

```python
SliderConfig(
    min: float,
    max: float,
    step: float = 1,
    value: Union[float, str, list] = None,
    css: str = None,
    helpMessage: str = None,
    hiddenLabel: bool = None,
    inverse: bool = None,
    label: str = None,
    labelPosition: str = None,
    labelWidth: Union[str, int] = None,
    majorTick: float = None,
    mode: str = 'horizontal',
    range: bool = None,
    tick: float = None,
    tickTemplate: Callable[[float], str] = None,
    tooltip: bool = True,
)
```

## Widget classes

### Slider

```python
blur() -> None
destructor() -> None
disable() -> None
enable() -> None
focus(extra: bool = None) -> None
get_value() -> List[float]
is_disabled() -> bool
paint() -> None
set_value(value: Union[str, float, List[float]]) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_before_change(handler: Callable[[float, float, bool], Union[bool, None]]) -> None
on_blur(handler: Callable[[], None]) -> None
on_change(handler: Callable[[float, float, bool], None]) -> None
on_focus(handler: Callable[[], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
on_mousedown(handler: Callable[[Any], None]) -> None
on_mouseup(handler: Callable[[Any], None]) -> None
```
