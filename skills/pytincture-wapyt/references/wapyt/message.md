# wapyt.message

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Functions

```python
toast_options(kind: str = 'info', timeout_ms: int = 4000) -> Dict[str, Any]
dialog_options(kind: str, text: str, *, title: Optional[str] = None, ok_text: Optional[str] = None, cancel_text: Optional[str] = None, danger: bool = False, value: Optional[str] = None, placeholder: Optional[str] = None, password: bool = False) -> Dict[str, Any]
toast(text: str, kind: str = 'info', timeout_ms: int = 4000) -> str
    # Show a toast at the bottom of the page and return its id.
dismiss(toast_id: str) -> bool
    # Remove one toast early. False when it has already gone.
dismiss_all() -> None
    # Remove every toast -- on sign-out, say.
async alert(text: str, *, title: Optional[str] = None, ok_text: str = 'OK') -> None
    # Show a message with one button; returns once it is acknowledged.
async confirm(text: str, *, title: Optional[str] = None, ok_text: str = 'OK', cancel_text: str = 'Cancel', danger: bool = False) -> bool
    # Ask a yes/no question. True only for the OK button.
async prompt(text: str, *, title: Optional[str] = None, value: str = '', placeholder: Optional[str] = None, ok_text: str = 'OK', cancel_text: str = 'Cancel', password: bool = False) -> Optional[str]
    # Ask for one line of text. Returns it, or None when cancelled.
```
