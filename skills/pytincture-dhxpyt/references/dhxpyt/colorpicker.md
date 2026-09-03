# dhxpyt.colorpicker

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### ColorpickerConfig
Configuration class for Colorpicker. Contains properties to customize the colorpicker.

```python
ColorpickerConfig(
    css: str = None,
    customColors: List[str] = None,
    grayShades: bool = True,
    mode: str = 'palette',
    palette: List[List[str]] = None,
    paletteOnly: bool = False,
    pickerOnly: bool = False,
    transparency: bool = True,
    width: Union[str, int] = '238px',
)
```

## Widget classes

### Colorpicker

```python
clear() -> None
destructor() -> None
get_current_mode() -> str
get_custom_colors() -> List[str]
get_value() -> str
paint() -> None
set_current_mode(view: str) -> None
set_custom_colors(custom_colors: List[str]) -> None
set_focus(value: str) -> None
set_value(value: str) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_apply(handler: Callable[[], None]) -> None
on_before_change(handler: Callable[[str], Union[bool, None]]) -> None
on_cancel_click(handler: Callable[[], None]) -> None
on_change(handler: Callable[[str], None]) -> None
on_mode_change(handler: Callable[[str], None]) -> None
css() -> str
css(value: str) -> None
custom_colors() -> List[str]
custom_colors(value: List[str]) -> None
gray_shades() -> bool
gray_shades(value: bool) -> None
mode() -> str
mode(value: str) -> None
palette() -> List[List[str]]
palette(value: List[List[str]]) -> None
palette_only() -> bool
palette_only(value: bool) -> None
picker_only() -> bool
picker_only(value: bool) -> None
transparency() -> bool
transparency(value: bool) -> None
width() -> Union[str, int]
width(value: Union[str, int]) -> None
```
