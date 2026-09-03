# dhxpyt.form

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### AvatarConfig
Configuration class for the Avatar control.

```python
AvatarConfig(
    name: str = None,
    id: str = None,
    target: str = None,
    value: Dict[str, Any] = None,
    hidden: bool = False,
    disabled: bool = False,
    readOnly: bool = False,
    removeIcon: bool = True,
    circle: bool = False,
    icon: str = None,
    placeholder: str = None,
    preview: str = None,
    alt: str = None,
    size: Union[str, int] = 'medium',
    css: str = None,
    width: Union[str, int] = 'content',
    height: Union[str, int] = 'content',
    padding: Union[str, int] = '5px',
    label: str = None,
    labelWidth: Union[str, int] = None,
    labelPosition: str = 'top',
    hiddenLabel: bool = False,
    helpMessage: str = None,
    required: bool = False,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
    validation: Callable[[Any], bool] = None,
    accept: str = 'image/*',
    fieldName: str = 'file',
    autosend: bool = False,
    params: Dict[str, Any] = None,
    headerParams: Dict[str, Any] = None,
    updateFromResponse: bool = True,
)
```

### ButtonConfig
Configuration class for the Button control.

```python
ButtonConfig(
    name: str = None,
    id: str = None,
    text: str = None,
    submit: bool = False,
    url: str = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    width: Union[str, int] = 'content',
    circle: bool = False,
    color: str = 'primary',
    full: bool = False,
    icon: str = None,
    loading: bool = False,
    size: str = 'medium',
    view: str = 'flat',
)
```

### CheckboxConfig
Configuration class for the Checkbox control.

```python
CheckboxConfig(
    name: str = None,
    id: str = None,
    value: str = None,
    checked: bool = False,
    text: str = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    width: Union[str, int] = 'content',
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
    validation: Callable[[Any], bool] = None,
)
```

### CheckboxGroupConfig
Configuration class for the CheckboxGroup control.

```python
CheckboxGroupConfig(
    name: str = None,
    id: str = None,
    options: Dict[str, Any] = None,
    value: Dict[str, Union[str, bool]] = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    width: Union[str, int] = 'content',
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
    validation: Callable[[Any], bool] = None,
)
```

### ColorpickerConfig
Configuration class for the ColorPicker control.

