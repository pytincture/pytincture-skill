# dhxpyt.pagination

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### PaginationConfig
Configuration class for the Pagination widget.

```python
PaginationConfig(
    data: Any,
    css: str = None,
    inputWidth: int = 40,
    page: int = 0,
    pageSize: int = 10,
)
```

## Widget classes

### Pagination

```python
destructor() -> None
get_page() -> int
get_pages_count() -> int
get_page_size() -> int
set_page(page: int) -> None
set_page_size(size: int) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_change(handler: Callable[[int, int], None]) -> None
```
