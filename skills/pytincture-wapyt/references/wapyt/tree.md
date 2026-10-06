# wapyt.tree

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### TreeAction
One entry in the right-click menu.

Args:
    id: Emitted as ``action`` by ``on_action``.
    label: Visible text.
    icon: MDI class or ligature name.
    scope: ``any`` (default), ``branch`` (folders only) or ``leaf``.
    kinds: Show only on nodes whose ``data["kind"]`` is one of these —
        for trees whose branches are different things (a server, a
        database) that need different menus. Combines with ``scope``.
    requires: Show only on nodes whose ``data["flags"]`` list contains
        every one of these — for per-node features (what a node's backend
        supports, say) that ``kinds`` cannot express. Combines with the
        others.
    danger: Render in the destructive style.
    separator: When True, renders a divider and ignores every other field.

```python
TreeAction(
    id: str = '',
    label: Optional[str] = None,
    icon: Optional[str] = None,
    scope: str = 'any',
    kinds: Optional[List[str]] = None,
    requires: Optional[List[str]] = None,
    danger: bool = False,
    separator: bool = False,
)
```

### TreeConfig
Layout and behaviour for :class:`Tree`.

Args:
    items: Root nodes.
    selected: Node id selected on mount.
    expand_all: Expand every branch the first time it is indexed.
    filterable: Show a filter box. A match keeps its ancestors visible and
        forces them open while the filter is active.
    filter_placeholder: Placeholder for that box.
    empty_text: Shown when nothing matches.
    context_actions: Right-click menu entries.
    indent: Pixels of indent per depth level.
    extra: Additional properties forwarded to JS verbatim.

```python
TreeConfig(
    items: List[TreeItem] = field(default_factory=list),
    selected: Optional[str] = None,
    expand_all: bool = False,
    filterable: bool = False,
    filter_placeholder: Optional[str] = None,
    empty_text: Optional[str] = None,
    context_actions: List[TreeAction] = field(default_factory=list),
    indent: int = 14,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### TreeItem
One node. A node with ``items`` renders as a branch, otherwise a leaf.

Args:
    id: Unique identifier, emitted by every event.
    label: Visible text.
    icon: MDI class (``mdi-server``) or a Material Symbols ligature name,
        which ``wapyt.icons`` maps onto MDI. Branches default to
        ``mdi-folder``, leaves to ``mdi-file-outline``.
    open_icon: Icon used while a branch is expanded (default
        ``mdi-folder-open``).
    badge: Small pill after the label — a child count, say.
    tooltip: Title attribute; defaults to the label.
    items: Child nodes.
    data: Arbitrary metadata carried along in event payloads.

```python
TreeItem(
    id: str,
    label: Optional[str] = None,
    icon: Optional[str] = None,
    open_icon: Optional[str] = None,
    badge: Optional[Any] = None,
    tooltip: Optional[str] = None,
    items: List['TreeItem'] = field(default_factory=list),
    data: Dict[str, Any] = field(default_factory=dict),
)
```

## Widget classes

### Tree
A nested list of nodes.

Quick start::

    tree = Tree(
        TreeConfig(
            items=[TreeItem(id="prod", label="Production", items=[
                TreeItem(id="sess_1", label="web-01", icon="mdi-server"),
            ])],
            filterable=True,
            context_actions=[TreeAction("edit", "Edit", "mdi-pencil", scope="leaf")],
        ),
        container=layout.get_cell("sidebar"),
    )
    tree.on_activate(lambda payload: connect(payload["node"]))

Expansion state is keyed by node id and survives :meth:`set_items`, so
reloading the list does not collapse what the user opened. Use
:meth:`get_expanded` / :meth:`set_expanded` to persist it across sessions.

```python
Tree(config: Optional[TreeConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_select(handler: Callable[[Dict[str, Any]], Any]) -> None  # Node clicked: ``{"id": ..., "node": {...}}``.
on_activate(handler: Callable[[Dict[str, Any]], Any]) -> None  # Leaf double-clicked: ``{"id": ..., "node": {...}}``.
on_action(handler: Callable[[Dict[str, Any]], Any]) -> None  # Context-menu entry chosen: ``{"action", "id", "node"}``.
on_toggle(handler: Callable[[Dict[str, Any]], Any]) -> None  # Branch opened or closed: ``{"id": ..., "expanded": bool}``.
on_filter(handler: Callable[[Dict[str, Any]], Any]) -> None
set_items(items: List[TreeItem]) -> None
get_node(node_id: str) -> Optional[Dict[str, Any]]
get_parent_id(node_id: str) -> Optional[str]
select(node_id: Optional[str]) -> None
get_selected() -> Optional[str]
expand(node_id: str) -> None
collapse(node_id: str) -> None
toggle(node_id: str) -> None
expand_all() -> None
collapse_all() -> None
get_expanded() -> List[str]
set_expanded(node_ids: List[str]) -> None
set_filter(value: str) -> None
set_empty_text(text: str) -> None
destroy() -> None  # Tear down the context menu and its document-level listeners.
```
