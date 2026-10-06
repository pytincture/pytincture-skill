# wapyt.toolbar

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### ToolbarButton
A button.

Args:
    id: Emitted as ``id`` by ``on_click``; addresses the button in every
        ``set_*`` method.
    label: Visible text. In compact mode it hides behind the icon and stays
        as the tooltip and accessible name.
    icon: MDI class (``mdi-plus``) or a Material Symbols name.
    tooltip: Hover text; defaults to the label.
    variant: ``default``, ``primary``, ``accent`` (a highlighted call to
        action, such as an update notice) or ``danger``.
    toggle: A button that stays pressed until clicked again.
    group: Buttons sharing a group are one-of-several choices: pressing one
        releases the others. Implies a pressed state.
    active: Initial pressed state, for ``toggle`` and ``group`` buttons.
    badge: Small count or tag after the label.
    disabled / hidden: Initial state; change with ``set_disabled`` /
        ``set_hidden``.
    show_label: False for an icon-only button (the label becomes its name).
    keep_label: Keep the label visible in compact mode.

```python
ToolbarButton(
    id: str,
    label: Optional[str] = None,
    icon: Optional[str] = None,
    tooltip: Optional[str] = None,
    variant: str = 'default',
    toggle: bool = False,
    group: Optional[str] = None,
    active: bool = False,
    badge: Optional[Union[int, str]] = None,
    disabled: bool = False,
    hidden: bool = False,
    show_label: bool = True,
    keep_label: bool = False,
)
```

### ToolbarConfig
Layout and behaviour for :class:`Toolbar`.

Args:
    items: Buttons, text, separators and spacers in order.
    label: Accessible name of the toolbar (``aria-label``).
    compact: ``auto`` (default) drops button labels to icons when the
        labelled toolbar no longer fits; ``always`` or ``never`` force it.
    extra: Additional properties forwarded to JS verbatim.

```python
ToolbarConfig(
    items: List[Any] = field(default_factory=list),
    label: str = 'Toolbar',
    compact: str = 'auto',
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### ToolbarSeparator
A thin vertical divider.

_No keyword parameters._

### ToolbarSpacer
Takes the free space, pushing what follows to the right.

_No keyword parameters._

### ToolbarText
Plain text, such as the signed-in user's name. ``set_text`` changes it.

```python
ToolbarText(
    id: str,
    text: str = '',
    hidden: bool = False,
)
```

## Widget classes

### Toolbar
A row of buttons.

Quick start::

    toolbar = self.add_toolbar("header", ToolbarConfig(items=[
        ToolbarButton("new", "New connection", "mdi-plus"),
        ToolbarButton("refresh", "Refresh", "mdi-refresh"),
        ToolbarSeparator(),
        ToolbarButton("tabbed", icon="mdi-table-row", tooltip="Tabs",
                      group="layout", active=True, show_label=False),
        ToolbarButton("tiled", icon="mdi-view-grid", tooltip="Tiles",
                      group="layout", show_label=False),
        ToolbarSpacer(),
        ToolbarButton("update", "Update", "mdi-arrow-up-circle",
                      variant="accent", hidden=True),
        ToolbarText("user"),
        ToolbarButton("logout", "Logout", "mdi-logout"),
    ]))
    toolbar.on_click(lambda p: self.on_toolbar(p["id"]))
    toolbar.set_text("user", me["username"])

Labels, tooltips, badges and text are set as text, never markup.

```python
Toolbar(config: Optional[ToolbarConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_click(handler: Callable[[Dict[str, Any]], Any]) -> None  # A button was clicked: ``{"id", "group", "active"}``. ``active`` is the new pressed state for toggle and group buttons, else None.
set_items(items: List[Any]) -> None  # Replace every item (validated like ``ToolbarConfig.items``).
set_text(item_id: str, text: str) -> None  # Change a button's label or a text item's text.
set_tooltip(item_id: str, tooltip: str) -> None
set_icon(item_id: str, icon: str) -> None
set_badge(item_id: str, badge: Optional[Union[int, str]]) -> None  # Show a badge on a button; ``None`` or ``""`` removes it.
set_disabled(item_id: str, disabled: bool = True) -> None
set_hidden(item_id: str, hidden: bool = True) -> None
set_active(item_id: str, active: bool = True) -> None  # Press or release a toggle; pressing a group button releases the rest.
is_active(item_id: str) -> bool
get_active(group: str) -> Optional[str]  # The pressed button's id in a group, or None.
destroy() -> None
```
