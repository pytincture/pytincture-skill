# wapyt.modal

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### ModalConfig
Declarative options for :class:`ModalWindow`.

Args:
    title: Header text displayed at the top of the modal.
    width: Pixel value or CSS size for the modal; defaults to ``520``.
    height: Pixel value or CSS size for the modal; defaults to ``360``.
    closable: When ``False`` the chrome hides the close affordance.
    dispose_on_close: The close button, Escape and a backdrop click remove
        the dialog (as :meth:`ModalWindow.close` does) instead of hiding
        it. For a modal built per use; leave it off for one that is built
        once and shown again.

```python
ModalConfig(
    title: str = '',
    width: Union[int, str] = 520,
    height: Union[int, str] = 360,
    closable: bool = True,
    dispose_on_close: bool = False,
)
```

## Widget classes

### ModalWindow
Lightweight wrapper around the JavaScript modal component.

Quick start::

    modal = ModalWindow(ModalConfig(title="Details"))
    modal.set_content(layout.layout)
    modal.show()

```python
ModalWindow(config: Optional[ModalConfig] = None)
```

```python
body() -> Any  # The modal's content element, for mounting a widget straight into it::
set_content(component: Any) -> None
set_title(title: str) -> None
show() -> None
hide() -> None
close() -> None
```