```python
ColorpickerConfig(
    name: str = None,
    id: str = None,
    value: str = None,
    css: str = None,
    disabled: bool = False,
    editable: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    validation: Callable[[Any], bool] = None,
    width: Union[str, int] = 'content',
    customColors: bool = False,
    grayShades: bool = True,
    icon: str = None,
    mode: str = 'palette',
    palette: Any = None,
    paletteOnly: bool = False,
    pickerOnly: bool = False,
    placeholder: str = None,
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### ComboConfig
Configuration class for the Combo control.

```python
ComboConfig(
    name: str = None,
    id: str = None,
    data: List[Dict[str, Any]] = None,
    value: Union[str, int, List[Union[str, int]]] = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    validation: Callable[[Any], bool] = None,
    width: Union[str, int] = 'content',
    filter: Callable[[Any], bool] = None,
    eventHandlers: Dict[str, Callable] = None,
    itemHeight: int = 32,
    itemsCount: bool = False,
    listHeight: int = 224,
    multiselection: bool = False,
    newOptions: bool = False,
    placeholder: str = None,
    readOnly: bool = False,
    selectAllButton: bool = False,
    template: str = None,
    virtual: bool = False,
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### ContainerConfig
Configuration class for the Container control.

```python
ContainerConfig(
    name: str = None,
    id: str = None,
    html: str = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    width: Union[str, int] = 'content',
    label: str = None,
    labelWidth: Union[str, int] = None,
    labelPosition: str = 'top',
    hiddenLabel: bool = False,
    helpMessage: str = None,
)
```

### DatepickerConfig
Configuration class for the DatePicker control.

```python
DatepickerConfig(
    name: str = None,
    id: str = None,
    value: Union[str, Any] = None,
    css: str = None,
    disabled: bool = False,
    editable: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    validation: Callable[[Any], bool] = None,
    width: Union[str, int] = 'content',
    date: Union[str, Any] = None,
    dateFormat: str = '%d/%m/%y',
    disabledDates: Any = None,
    icon: str = None,
    mark: Any = None,
    mode: str = 'calendar',
    placeholder: str = None,
    thisMonthOnly: bool = False,
    timeFormat: Union[int, str] = 24,
    timePicker: bool = False,
    valueFormat: str = 'string',
    weekNumbers: bool = False,
    weekStart: str = 'sunday',
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### FieldsetConfig
Configuration class for the Fieldset control.

```python
FieldsetConfig(
    name: str = None,
    id: str = None,
    hidden: bool = False,
    disabled: bool = False,
    css: str = None,
    width: Union[str, int] = 'content',
    height: Union[str, int] = 'content',
    padding: Union[str, int] = '5px',
    label: str = None,
    labelAlignment: str = 'left',
    rows: List[Any] = None,
    cols: List[Any] = None,
    align: str = 'start',
)
```

### FormConfig
Configuration class for Form.

```python
FormConfig(
    align: str = 'start',
    cols: List[Dict[str, Any]] = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = None,
    rows: List[Dict[str, Any]] = None,
    title: str = None,
    width: Union[str, int] = 'content',
)
```

### InputConfig
Configuration class for the Input control.

```python
InputConfig(
    name: str = None,
    id: str = None,
    value: Union[str, int] = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    validation: Union[str, Callable[[Any], bool]] = None,
    width: Union[str, int] = 'content',
    autocomplete: bool = False,
    icon: str = None,
    inputType: str = 'input',
    max: Union[int, None] = None,
    maxlength: Union[int, None] = None,
    min: Union[int, None] = None,
    minlength: Union[int, None] = None,
    placeholder: str = None,
    readOnly: bool = False,
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### RadioGroupConfig
Configuration class for the RadioGroup control.

```python
RadioGroupConfig(
    name: str = None,
    id: str = None,
    options: List[RadioButtonOption] = None,
    value: str = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    width: Union[str, int] = 'content',
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### SelectConfig
Configuration class for the Select control.

```python
SelectConfig(
    name: str = None,
    id: str = None,
    options: List[SelectOption] = None,
    value: Union[str, int] = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    validation: Callable[[Any], bool] = None,
    width: Union[str, int] = 'content',
    icon: str = None,
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### SimpleVaultConfig
Configuration class for the SimpleVault control.

```python
SimpleVaultConfig(
    name: str = None,
    id: str = None,
    target: str = None,
    value: List[Dict[str, Any]] = None,
    css: str = None,
    height: Union[str, int] = 'content',
    width: Union[str, int] = 'content',
    padding: Union[str, int] = '5px',
    hidden: bool = False,
    disabled: bool = False,
    fieldName: str = 'file',
    params: Dict[str, Any] = None,
    headerParams: Dict[str, Any] = None,
    singleRequest: bool = False,
    updateFromResponse: bool = True,
    autosend: bool = False,
    accept: str = None,
    validation: Callable[[Any], bool] = None,
    required: bool = False,
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### SliderConfig
Configuration class for the Slider control.

```python
SliderConfig(
    name: str = None,
    id: str = None,
    value: Union[float, List[float]] = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    width: Union[str, int] = 'content',
    inverse: bool = False,
    majorTick: Union[int, float] = None,
    max: Union[int, float] = 100,
    min: Union[int, float] = 0,
    mode: str = 'horizontal',
    range: bool = False,
    step: Union[int, float] = 1,
    tick: Union[int, float] = None,
    tickTemplate: Callable[[Any], str] = None,
    tooltip: bool = True,
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
)
```

### SpacerConfig
Configuration class for the Spacer control.

```python
SpacerConfig(
    name: str = None,
    id: str = None,
    css: str = None,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    width: Union[str, int] = 'content',
)
```

### TextConfig
Configuration class for the Text control.

```python
TextConfig(
    name: str = None,
    id: str = None,
    value: Union[str, int] = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    width: Union[str, int] = 'content',
    inputType: str = 'text',
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### TextareaConfig
Configuration class for the Textarea control.

```python
TextareaConfig(
    name: str = None,
    id: str = None,
    value: str = None,
    css: str = None,
    disabled: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    validation: Union[str, Callable[[Any], bool]] = None,
    width: Union[str, int] = 'content',
    maxlength: int = None,
    minlength: int = None,
    placeholder: str = None,
    readOnly: bool = False,
    resizable: bool = False,
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### TimepickerConfig
Configuration class for the TimePicker control.

```python
TimepickerConfig(
    name: str = None,
    id: str = None,
    value: Union[str, int, float, Dict[str, Any], list] = None,
    css: str = None,
    disabled: bool = False,
    editable: bool = False,
    height: Union[str, int] = 'content',
    hidden: bool = False,
    padding: Union[str, int] = '5px',
    required: bool = False,
    validation: Callable[[Any], bool] = None,
    width: Union[str, int] = 'content',
    controls: bool = False,
    icon: str = None,
    placeholder: str = None,
    timeFormat: int = 24,
    valueFormat: str = 'string',
    hiddenLabel: bool = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = None,
    helpMessage: str = None,
    preMessage: str = None,
    successMessage: str = None,
    errorMessage: str = None,
)
```

### ToggleConfig
Configuration class for the Toggle control.

```python
ToggleConfig(
    name: str = None,
    id: str = None,
    hidden: bool = False,
    disabled: bool = False,
    selected: bool = False,
    full: bool = False,
    text: str = None,
    offText: str = None,
    icon: str = None,
    offIcon: str = None,
    value: Union[str, int, bool] = None,
    css: str = None,
    height: Union[str, int] = 'content',
    width: Union[str, int] = 'content',
    padding: Union[str, int] = None,
)
```

### ToggleGroupConfig
Configuration class for the ToggleGroup control.

```python
ToggleGroupConfig(
    name: str = None,
    id: str = None,
    hidden: bool = False,
    disabled: bool = False,
    full: bool = False,
    gap: int = 0,
    multiselection: bool = False,
    options: List[ToggleOption] = None,
    value: Dict[str, bool] = None,
    css: str = None,
    height: Union[str, int] = 'content',
    width: Union[str, int] = 'content',
    padding: Union[str, int] = None,
)
```

## Widget classes

### Avatar

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> Dict[str, Any]
hide() -> None
is_disabled() -> bool
is_visible() -> bool
select_file() -> None
send(params: Dict[str, Any] = None) -> None
set_properties(properties: Dict[str, Any]) -> None
set_value(value: Dict[str, Any]) -> None
show() -> None
validate(silent: bool = False, validate_value: Dict[str, Any] = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Dict[str, Any], bool], None]) -> None
on_after_show(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_validate(handler: Callable[[Dict[str, Any], bool], None]) -> None
on_before_change(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Dict[str, Any], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_upload_file(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Dict[str, Any]], None]) -> None
on_change(handler: Callable[[Dict[str, Any]], None]) -> None
on_focus(handler: Callable[[Dict[str, Any]], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
on_upload_begin(handler: Callable[[Dict[str, Any]], None]) -> None
on_upload_complete(handler: Callable[[Dict[str, Any]], None]) -> None
on_upload_fail(handler: Callable[[Dict[str, Any]], None]) -> None
on_upload_file(handler: Callable[[Dict[str, Any], Dict[str, Any]], None]) -> None
on_upload_progress(handler: Callable[[int, Dict[str, Any]], None]) -> None
```

### Button

```python
blur() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
show() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[str, bool], None]) -> None
on_after_show(handler: Callable[[str], None]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[str, bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[str], Union[bool, None]]) -> None
on_blur(handler: Callable[[str], None]) -> None
on_click(handler: Callable[[Any], None]) -> None
on_focus(handler: Callable[[str], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### Checkbox

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> Union[str, bool]
hide() -> None
is_checked() -> bool
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(checked: bool) -> None
show() -> None
validate(silent: bool = False) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, bool], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, bool]], None]) -> None
on_after_validate(handler: Callable[[Union[str, bool], bool], None]) -> None
on_before_change(handler: Callable[[Union[str, bool]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, bool], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, bool]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Union[str, bool]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Union[str, bool]], None]) -> None
on_change(handler: Callable[[Union[str, bool]], None]) -> None
on_focus(handler: Callable[[Union[str, bool]], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### CheckboxGroup

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable(id: str = None) -> None
enable(id: str = None) -> None
focus(id: str = None) -> None
get_properties(id: str = None) -> Dict[str, Any]
get_value(id: str = None) -> Union[str, bool, Dict[str, Union[str, bool]]]
hide(id: str = None) -> None
is_checked(id: str = None) -> Union[bool, Dict[str, bool]]
is_disabled(id: str = None) -> bool
is_visible(id: str = None) -> bool
set_properties(arg: Union[str, Dict[str, Any]] = None, properties: Dict[str, Any] = None) -> None
set_value(value: Dict[str, Union[str, bool]]) -> None
show(id: str = None) -> None
validate(silent: bool = False) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Dict[str, Union[str, bool]], str, bool], None]) -> None
on_after_show(handler: Callable[[Dict[str, Union[str, bool]], str], None]) -> None
on_after_validate(handler: Callable[[Dict[str, Union[str, bool]], bool], None]) -> None
on_before_change(handler: Callable[[Dict[str, Union[str, bool]]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Dict[str, Union[str, bool]], str, bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Dict[str, Union[str, bool]], str], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Dict[str, Union[str, bool]]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Dict[str, Union[str, bool]], str], None]) -> None
on_change(handler: Callable[[Dict[str, Union[str, bool]]], None]) -> None
on_focus(handler: Callable[[Dict[str, Union[str, bool]], str], None]) -> None
on_keydown(handler: Callable[[Any, str], None]) -> None
```

### Colorpicker

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> str
get_widget() -> Any
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(value: str) -> None
show() -> None
validate(silent: bool = False, validate_value: str = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[str, bool], None]) -> None
on_after_show(handler: Callable[[str], None]) -> None
on_after_validate(handler: Callable[[str, bool], None]) -> None
on_before_change(handler: Callable[[str], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[str, bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[str], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[str], Union[bool, None]]) -> None
on_blur(handler: Callable[[str], None]) -> None
on_change(handler: Callable[[str], None]) -> None
on_focus(handler: Callable[[str], None]) -> None
on_input(handler: Callable[[str], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### Combo

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> Union[str, int, List[Union[str, int]]]
get_widget() -> Any
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(ids: Union[str, int, List[Union[str, int]]]) -> None
show() -> None
validate(silent: bool = False, validate_value: Union[str, List[str]] = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, int, List[Union[str, int]]], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, int, List[Union[str, int]]]], None]) -> None
on_after_validate(handler: Callable[[Union[str, int, List[Union[str, int]]], bool], None]) -> None
on_before_change(handler: Callable[[Union[str, int, List[Union[str, int]]]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, int, List[Union[str, int]]], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, int, List[Union[str, int]]]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Union[str, int, List[Union[str, int]]]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Union[str, int, List[Union[str, int]]]], None]) -> None
on_change(handler: Callable[[Union[str, int, List[Union[str, int]]]], None]) -> None
on_focus(handler: Callable[[Union[str, int, List[Union[str, int]]]], None]) -> None
on_keydown(handler: Callable[[Any, Union[str, int, None]], None]) -> None
```

### Container

```python
attach(widget: Any) -> None
attach_html(html: str) -> None
disable() -> None
enable() -> None
get_properties() -> Dict[str, Any]
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
show() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[bool], None]) -> None
on_after_show(handler: Callable[[], None]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[], Union[bool, None]]) -> None
```

### Datepicker

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value(as_date: bool = False) -> Union[str, Any]
get_widget() -> Any
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(value: Union[str, Any]) -> None
show() -> None
validate(silent: bool = False, validate_value: Union[str, Any] = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, Any], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, Any]], None]) -> None
on_after_validate(handler: Callable[[Union[str, Any], bool], None]) -> None
on_before_change(handler: Callable[[Union[str, Any]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, Any], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, Any]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Union[str, Any]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Union[str, Any]], None]) -> None
on_change(handler: Callable[[Union[str, Any]], None]) -> None
on_focus(handler: Callable[[Union[str, Any]], None]) -> None
on_input(handler: Callable[[str], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### Fieldset

```python
destructor() -> None
disable() -> None
enable() -> None
for_each(callback: Callable[[Any, int, List[Any]], None], tree: bool = False) -> None
get_properties() -> Dict[str, Any]
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
show() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
```

### Form

```python
blur(name: str = None) -> None
clear(method: str = None) -> None
destructor() -> None
disable() -> None
enable() -> None
for_each(callback: Callable[[Any, int, List[Any]], Any]) -> None
get_item(name: str) -> Any
get_properties(name: str = None) -> Union[Dict[str, Any], Dict[str, Dict[str, Any]]]
get_value(as_form_data: bool = False) -> Dict[str, Any]
hide() -> None
is_disabled(name: str = None) -> bool
is_visible(name: str = None) -> bool
paint() -> None
send(url: str, method: str = 'POST', as_form_data: bool = False) -> Any
set_focus(name: str) -> None
set_properties(arg: Union[str, Dict[str, Dict[str, Any]]], properties: Dict[str, Any] = None) -> None
set_value(obj: Dict[str, Any]) -> None
show() -> None
validate(silent: bool = False) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[str, Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[str, Any, str], None]) -> None
on_after_send(handler: Callable[[], None]) -> None
on_after_show(handler: Callable[[str, Any, str], None]) -> None
on_after_validate(handler: Callable[[str, Any, bool], None]) -> None
on_before_change(handler: Callable[[str, Any], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[str, Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, int], Any, str], Union[bool, None]]) -> None
on_before_send(handler: Callable[[], Union[bool, None]]) -> None
on_before_show(handler: Callable[[str, Any, str], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[str, Any], Union[bool, None]]) -> None
on_blur(handler: Callable[[str, Any, str], None]) -> None
on_change(handler: Callable[[str, Any], None]) -> None
on_click(handler: Callable[[str, Any], Any]) -> None
on_focus(handler: Callable[[str, Any, str], None]) -> None
on_keydown(handler: Callable[[Any, str, str], None]) -> None
align() -> str
align(value: str) -> None
cols() -> List[Dict[str, Any]]
cols(value: List[Dict[str, Any]]) -> None
css() -> str
css(value: str) -> None
disabled() -> bool
disabled(value: bool) -> None
height() -> Union[str, int]
height(value: Union[str, int, str]) -> None
hidden() -> bool
hidden(value: bool) -> None
padding() -> Union[str, int]
padding(value: Union[str, int]) -> None
rows() -> List[Dict[str, Any]]
rows(value: List[Dict[str, Any]]) -> None
title() -> str
title(value: str) -> None
width() -> Union[str, int]
width(value: Union[str, int, str]) -> None
```

### Input

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> Union[str, int]
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(value: Union[str, int]) -> None
show() -> None
validate(silent: bool = False, validate_value: Union[str, int] = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, int], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, int]], None]) -> None
on_after_validate(handler: Callable[[Union[str, int], bool], None]) -> None
on_before_change(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, int], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Union[str, int]], None]) -> None
on_change(handler: Callable[[Union[str, int]], None]) -> None
on_focus(handler: Callable[[Union[str, int]], None]) -> None
on_input(handler: Callable[[Union[str, int]], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### RadioButtonOption
Represents an individual radio button option in the RadioGroup.

```python
to_dict() -> Dict[str, Any]
```

### RadioGroup

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable(id: str = None) -> None
enable(id: str = None) -> None
focus(id: str = None) -> None
get_properties(id: str = None) -> Dict[str, Any]
get_value() -> str
hide(id: str = None) -> None
is_disabled(id: str = None) -> bool
is_visible(id: str = None) -> bool
set_properties(arg: Union[str, Dict[str, Any]], props: Dict[str, Any] = None) -> None
set_value(value: str) -> None
show(id: str = None) -> None
validate(silent: bool = False) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[str, str, bool], None]) -> None
on_after_show(handler: Callable[[str, str], None]) -> None
on_after_validate(handler: Callable[[str, bool], None]) -> None
on_before_change(handler: Callable[[str], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[str, str, bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[str, str], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[str], Union[bool, None]]) -> None
on_blur(handler: Callable[[str, str], None]) -> None
on_change(handler: Callable[[str], None]) -> None
on_focus(handler: Callable[[str, str], None]) -> None
on_keydown(handler: Callable[[Any, str], None]) -> None
```

