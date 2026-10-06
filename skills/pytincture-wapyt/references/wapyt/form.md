# wapyt.form

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### FieldConfig
One form control.

Args:
    id: Key this field contributes to the submitted values dict.
    label: Visible label text.
    type: ``text`` · ``password`` · ``email`` · ``number`` · ``url``
        · ``textarea`` · ``select`` · ``checkbox`` · ``hidden``.
    value: Initial value. For ``checkbox`` it is coerced to a bool.
    placeholder: Placeholder text for textual controls.
    help: Hint rendered under the control.
    required: Fails validation when empty.
    min_length: Minimum string length once non-empty.
    pattern: JavaScript regular expression source the value must match.
    matches: Another field's id whose value this one must equal — for
        "confirm password" pairs.
    options: Choices for ``select``; strings or :class:`SelectOption`.
    rows: Row count for ``textarea``.
    min / max / step: Bounds for ``number``.
    span: Column span when the form is laid out in more than one column.
    disabled / readonly: Control state.
    autocomplete: Forwarded to the control's ``autocomplete`` attribute.
    required_message / min_length_message / pattern_message /
    matches_message: Override the default validation copy.

Client-side validation is a convenience, never a control: the BFF revalidates.

```python
FieldConfig(
    id: str,
    label: Optional[str] = None,
    type: str = 'text',
    value: Any = None,
    placeholder: Optional[str] = None,
    help: Optional[str] = None,
    required: bool = False,
    min_length: Optional[int] = None,
    pattern: Optional[str] = None,
    matches: Optional[str] = None,
    options: Optional[List[Union[str, SelectOption]]] = None,
    rows: Optional[int] = None,
    min: Optional[Union[int, float]] = None,
    max: Optional[Union[int, float]] = None,
    step: Optional[Union[int, float]] = None,
    span: Optional[int] = None,
    disabled: bool = False,
    readonly: bool = False,
    autocomplete: Optional[str] = None,
    required_message: Optional[str] = None,
    min_length_message: Optional[str] = None,
    pattern_message: Optional[str] = None,
    matches_message: Optional[str] = None,
)
```

### FormConfig
Layout and chrome for :class:`Form`.

Args:
    fields: Controls in render order.
    submit_text: Label for the submit button; ``None`` hides it.
    cancel_text: Label for the cancel button; ``None`` hides it.
    columns: Grid column count (1 stacks the fields).
    busy: Start with the buttons disabled.
    autocomplete: Form-level ``autocomplete`` attribute.
    extra: Additional properties forwarded to JS verbatim.

```python
FormConfig(
    fields: List[FieldConfig] = field(default_factory=list),
    submit_text: Optional[str] = 'Save',
    cancel_text: Optional[str] = None,
    columns: int = 1,
    busy: bool = False,
    autocomplete: str = 'off',
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### SelectOption
One entry in a ``select`` field.

```python
SelectOption(
    value: str,
    label: Optional[str] = None,
)
```

## Widget classes

### Form
A set of labelled controls with a submit action.

Quick start::

    form = Form(
        FormConfig(
            fields=[
                FieldConfig(id="host", label="Host", required=True),
                FieldConfig(id="port", label="Port", type="number", value=22),
            ],
            submit_text="Connect",
            cancel_text="Cancel",
        ),
        container=modal.body,
    )
    form.on_submit(lambda values: print(values))

``on_submit`` only fires once client-side validation passes. That validation
is a convenience for the person typing, never a security control — the BFF
revalidates everything it is sent.

```python
Form(config: Optional[FormConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_submit(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fires with the values dict once validation passes.
on_cancel(handler: Callable[[Dict[str, Any]], Any]) -> None
on_change(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fires per edit with ``{"id": ..., "value": ...}``.
on_invalid(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fires with ``{"errors": {...}}`` when a submit is rejected locally.
get_values() -> Dict[str, Any]
set_values(values: Dict[str, Any]) -> None
set_field_options(field_id: str, options: List[Union[str, SelectOption]]) -> None
show_field(field_id: str) -> None
hide_field(field_id: str) -> None
set_field_disabled(field_id: str, disabled: bool = True) -> None
set_busy(busy: bool = True) -> None  # Disable the buttons while an async submit is in flight.
focus_first() -> None
submit() -> None  # Trigger validation and, if it passes, the submit event.
set_error(field_id: Optional[str], message: str) -> None  # Show an error under a field, or form-wide when ``field_id`` is None.
set_errors(errors: Dict[str, str]) -> None
clear_errors() -> None
validate() -> Dict[str, str]
```
