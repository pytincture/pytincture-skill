# dhxpyt 0.9.18 API reference

One page per module, generated from source. Load only the module you need.

## Modules

- [`calendar`](calendar.md) — 2 config, 1 widget
- [`cardflow`](cardflow.md) — 2 config, 1 widget
- [`cardpanel`](cardpanel.md) — 2 config, 1 widget
- [`chart`](chart.md) — 15 config, 1 widget
- [`chat`](chat.md) — 3 config, 1 widget
- [`colorpicker`](colorpicker.md) — 1 config, 1 widget
- [`combobox`](combobox.md) — 1 config, 1 widget
- [`form`](form.md) — 21 config, 24 widget
- [`gpu`](gpu.md) — 0 config, 0 widget
- [`grid`](grid.md) — 2 config, 1 widget
- [`kanban`](kanban.md) — 4 config, 1 widget
- [`layout`](layout.md) — 2 config, 3 widget
- [`listbox`](listbox.md) — 1 config, 1 widget
- [`menu`](menu.md) — 2 config, 1 widget
- [`message`](message.md) — 1 config, 1 widget
- [`pagination`](pagination.md) — 1 config, 1 widget
- [`popup`](popup.md) — 2 config, 1 widget
- [`ribbon`](ribbon.md) — 13 config, 1 widget
- [`sidebar`](sidebar.md) — 8 config, 1 widget
- [`slider`](slider.md) — 1 config, 1 widget
- [`tabbar`](tabbar.md) — 2 config, 1 widget
- [`theme`](theme.md) — 0 config, 0 widget
- [`timepicker`](timepicker.md) — 1 config, 1 widget
- [`toolbar`](toolbar.md) — 11 config, 1 widget
- [`tree`](tree.md) — 2 config, 1 widget
- [`window`](window.md) — 1 config, 1 widget

## `add_*` helpers

Prefer these over constructing a widget directly: they mount the widget
into a container that already exists. The `id` is an **existing cell id**
in the layout/tabbar you are calling, not a new name.

```python
cardflow.CardFlow.add_layout(id: str = 'mainwindow', layout_config = None)
layout.Layout.add_calendar(id: str, calendar_config: CalendarConfig = None) -> Any
layout.Layout.add_cardflow(id: str, cardflow_config: CardFlowConfig = None) -> Any
layout.Layout.add_cardpanel(id: str, cardpanel_config: CardPanelConfig = None) -> CardPanel
layout.Layout.add_chart(id: str, chart_config: ChartConfig = None) -> Any
layout.Layout.add_chat(id: str, chat_config: ChatConfig = None) -> Chat
layout.Layout.add_form(id: str, form_config: FormConfig = None) -> Form
layout.Layout.add_grid(id: str = 'mainwindow', grid_config: GridConfig = None) -> Grid
layout.Layout.add_kanban(id: str = 'mainwindow', kanban_config: KanbanConfig = None, kanban_callback: callable = None) -> None
layout.Layout.add_layout(id: str = 'mainwindow', layout_config: LayoutConfig = None) -> TLayout
layout.Layout.add_listbox(id: str, listbox_config: ListboxConfig = None) -> Any
layout.Layout.add_menu(id: str = 'mainwindow_header', menu_config: MenuConfig = None) -> Menu
layout.Layout.add_pagination(id: str, pagination_config: PaginationConfig = None) -> Any
layout.Layout.add_ribbon(id: str, ribbon_config: RibbonConfig = None) -> Any
layout.Layout.add_sidebar(id: str, sidebar_config: SidebarConfig = None) -> Sidebar
layout.Layout.add_tabbar(id: str, tabbar_config: TabbarConfig = None) -> Any
layout.Layout.add_timepicker(id: str, timepicker_config: TimepickerConfig = None) -> Any
layout.Layout.add_toolbar(id: str = 'mainwindow', toolbar_config: ToolbarConfig = None) -> Toolbar
layout.Layout.add_tree(id: str, tree_config: TreeConfig = None) -> Any
tabbar.Tabbar.add_calendar(id: str, calendar_config: CalendarConfig = None) -> Any
tabbar.Tabbar.add_cardflow(id: str, cardflow_config: CardFlowConfig = None) -> Any
tabbar.Tabbar.add_cardpanel(id: str, cardpanel_config: CardPanelConfig = None) -> CardPanel
tabbar.Tabbar.add_chart(id: str, chart_config: ChartConfig = None) -> Any
tabbar.Tabbar.add_form(id: str, form_config: FormConfig = None) -> Form
tabbar.Tabbar.add_grid(id: str = 'mainwindow', grid_config: GridConfig = None) -> Grid
tabbar.Tabbar.add_kanban(id: str = 'mainwindow', kanban_config: KanbanConfig = None, kanban_callback: callable = None) -> None
tabbar.Tabbar.add_listbox(id: str, listbox_config: ListboxConfig = None) -> Any
tabbar.Tabbar.add_menu(id: str = 'mainwindow_header', menu_config: MenuConfig = None) -> Menu
tabbar.Tabbar.add_pagination(id: str, pagination_config: PaginationConfig = None) -> Any
tabbar.Tabbar.add_ribbon(id: str, ribbon_config: RibbonConfig = None) -> Any
tabbar.Tabbar.add_sidebar(id: str, sidebar_config: SidebarConfig = None) -> Sidebar
tabbar.Tabbar.add_tabbar(id: str, tabbar_config: TabbarConfig = None) -> Any
tabbar.Tabbar.add_timepicker(id: str, timepicker_config: TimepickerConfig = None) -> Any
tabbar.Tabbar.add_toolbar(id: str = 'mainwindow', toolbar_config: ToolbarConfig = None) -> Toolbar
tabbar.Tabbar.add_tree(id: str, tree_config: TreeConfig = None) -> Any
```
