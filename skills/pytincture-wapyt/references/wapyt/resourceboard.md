# wapyt.resourceboard

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### ResourceBoardConfig
Configuration for the master/detail resource browser.

Args:
    items: Initial collection of :class:`ResourceItem` or dicts.
    selected_id: ID that should be selected on load.
    list_width: Constrains the list column (px).
    add_button_text: Label for the built-in add button.
    detail_template: HTML template populated with ``{placeholder}`` tokens.
        Interpolated values are HTML-escaped; use a key ending in ``Html``
        (e.g. ``{modelsHtml}``) to inject markup deliberately.
    empty_state: Text or markup rendered when no selection is active.
    title: Optional heading above the board.

```python
ResourceBoardConfig(
    items: List[Any] = field(default_factory=list),
    selected_id: Optional[str] = None,
    list_width: Optional[int] = None,
    add_button_text: Optional[str] = None,
    detail_template: Optional[str] = None,
    empty_state: Optional[str] = None,
    title: Optional[str] = None,
)
```

### ResourceItem
Item descriptor rendered inside the ResourceBoard list.

Args:
    id: Identifier returned by ``on_select`` / ``on_action`` callbacks.
    title: Primary label for the item.
    subtitle: Secondary label/supporting text.
    status: Textual status token (e.g., ``"active"``).
    badge: Small pill rendered next to the title.
    extra: Arbitrary metadata forwarded to the detail template context.

```python
ResourceItem(
    id: str,
    title: str,
    subtitle: Optional[str] = None,
    status: Optional[str] = None,
    badge: Optional[str] = None,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

## Widget classes

### ResourceBoard
Master/detail browser for resources with select/add/action events.

Quick start::

    board = layout.add_resourceboard("resources", ResourceBoardConfig(items=[...]))
    board.on_select(lambda item: print("Row selected:", item["id"]))
    board.on_action(lambda payload: handle(payload["action"], payload["id"]))

```python
ResourceBoard(config: Optional[ResourceBoardConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
set_items(items: List[Any]) -> None
select(item_id: Optional[str]) -> None
on_select(handler: Callable[[Dict[str, Any]], Any]) -> None
on_add(handler: Callable[[], Any]) -> None
on_action(handler: Callable[[Dict[str, Any]], Any]) -> None
```
