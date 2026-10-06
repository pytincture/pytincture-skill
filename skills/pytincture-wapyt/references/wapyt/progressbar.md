# wapyt.progressbar

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### ProgressBarConfig
Initial value and look of a :class:`ProgressBar`.

Args:
    value / max: Progress as ``value`` out of ``max`` (default 100); values
        are clamped to ``0..max``.
    label: Text before the bar, such as a file name.
    show_value: Show the percentage when no ``value_text`` is given.
    value_text: Replaces the percentage readout, e.g. ``"42%  1.2 MB"``.
    state: ``active`` (blue), ``done`` (green), ``error`` (red) or
        ``paused`` (amber).
    indeterminate: Total unknown: an animated bar and no percentage.
    compact: One line -- label, bar, value -- for rows, queues and tiles.
    label_width / value_width: Fixed widths (px or any CSS size) for the
        label and value, so the bars of a stacked list line up.
    extra: Additional properties forwarded to JS verbatim.

```python
ProgressBarConfig(
    value: Number = 0,
    max: Number = 100,
    label: Optional[str] = None,
    show_value: bool = True,
    value_text: Optional[str] = None,
    state: str = 'active',
    indeterminate: bool = False,
    compact: bool = False,
    label_width: Optional[Union[int, str]] = None,
    value_width: Optional[Union[int, str]] = None,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

## Widget classes

### ProgressBar
A progress bar.

Quick start::

    bar = ProgressBar(ProgressBarConfig(label="report.pdf", compact=True),
                      container=row_element)
    bar.set_value(seen, total, text=f"{seen * 100 // total}%  {format_size(seen)}")
    bar.set_state("done")

Updates only touch the bar's width and two text nodes, so calling
``set_value`` from a transfer's progress callback several times a second
is fine. The total unknown? ``set_indeterminate(True)`` and pass the bytes
moved as ``text``. For static HTML (a dashboard tile built as a string)
use :func:`progress_html` instead.

```python
ProgressBar(config: Optional[ProgressBarConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
set_value(value: Number, max: Optional[Number] = None, *, text: Optional[str] = None) -> None  # Move the bar. ``max`` changes the total; ``text`` replaces the percentage readout (``""`` returns to the percentage).
set_label(label: Optional[str]) -> None
set_state(state: str) -> None  # ``active``, ``done``, ``error`` or ``paused``.
set_indeterminate(indeterminate: bool = True) -> None
destroy() -> None
```

## Functions

```python
progress_html(value: Number, max: Number = 100, *, label: Optional[str] = None, text: Optional[str] = None, state: str = 'active', compact: bool = True, show_value: bool = True) -> str
    # Static progress-bar markup for UIs built from HTML strings (dashboard tiles, ``attach_html``). Same classes and look as :class:`ProgressBar`, no JS; every string is HTML-escaped. Pass ``value`` as a fraction with ``max=1``, or as a count with its ``max``.
```
