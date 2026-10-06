# wapyt.sidebar

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### SidebarConfig
Controls Sidebar rendering/behavior.

Args:
    title: Optional heading rendered above the list.
    collapse_button: Whether the built-in collapse toggle is shown.
    collapsed: Initial collapsed state.
    items: List of :class:`SidebarItem` entries.
    active: ID to mark as selected when the widget mounts.

```python
SidebarConfig(
    title: Optional[str] = None,
    collapse_button: bool = True,
    collapsed: bool = False,
    items: List[SidebarItem] = field(default_factory=list),
    active: Optional[str] = None,
)
```

### SidebarItem
Represents a clickable entry in the Sidebar widget.

Args:
    id: Identifier emitted by `Sidebar.on_select`.
    label: Visible text.
    icon: Optional CSS class (e.g., Material icon).
    badge: Optional pill rendered to the right of the label.
    data: Arbitrary metadata forwarded to event handlers.

```python
SidebarItem(
    id: str,
    label: str,
    icon: Optional[str] = None,
    badge: Optional[str] = None,
    data: Dict[str, Any] = field(default_factory=dict),
)
```

## Widget classes

### Sidebar
Collapsible navigation rail that emits `select` events.

Quick start::

    sidebar = layout.add_sidebar("nav", SidebarConfig(items=[...]))
    sidebar.on_select(lambda item: print("Selected", item["id"]))
    sidebar.set_active("home")

```python
Sidebar(config: Optional[SidebarConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_select(handler: Callable[[Dict[str, Any]], Any]) -> None
collapse() -> None
expand() -> None
toggle() -> None
set_active(item_id: str) -> None
get_active() -> Optional[str]
```
