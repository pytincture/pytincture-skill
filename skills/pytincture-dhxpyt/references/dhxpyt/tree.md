# dhxpyt.tree

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### TreeConfig
Configuration class for the Tree widget.

```python
TreeConfig(
    data: Optional[List[TreeItemConfig]] = None,
    checkbox: Optional[bool] = None,
    collapsed: Optional[bool] = None,
    css: Optional[str] = None,
    dragCopy: Optional[bool] = None,
    dragMode: Optional[str] = None,
    dropBehaviour: Optional[str] = None,
    editable: Optional[bool] = None,
    icon: Optional[dict] = None,
    itemHeight: Optional[Union[int, str]] = None,
    keyNavigation: Optional[bool] = None,
    rootId: Optional[Union[str, int]] = None,
    selection: Optional[bool] = None,
    template: Optional[Callable[[dict, bool], str]] = None,
)
```

### TreeItemConfig

```python
TreeItemConfig(
    id: Optional[Union[str, int]] = None,
    value: Optional[str] = None,
    opened: Optional[bool] = None,
    checkbox: Optional[bool] = None,
    items: Optional[List['TreeItemConfig']] = None,
    icon: Optional[dict] = None,
)
```

## Widget classes

### Tree

```python
check_item(id: Union[str, int]) -> None
collapse(id: Union[str, int]) -> None
collapse_all() -> None
destructor() -> None
edit_item(id: Union[str, int], config: dict = None) -> None
expand(id: Union[str, int]) -> None
expand_all() -> None
focus_item(id: Union[str, int]) -> None
get_checked() -> List[Union[str, int]]
get_state() -> Dict[str, Dict[str, Union[int, bool]]]
paint() -> None
set_state(state: Dict[str, Dict[str, Union[int, bool]]]) -> None
toggle(id: Union[str, int]) -> None
uncheck_item(id: Union[str, int]) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_check(handler: Callable[[int, Union[str, int], bool], None]) -> None
on_after_collapse(handler: Callable[[Union[str, int]], None]) -> None
on_after_drag(handler: Callable[[dict, Any], Any]) -> None
on_after_drop(handler: Callable[[dict, Any], None]) -> None
on_after_edit_end(handler: Callable[[str, Union[str, int]], None]) -> None
on_after_edit_start(handler: Callable[[str, Union[str, int]], None]) -> None
on_after_expand(handler: Callable[[Union[str, int]], None]) -> None
on_before_check(handler: Callable[[int, Union[str, int]], Union[bool, None]]) -> None
on_before_collapse(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_before_drag(handler: Callable[[dict, Any, Any], Union[bool, None]]) -> None
on_before_drop(handler: Callable[[dict, Any], Union[bool, None]]) -> None
on_before_edit_end(handler: Callable[[str, Union[str, int]], Union[bool, None]]) -> None
on_before_edit_start(handler: Callable[[str, Union[str, int]], Union[bool, None]]) -> None
on_before_expand(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
```
