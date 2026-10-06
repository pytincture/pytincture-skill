# wapyt.tabwidget

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### TabConfig
Describes a single tab strip entry.

Args:
    id: Unique identifier for the tab.
    title: Visible label.
    icon: Optional CSS class name for leading icon.
    closable: Whether the close icon should appear.
    badge: Optional numeric or string badge.
    disabled: Prevents interaction when True.
    html: Static markup injected when the tab renders.

```python
TabConfig(
    id: str,
    title: str,
    icon: Optional[str] = None,
    closable: bool = False,
    badge: Optional[Union[int, str]] = None,
    disabled: bool = False,
    html: Optional[str] = None,
)
```

### TabWidgetConfig
Layout/behavior options for :class:`TabWidget`.

Args:
    tabs: Initial list of :class:`TabConfig`.
    active: Tab ID that should start active.
    orientation: ``"top"`` or ``"left"`` (defaults to ``"top"``).
    fill_height: Stretch panel to consume vertical space.
    keep_alive: Whether hidden tabs stay mounted.
    extra: Additional properties forwarded to JS (feature flags).

```python
TabWidgetConfig(
    tabs: List[TabConfig] = field(default_factory=list),
    active: Optional[str] = None,
    orientation: str = 'top',
    fill_height: bool = True,
    keep_alive: bool = True,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

## Widget classes

### TabWidget
Minimal tab system.

Quick start::

    tabs = layout.add_tabwidget("body", TabWidgetConfig(
        tabs=[TabConfig(id="chat", title="Chat")]
    ))
    tabs.attach_html("chat", "<h1>Hello</h1>")
    tabs.on_change(lambda tab_id: print("Active tab:", tab_id))

```python
TabWidget(config: Optional[TabWidgetConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_change(handler: Callable[[str], Any]) -> None
on_close(handler: Callable[[str], Any]) -> None
on_ready(handler: Callable[[], Any]) -> None
add_tab(tab: Union[TabConfig, Dict[str, Any]], index: Optional[int] = None) -> None
remove_tab(tab_id: str) -> None
set_active(tab_id: str) -> None
get_active() -> Optional[str]
attach_html(tab_id: str, html: str) -> None
attach(tab_id: str, component: Any) -> None
set_badge(tab_id: str, badge: Optional[Union[int, str]]) -> None
disable_tab(tab_id: str) -> None
enable_tab(tab_id: str) -> None
get_cell(tab_id: str) -> Any
```
