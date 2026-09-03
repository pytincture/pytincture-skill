# dhxpyt.calendar

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### CalendarConfig
Configuration class for Calendar.

```python
CalendarConfig(
    date: Union[str, Any] = None,
    date_format: str = '%d/%m/%y',
    disabled_dates: Callable[[Any], bool] = None,
    mark: Callable[[Any], str] = None,
    mode: str = 'calendar',
    range: bool = False,
    this_month_only: bool = False,
    time_format: int = 24,
    time_picker: bool = False,
    value: Union[str, Any, List[Union[str, Any]]] = None,
    week_numbers: bool = False,
    week_start: str = 'sunday',
    css: str = None,
    width: Union[int, str] = '250px',
)
```

### ControlConfig

_No keyword parameters._

## Widget classes

### Calendar
A Python wrapper for the DHX Calendar JavaScript widget.

```python
clear() -> None
destructor() -> None
get_current_mode() -> str
get_value(as_date_obj: bool = False) -> Union[str, List[str]]
link(calendar: Any) -> None
paint() -> None
set_value(value: Union[str, List[str]]) -> bool
show_date(date: Union[str, None] = None, mode: str = 'calendar') -> None
add_event_handler(event_name: str, handler: Callable) -> None
before_change(handler: Callable[[str, str, bool], Union[bool, None]]) -> None
cancel_click(handler: Callable[[], None]) -> None
change(handler: Callable[[str, str, bool], None]) -> None
date_mouse_over(handler: Callable[[str, str], None]) -> None
mode_change(handler: Callable[[str], None]) -> None
month_selected(handler: Callable[[int], None]) -> None
year_selected(handler: Callable[[int], None]) -> None
css() -> str
css(value: str) -> None
date() -> str
date(value: str) -> None
date_format() -> str
date_format(value: str) -> None
disabled_dates() -> Callable[[str], bool]
disabled_dates(value: Callable[[str], bool]) -> None
mark() -> Callable[[str], str]
mark(value: Callable[[str], str]) -> None
mode() -> str
mode(value: str) -> None
range() -> bool
range(value: bool) -> None
this_month_only() -> bool
this_month_only(value: bool) -> None
time_format() -> int
time_format(value: int) -> None
time_picker() -> bool
time_picker(value: bool) -> None
value() -> Union[str, List[str]]
value(value: Union[str, List[str]]) -> None
week_numbers() -> bool
week_numbers(value: bool) -> None
week_start() -> str
week_start(value: str) -> None
width() -> Union[str, int]
width(value: Union[str, int]) -> None
```
