# dhxpyt.kanban

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### KanbanCardConfig
Represents a single card rendered on the Kanban board.

```python
KanbanCardConfig(
    id: str,
    title: str,
    status: str,
    description: Optional[str] = None,
    lane: Optional[str] = None,
    assignee: Optional[str] = None,
    avatar: Optional[str] = None,
    priority: Optional[str] = None,
    due: Optional[str] = None,
    tags: List[str] = field(default_factory=list),
    progress: Optional[int] = None,
    meta: Dict[str, Any] = field(default_factory=dict),
    template: Optional[Any] = None,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### KanbanColumnConfig
High level column configuration. Columns own the cards rendered inside of

```python
KanbanColumnConfig(
    id: str,
    title: str,
    limit: Optional[int] = None,
    allow_drop: bool = True,
    allow_add: bool = True,
    collapsed: bool = False,
    badge: Optional[str] = None,
    order: Optional[int] = None,
    empty_text: Optional[str] = None,
    add_button_text: Optional[str] = None,
    template: Optional[Any] = None,
    cards: List[Union[KanbanCardConfig, Dict[str, Any]]] = field(default_factory=list),
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### KanbanConfig
Top level configuration payload for the custom Kanban widget.

```python
KanbanConfig(
    columns: List[Union[KanbanColumnConfig, Dict[str, Any]]] = field(default_factory=list),
    cards: List[Union[KanbanCardConfig, Dict[str, Any]]] = field(default_factory=list),
    lanes: Optional[List[Union[KanbanLaneConfig, Dict[str, Any]]]] = None,
    lane_field: str = 'lane',
    enable_lanes: bool = False,
    allow_card_drag: bool = True,
    allow_column_reorder: bool = False,
    add_column_text: Optional[str] = None,
    add_card_text: Optional[str] = 'Add card',
    title: Optional[str] = None,
    description: Optional[str] = None,
    theme: str = 'auto',
    card_template: Optional[Any] = None,
    column_template: Optional[Any] = None,
    empty_board_text: Optional[str] = None,
    board_id: Optional[str] = None,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### KanbanLaneConfig
Optional swimlane configuration that groups columns by `lane_field`.

```python
KanbanLaneConfig(
    id: str,
    title: str,
    description: Optional[str] = None,
    order: Optional[int] = None,
    collapsed: bool = False,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

## Widget classes

### Kanban
Python wrapper around the custom Kanban widget (mirrors the structure used

```python
register_card_template(name: str, factory: Any) -> None
register_column_template(name: str, factory: Any) -> None
on_card_click(handler: Callable[[Dict[str, Any]], Any]) -> None
on_card_move(handler: Callable[[Dict[str, Any]], Any]) -> None
on_card_create(handler: Callable[[Dict[str, Any]], Any]) -> None
on_column_create(handler: Callable[[Dict[str, Any]], Any]) -> None
on_column_toggle(handler: Callable[[Dict[str, Any]], Any]) -> None
load(config: KanbanConfig) -> None
reload(config: KanbanConfig) -> None
set_columns(columns: Iterable[Union[KanbanColumnConfig, Dict[str, Any]]]) -> None
set_cards(cards: Iterable[Union[KanbanCardConfig, Dict[str, Any]]]) -> None
set_lanes(lanes: Iterable[Union[KanbanLaneConfig, Dict[str, Any]]]) -> None
add_card(card: Union[KanbanCardConfig, Dict[str, Any]], *, index: Optional[int] = None) -> str
update_card(card_id: str, **updates) -> None
remove_card(card_id: str) -> None
move_card(card_id: str, *, to_column: str, lane: Optional[str] = None, index: Optional[int] = None) -> None
add_column(column: Union[KanbanColumnConfig, Dict[str, Any]], *, index: Optional[int] = None) -> str
update_column(column_id: str, **updates) -> None
remove_column(column_id: str) -> None
set_theme(theme: str) -> None
get_state() -> Dict[str, Any]
destroy() -> None
```