### Select

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable(value: Union[str, int] = None) -> None
enable(value: Union[str, int] = None) -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_options() -> List[Dict[str, Any]]
get_value() -> Union[str, int]
hide() -> None
is_disabled(value: Union[str, int] = None) -> bool
is_visible() -> bool
set_options(options: List[Dict[str, Any]]) -> None
set_properties(properties: Dict[str, Any]) -> None
set_value(value: Union[str, int]) -> None
show() -> None
validate(silent: bool = False) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, int], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, int]], None]) -> None
on_after_validate(handler: Callable[[Union[str, int], bool], None]) -> None
on_before_change(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_before_change_options(handler: Callable[[List[Dict[str, Any]]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, int], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Union[str, int]], None]) -> None
on_change(handler: Callable[[Union[str, int]], None]) -> None
on_change_options(handler: Callable[[List[Dict[str, Any]]], None]) -> None
on_focus(handler: Callable[[Union[str, int]], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### SelectOption
Represents an individual option in the Select control.

```python
to_dict() -> Dict[str, Any]
```

### SimpleVault

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> List[Dict[str, Any]]
hide() -> None
is_disabled() -> bool
is_visible() -> bool
select_file() -> None
send(params: Dict[str, Any] = None) -> None
set_properties(properties: Dict[str, Any]) -> None
set_value(value: List[Dict[str, Any]]) -> None
show() -> None
validate(silent: bool = False, validate_value: List[Dict[str, Any]] = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_add(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[List[Dict[str, Any]], bool], None]) -> None
on_after_remove(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_show(handler: Callable[[List[Dict[str, Any]]], None]) -> None
on_after_validate(handler: Callable[[List[Dict[str, Any]], bool], None]) -> None
on_before_add(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_change(handler: Callable[[List[Dict[str, Any]], Dict[str, Any]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[List[Dict[str, Any]], bool], Union[bool, None]]) -> None
on_before_remove(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_show(handler: Callable[[List[Dict[str, Any]]], Union[bool, None]]) -> None
on_before_upload_file(handler: Callable[[Dict[str, Any], List[Dict[str, Any]]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[List[Dict[str, Any]]], Union[bool, None]]) -> None
on_change(handler: Callable[[List[Dict[str, Any]]], None]) -> None
on_upload_begin(handler: Callable[[List[Dict[str, Any]], List[Dict[str, Any]]], None]) -> None
on_upload_complete(handler: Callable[[List[Dict[str, Any]], List[Dict[str, Any]]], None]) -> None
on_upload_fail(handler: Callable[[Dict[str, Any], List[Dict[str, Any]]], None]) -> None
on_upload_file(handler: Callable[[Dict[str, Any], List[Dict[str, Any]], Dict[str, Any]], None]) -> None
on_upload_progress(handler: Callable[[int, List[Dict[str, Any]]], None]) -> None
```

### Slider

```python
blur() -> None
clear() -> None
destructor() -> None
disable() -> None
enable() -> None
focus(extra: bool = False) -> None
get_properties() -> Dict[str, Any]
get_value() -> List[float]
get_widget() -> Any
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(value: Union[float, List[float]]) -> None
show() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[List[float], bool], None]) -> None
on_after_show(handler: Callable[[List[float]], None]) -> None
on_before_change(handler: Callable[[List[float]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[List[float], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[List[float]], Union[bool, None]]) -> None
on_blur(handler: Callable[[List[float]], None]) -> None
on_change(handler: Callable[[List[float]], None]) -> None
on_focus(handler: Callable[[List[float]], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### Spacer

```python
destructor() -> None
get_properties() -> Dict[str, Any]
hide() -> None
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
show() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[bool], None]) -> None
on_after_show(handler: Callable[[], None]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[], Union[bool, None]]) -> None
```

### Text

```python
clear() -> None
destructor() -> None
disable() -> None
enable() -> None
get_properties() -> Dict[str, Any]
get_value() -> Union[str, int]
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(value: Union[str, int]) -> None
show() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, int], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, int]], None]) -> None
on_after_validate(handler: Callable[[Union[str, int], bool], None]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, int], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Union[str, int]], Union[bool, None]]) -> None
on_change(handler: Callable[[Union[str, int]], None]) -> None
```

### Textarea

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> str
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(value: str) -> None
show() -> None
validate(silent: bool = False, validate_value: str = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[str, bool], None]) -> None
on_after_show(handler: Callable[[str], None]) -> None
on_after_validate(handler: Callable[[str, bool], None]) -> None
on_before_change(handler: Callable[[str], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[str, bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[str], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[str], Union[bool, None]]) -> None
on_blur(handler: Callable[[str], None]) -> None
on_change(handler: Callable[[str], None]) -> None
on_focus(handler: Callable[[str], None]) -> None
on_input(handler: Callable[[str], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### Timepicker

```python
blur() -> None
clear() -> None
clear_validate() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value(as_object: bool = False) -> Union[str, Dict[str, Any]]
get_widget() -> Any
hide() -> None
is_disabled() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(value: Union[str, int, float, Dict[str, Any], list]) -> None
show() -> None
validate(silent: bool = False, validate_value: str = None) -> bool
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, Dict[str, Any]], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, Dict[str, Any]]], None]) -> None
on_after_validate(handler: Callable[[Union[str, Dict[str, Any]], bool], None]) -> None
on_before_change(handler: Callable[[Union[str, Dict[str, Any]]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, Dict[str, Any]], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, Dict[str, Any]]], Union[bool, None]]) -> None
on_before_validate(handler: Callable[[Union[str, Dict[str, Any]]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Union[str, Dict[str, Any]]], None]) -> None
on_change(handler: Callable[[Union[str, Dict[str, Any]]], None]) -> None
on_focus(handler: Callable[[Union[str, Dict[str, Any]]], None]) -> None
on_input(handler: Callable[[str], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### Toggle

```python
blur() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_properties() -> Dict[str, Any]
get_value() -> Union[str, int, bool]
hide() -> None
is_disabled() -> bool
is_selected() -> bool
is_visible() -> bool
set_properties(properties: Dict[str, Any]) -> None
set_value(selected: bool) -> None
show() -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any]], None]) -> None
on_after_hide(handler: Callable[[Union[str, int, bool], bool], None]) -> None
on_after_show(handler: Callable[[Union[str, int, bool]], None]) -> None
on_before_change(handler: Callable[[Union[str, int, bool]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, int, bool], bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Union[str, int, bool]], Union[bool, None]]) -> None
on_blur(handler: Callable[[Union[str, int, bool]], None]) -> None
on_change(handler: Callable[[Union[str, int, bool]], None]) -> None
on_focus(handler: Callable[[Union[str, int, bool]], None]) -> None
on_keydown(handler: Callable[[Any], None]) -> None
```

### ToggleGroup

```python
blur() -> None
destructor() -> None
disable(id: str = None) -> None
enable(id: str = None) -> None
focus(id: str = None) -> None
get_properties(id: str = None) -> Dict[str, Any]
get_value(id: str = None) -> Union[str, int, bool, Dict[str, Union[str, int, bool]]]
hide(id: str = None) -> None
is_disabled(id: str = None) -> bool
is_selected(id: str = None) -> Union[bool, Dict[str, bool]]
is_visible(id: str = None) -> bool
set_properties(config: Dict[str, Any], id: str = None) -> None
set_value(value: Dict[str, bool]) -> None
show(id: str = None) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_change_properties(handler: Callable[[Dict[str, Any], str], None]) -> None
on_after_hide(handler: Callable[[Dict[str, Any], str, bool], None]) -> None
on_after_show(handler: Callable[[Dict[str, Any], str], None]) -> None
on_before_change(handler: Callable[[Dict[str, Any]], Union[bool, None]]) -> None
on_before_change_properties(handler: Callable[[Dict[str, Any], str], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Dict[str, Any], str, bool], Union[bool, None]]) -> None
on_before_show(handler: Callable[[Dict[str, Any], str], Union[bool, None]]) -> None
on_blur(handler: Callable[[Dict[str, Any], str], None]) -> None
on_change(handler: Callable[[Dict[str, Any]], None]) -> None
on_focus(handler: Callable[[Dict[str, Any], str], None]) -> None
on_keydown(handler: Callable[[Any, str], None]) -> None
```

### ToggleOption
Represents an individual toggle option in the ToggleGroup.

```python
to_dict() -> Dict[str, Any]
```
