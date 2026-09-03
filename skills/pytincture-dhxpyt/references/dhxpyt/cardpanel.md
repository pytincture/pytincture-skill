# dhxpyt.cardpanel

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### CardPanelCardConfig
Represents an individual card shown inside the CardPanel widget.

```python
CardPanelCardConfig(
    id: str,
    title: str,
    subtitle: Optional[str] = None,
    pill: Optional[str] = None,
    icon: Optional[str] = None,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### CardPanelConfig
High-level configuration for the CardPanel widget.

```python
CardPanelConfig(
    title: str = 'Data Sources',
    description: str = 'Manage and connect to various data sources with intelligent profiling and lineage tracking.',
    searchable: bool = True,
    auto_filter: bool = True,
    cards: List[Any] = field(default_factory=list),
    add_button_text: Optional[str] = None,
    search_button_text: Optional[str] = None,
    search_placeholder: Optional[str] = None,
    search_aria_label: Optional[str] = None,
    show_search: Optional[bool] = None,
    view_button_text: Optional[str] = None,
    card_min_width: Optional[Union[int, float, str]] = None,
    card_min_height: Optional[Union[int, float, str]] = None,
    card_max_height: Optional[Union[int, float, str]] = None,
    card_gap: Optional[Union[int, float, str]] = None,
    card_columns: Optional[int] = None,
    card_icon_size: Optional[Union[int, float, str]] = None,
    card_template: Optional[Any] = None,
)
```

## Widget classes

### CardPanel
Python wrapper for the custom CardPanel widget.

```python
register_template(cls, name: str, factory: Any) -> None
get_template(cls, name: str) -> Any
on_search(handler: Callable[[str], Any]) -> None
on_add(handler: Callable[[], Any]) -> None
on_view(handler: Callable[[Any], Any]) -> None
on_card_click(handler: Callable[[Any], Any]) -> None
load(cards: Iterable[Union[CardPanelCardConfig, Dict[str, Any]]]) -> None
add_card(card: Union[CardPanelCardConfig, Dict[str, Any]]) -> None
filter(query: str) -> None
destroy() -> None
```
