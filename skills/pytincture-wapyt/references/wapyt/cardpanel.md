# wapyt.cardpanel

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### CardPanelCardConfig
Represents an individual card shown inside the CardPanel widget.

Args:
    id: Stable identifier emitted with callbacks.
    title: Primary text rendered in the card header.
    subtitle: Secondary text below the title (optional).
    pill: Optional badge rendered next to the subtitle.
    icon: Optional class name or URL consumed by templates.
    extra: Arbitrary metadata accessible via placeholders.

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

The ``card_template`` option may be:

* the name of a registered template (string)
* a callable/JS function handle
* a nested dictionary describing DOM structure. The descriptor supports keys:
    - ``tag``: element tag name (default ``div``)
    - ``class``/``className``/``classes``: string or list of classes
    - ``text`` or ``html``: content strings. Placeholders like ``{title}``
      or ``{card.subtitle}`` are interpolated from the card/context.
      Values interpolated into ``html`` are HTML-escaped; use ``text``
      or a registered template when you need to emit markup.
    - ``attrs``/``dataset``/``style``: mapping of attributes with placeholders
    - ``children``: list of nested descriptor nodes

Additional convenience properties:

* ``card_columns`` – integer column count translated into CSS grid template.
* ``viewport_height`` – constrains the grid height and enables scrolling.
* ``card_gap`` / ``card_min_height`` / ``card_height`` – tune card spacing.
* ``add_button_text`` / ``search_placeholder`` – copy for built-in chrome
  (``"Add"`` / ``"Search…"`` when unset).
* ``title`` / ``description`` default to empty; an empty description hides
  its row.

```python
CardPanelConfig(
    title: str = '',
    description: str = '',
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
    card_height: Optional[Union[int, float, str]] = None,
    card_gap: Optional[Union[int, float, str]] = None,
    card_columns: Optional[int] = None,
    card_icon_size: Optional[Union[int, float, str]] = None,
    viewport_height: Optional[Union[int, float, str]] = None,
    card_template: Optional[Any] = None,
)
```

## Widget classes

### CardPanel
Python wrapper for the custom CardPanel widget.

Quick start::

    layout = Layout(LayoutConfig(rows=[CellConfig(id="cards", grow=1)]))
    panel = layout.add_cardpanel("cards", CardPanelConfig(cards=[...]))
    panel.on_action(lambda payload: handle_click(payload["action"], payload["cardId"]))

Use `load`/`add_card` to refresh cards and `register_template` when you
need fine-grained control over the rendered HTML.

```python
CardPanel(config: Optional[CardPanelConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
register_template(name: str, factory: Any) -> None  # Register a template factory with the underlying JavaScript widget.
get_template(name: str) -> Any  # Retrieve a previously registered template factory from the JS layer (if available).
on_search(handler: Callable[[str], Any]) -> None
on_add(handler: Callable[[], Any]) -> None
on_view(handler: Callable[[Any], Any]) -> None
on_card_click(handler: Callable[[Any], Any]) -> None
on_action(handler: Callable[[Dict[str, Any]], Any]) -> None
load(cards: Iterable[Union[CardPanelCardConfig, Dict[str, Any]]]) -> None
add_card(card: Union[CardPanelCardConfig, Dict[str, Any]]) -> None
filter(query: str) -> None  # Access the underlying filter logic (mirrors the JS helper).
destroy() -> None  # Tears down DOM content created for the widget (best-effort).
```
