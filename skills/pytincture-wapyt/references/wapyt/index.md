# wapyt 0.1.0 API reference

One page per module, generated from source. Load only the module you need.

## Modules

- [`cardpanel`](cardpanel.md) — 2 config, 1 widget
- [`chat`](chat.md) — 3 config, 2 widget
- [`datatable`](datatable.md) — 3 config, 1 widget
- [`filetransfer`](filetransfer.md) — 3 config, 0 widget, 14 function
- [`form`](form.md) — 3 config, 1 widget
- [`layout`](layout.md) — 2 config, 3 widget
- [`message`](message.md) — 0 config, 0 widget, 8 function
- [`modal`](modal.md) — 1 config, 1 widget
- [`resourceboard`](resourceboard.md) — 2 config, 1 widget
- [`sidebar`](sidebar.md) — 2 config, 1 widget
- [`tabwidget`](tabwidget.md) — 2 config, 1 widget
- [`terminal`](terminal.md) — 2 config, 1 widget
- [`toolbar`](toolbar.md) — 5 config, 1 widget
- [`tree`](tree.md) — 3 config, 1 widget

## `add_*` helpers

Prefer these over constructing a widget directly: they mount the widget
into a container that already exists. The `id` is an **existing cell id**
in the layout/tabbar you are calling, not a new name.

```python
layout.Layout.add_cardpanel(id: str = 'mainwindow', cardpanel_config: Optional['CardPanelConfig'] = None) -> 'CardPanel'
layout.Layout.add_chat(id: str = 'mainwindow', chat_config: Optional['ChatConfig'] = None) -> 'Chat'
layout.Layout.add_datatable(id: str = 'mainwindow', datatable_config: Optional['DataTableConfig'] = None) -> 'DataTable'
layout.Layout.add_form(id: str = 'mainwindow', form_config: Optional['FormConfig'] = None) -> 'Form'
layout.Layout.add_layout(id: str = 'mainwindow', layout_config: Optional[LayoutConfig] = None) -> TLayout
layout.Layout.add_resourceboard(id: str = 'mainwindow', resourceboard_config: Optional['ResourceBoardConfig'] = None) -> 'ResourceBoard'
layout.Layout.add_sidebar(id: str = 'mainwindow', sidebar_config: Optional['SidebarConfig'] = None) -> 'Sidebar'
layout.Layout.add_tabwidget(id: str = 'mainwindow', tab_config: Optional['TabWidgetConfig'] = None) -> 'TabWidget'
layout.Layout.add_terminal(id: str = 'mainwindow', terminal_config: Optional['TerminalConfig'] = None) -> 'Terminal'
layout.Layout.add_toolbar(id: str = 'mainwindow_header', toolbar_config: Optional['ToolbarConfig'] = None) -> 'Toolbar'
layout.Layout.add_tree(id: str = 'mainwindow', tree_config: Optional['TreeConfig'] = None) -> 'Tree'
```
