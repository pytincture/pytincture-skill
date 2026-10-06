# wapyt.contextmenu

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### ContextMenuConfig
Items and labelling for :class:`ContextMenu`.

Args:
    items: Entries in order; ``MenuItem(separator=True)`` for dividers.
    label: Accessible name of the menu.
    extra: Additional properties forwarded to JS verbatim.

```python
ContextMenuConfig(
    items: List[MenuItem] = field(default_factory=list),
    label: str = 'Context menu',
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### MenuItem
One menu entry.

Args:
    id: Emitted as ``id`` by ``on_select``; used by ``show_at(hide=...,
        disable=...)``. Must be unique across the whole menu, submenus
        included.
    label: Visible text; defaults to the id.
    icon: MDI class (``mdi-pencil``) or a Material Symbols name.
    shortcut: A hint shown on the right ("Ctrl+C"). Display only: the
        menu does not bind it.
    danger: Destructive styling.
    disabled: Shown but not choosable.
    items: A submenu. An item with ``items`` opens it instead of being
        selected.
    separator: A divider; every other field is ignored. Separators that
        would lead, trail or double up after hiding items are dropped.

```python
MenuItem(
    id: str = '',
    label: Optional[str] = None,
    icon: Optional[str] = None,
    shortcut: Optional[str] = None,
    danger: bool = False,
    disabled: bool = False,
    items: List['MenuItem'] = field(default_factory=list),
    separator: bool = False,
)
```

## Widget classes

### ContextMenu
A right-click menu, not mounted in a cell: it opens at the pointer.

Quick start::

    menu = ContextMenu(ContextMenuConfig(items=[
        MenuItem("open", "Open", "mdi-open-in-new", shortcut="Enter"),
        MenuItem("share", "Share", "mdi-share-variant", items=[
            MenuItem("copy_link", "Copy link", "mdi-link"),
            MenuItem("email", "Email…", "mdi-email-outline"),
        ]),
        MenuItem(separator=True),
        MenuItem("delete", "Delete", "mdi-delete", danger=True),
    ]))
    menu.attach("#files", context="files")
    menu.on_select(lambda p: handle(p["id"], p["target"]))

``attach`` opens it on right-click, Shift+F10 or the Menu key over an
element; ``target`` in the payload is the ``data-context`` attribute of the
nearest element under the pointer that has one (a row id, say). For full
control call ``show_at(x, y, context=..., hide=[...], disable=[...])``
from your own handler. Labels and hints are set as text, never markup.

```python
ContextMenu(config: Optional[ContextMenuConfig] = None)
```

```python
on_select(handler: Callable[[Dict[str, Any]], Any]) -> None  # An item was chosen: ``{"id", "context", "target"}``.
on_show(handler: Callable[[Dict[str, Any]], Any]) -> None  # The menu opened: ``{"context", "target"}``.
on_hide(handler: Callable[[Dict[str, Any]], Any]) -> None  # The menu closed, chosen or dismissed: ``{"context", "target"}``.
attach(target: Union[str, Any], context: Any = None) -> None  # Open on right-click, Shift+F10 or the Menu key over ``target`` (a CSS selector or element). ``context`` comes back in every payload.
detach(target: Union[str, Any, None] = None) -> None  # Stop opening over ``target``, or over everything when omitted.
show_at(x: float, y: float, *, context: Any = None, target: Optional[str] = None, hide: Optional[Iterable[str]] = None, disable: Optional[Iterable[str]] = None) -> None  # Open at viewport coordinates (``event.clientX`` / ``clientY``).
hide() -> None
is_open() -> bool
set_items(items: List[MenuItem]) -> None
destroy() -> None
```
