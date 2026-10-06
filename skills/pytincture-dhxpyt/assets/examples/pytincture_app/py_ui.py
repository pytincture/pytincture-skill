"""
Example application using MainWindow subclass and layout management
with a collapsible sidebar, content area, a Tabbar containing a grid, calendar, and form.
"""
import asyncio
import json

import js

import widget  # declares __widgetset__/__version__ for the backend
from dhxpyt.layout import MainWindow
from dhxpyt.chart import BarChartConfig
from dhxpyt.toolbar import ButtonConfig, ToolbarConfig, SeparatorConfig as ToolbarSeparatorConfig
from dhxpyt.sidebar import NavItemConfig, SeparatorConfig as SidebarSeparatorConfig, SpacerConfig, SidebarConfig
from dhxpyt.grid import GridConfig, GridColumnConfig  # Grid and GridColumnConfig
from dhxpyt.calendar import CalendarConfig
from dhxpyt.form import FormConfig, InputConfig, DatepickerConfig  # Importing form-related classes
from dhxpyt.layout import LayoutConfig, CellConfig  # Direct imports
from dhxpyt.tabbar import TabbarConfig, TabConfig  # Tabbar-related imports
from py_ui_data import py_ui_data  # server-side data, reached over the BFF


class py_ui(MainWindow):
    # Do NOT define __init__ to call load_ui(): dhxpyt's LoadUICaller metaclass
    # calls load_ui() automatically after construction. Calling it here as well
    # builds the entire UI twice.
    def load_ui(self):
        self.set_theme("dark")
        self.sidebar_collapsed = False  # Track the sidebar state
        # Add a toolbar to the pre-existing 'mainwindow_header'
        toolbar_buttons = [
            ButtonConfig(id="file", value="File", icon="mdi mdi-car-brake-hold"),
            ButtonConfig(id="edit", value="Edit", icon="mdi mdi-pencil"),
            ToolbarSeparatorConfig(id="sep1"),
            ButtonConfig(id="help", value="Help", icon="mdi mdi-help-circle")
        ]
        toolbar_config = ToolbarConfig(data=toolbar_buttons)
        self.toolbar = self.add_toolbar(id="mainwindow_header", toolbar_config=toolbar_config)

        # Create a layout for the body (main content area) with two columns: sidebar and main content
        body_layout_config = LayoutConfig(
            type="line",
            cols=[
                CellConfig(id="mainwindow_sidebar", width="auto"),  # Sidebar column
                CellConfig(id="mainwindow_content", width="100%")  # Content column
            ]
        )

        # Add the body layout to the pre-existing 'mainwindow' cell and capture the layout instance
        self.mw_body_layout = self.add_layout(id="mainwindow", layout_config=body_layout_config)

        # Sidebar items configuration
        sidebar_items = [
            NavItemConfig(id="hamburger", icon="mdi mdi-menu"),  # Hamburger button for collapsing/expanding
            NavItemConfig(id="dashboard", value="Dashboard", icon="mdi mdi-view-dashboard"),
            NavItemConfig(id="statistics", value="Statistics", icon="mdi mdi-chart-line"),
            NavItemConfig(id="reports", value="Reports", icon="mdi mdi-file-chart"),
            SidebarSeparatorConfig(),  # Separator
            NavItemConfig(id="posts", value="Posts", icon="mdi mdi-square-edit-outline", items=[
                NavItemConfig(id="addPost", value="New Post", icon="mdi mdi-plus"),
                NavItemConfig(id="allPost", value="Posts", icon="mdi mdi-view-list"),
                NavItemConfig(id="categoryPost", value="Category", icon="mdi mdi-tag")
            ]),
            NavItemConfig(id="pages", value="Pages", icon="mdi mdi-file-outline", items=[
                NavItemConfig(id="addPage", value="New Page", icon="mdi mdi-plus"),
                NavItemConfig(id="allPage", value="Pages", icon="mdi mdi-view-list"),
                NavItemConfig(id="categoryPages", value="Category", icon="mdi mdi-tag")
            ]),
            NavItemConfig(id="messages", value="Messages", icon="mdi mdi-email-mark-as-unread", count=18),
            NavItemConfig(id="media", value="Media", icon="mdi mdi-folder-multiple-image"),
            NavItemConfig(id="links", value="Links", icon="mdi mdi-link"),
            NavItemConfig(id="comments", value="Comments", icon="mdi mdi-comment-multiple-outline", count="118", countColor="primary", items=[
                NavItemConfig(id="myComments", value="My Comments", icon="mdi mdi-account", count=15),
                NavItemConfig(id="allComments", value="All Comments", icon="mdi mdi-comment-multiple-outline", count=103, countColor="primary")
            ]),
            SpacerConfig(),  # Spacer
            NavItemConfig(id="notification", value="Notification", icon="mdi mdi-bell", count=25, countColor="primary"),
            NavItemConfig(id="configuration", value="Configuration", icon="mdi mdi-settings", items=[
                NavItemConfig(id="myAccount", value="My Account", icon="mdi mdi-account-settings"),
                NavItemConfig(id="general", value="General Configuration", icon="mdi mdi-tune")
            ])
        ]

        # Sidebar configuration with width and the items
        sidebar_config = SidebarConfig(data=sidebar_items)

        # Add the sidebar to the layout
        self.sidebar = self.mw_body_layout.add_sidebar(id="mainwindow_sidebar", sidebar_config=sidebar_config)

        # Add event to the hamburger button to toggle the sidebar
        self.sidebar.on_click(self.handle_toolbar_click)

        # Now, create a new layout within the 'mainwindow_content' cell with two rows:
        # One for the HTML content and another for the tabbed content area.
        content_layout_config = LayoutConfig(
            type="line",
            rows=[
                CellConfig(id="content_message", height="auto"),  # Row for the HTML message
                CellConfig(id="content_tabbar", height="100%")      # Row for the tabbed area
            ]
        )

        # Add the new layout to 'mainwindow_content'
        self.content_layout = self.mw_body_layout.add_layout(id="mainwindow_content", layout_config=content_layout_config)

        # Add the HTML content to the top row (content_message)
        self.content_layout.attach_html(id="content_message", html="<h1 style='margin-left: 10px;'>Book Details and Ratings</h1>")

        # Tabbar configuration with four tabs: Grid, Book Ratings Chart, Form, Calendar
        tabbar_config = TabbarConfig(
            views=[
                TabConfig(id="tab1", tab="Grid View"),
                TabConfig(id="tab2", tab="Book Ratings Chart"),
                TabConfig(id="tab3", tab="Form View"),
                TabConfig(id="tab4", tab="Calendar View")
            ],
            activeTab="tab1"  # Set Grid View as the active tab by default
        )

        # Add the tabbar to the content_tabbar row
        self.tabbar = self.content_layout.add_tabbar(id="content_tabbar", tabbar_config=tabbar_config)

        # Grid columns configuration using GridColumnConfig
        grid_columns = [
            GridColumnConfig(width=300, id="title", header=[{"text": "TITle"}]),
            GridColumnConfig(width=200, id="authors", header=[{"text": "Authors"}]),
            GridColumnConfig(width=80, id="average_rating", header=[{"text": "Rating"}]),
            GridColumnConfig(width=150, id="publication_date", header=[{"text": "Publication date"}]),
            GridColumnConfig(width=150, id="isbn13", header=[{"text": "ISBN"}]),
            GridColumnConfig(width=90, id="language_code", header=[{"text": "Language"}]),
            GridColumnConfig(width=90, id="num_pages", header=[{"text": "Pages"}]),
            GridColumnConfig(width=120, id="ratings_count", header=[{"text": "Rating count"}]),
            GridColumnConfig(width=100, id="text_reviews_count", header=[{"text": "Text reviews count"}]),
            GridColumnConfig(width=200, id="publisher", header=[{"text": "Publisher"}])
        ]

        # Grid configuration with columns. The rows arrive from the BFF after
        # load_ui() returns, so no data= here.
        grid_config = GridConfig(columns=grid_columns)

        # Attach the grid to the first tab (tab1) using tabbar.add_grid
        self.book_grid = self.tabbar.add_grid(id="tab1", grid_config=grid_config)

        # load_ui() is synchronous, so schedule the BFF call instead of
        # blocking on it. This fills the grid (tab1) and builds the chart
        # (tab2) once the dataset arrives.
        self.book_chart = None
        asyncio.ensure_future(self._load_dataset())

        # Calendar configuration
        calendar_config = CalendarConfig(width="50%")
        self.cal = self.tabbar.add_calendar(id="tab4", calendar_config=calendar_config)

        # Add a form for the book details in tab3
        form_fields = [
            InputConfig(id="title", label="Title"),
            InputConfig(id="authors", label="Authors"),
            InputConfig(id="average_rating", label="Rating"),
            DatepickerConfig(id="publication_date", label="Publication Date"),
            InputConfig(id="isbn13", label="ISBN"),
            InputConfig(id="language_code", label="Language"),
            InputConfig(id="num_pages", label="Pages"),
            InputConfig(id="ratings_count", label="Rating Count"),
            InputConfig(id="text_reviews_count", label="Text Reviews Count"),
            InputConfig(id="publisher", label="Publisher")
        ]

        form_config = FormConfig(cols=form_fields)

        # Attach the form to the third tab (tab3) using tabbar.add_form
        self.book_form = self.tabbar.add_form(id="tab3", form_config=form_config)

    async def _load_dataset(self):
        """Fetch the dataset over the BFF and populate tab1 and tab2."""
        # asyncio.ensure_future() swallows exceptions from this coroutine, so
        # report them explicitly rather than failing silently.
        try:
            # The generated browser stub exposes both dataset() -- a blocking
            # XHR, deprecated through 1.x -- and dataset_async(). Only the
            # latter is awaitable, and it is what new browser code should use.
            raw = await py_ui_data().dataset_async()
            data = json.loads(raw) if isinstance(raw, str) else raw
        except Exception:
            import traceback
            js.console.error("dataset load failed: " + traceback.format_exc())
            return

        # dhxpyt's Grid wrapper has no data API; reach the underlying widget.
        self.book_grid.grid.data.parse(js.JSON.parse(json.dumps(data)))

        # Ten most-rated books, with titles trimmed so the axis stays legible.
        top_rated = sorted(
            data, key=lambda book: book.get("ratings_count") or 0, reverse=True
        )[:10]
        chart_rows = [
            {
                "title": (book.get("title") or "")[:24],
                "average_rating": book.get("average_rating") or 0,
            }
            for book in top_rated
        ]

        # Chart.__init__ hands config.to_dict() to dhx through JSON, so data=
        # is delivered correctly; building the widget here keeps one code path.
        self.book_chart = self.tabbar.add_chart(
            id="tab2",
            chart_config=BarChartConfig(
                series=[
                    {"id": "rating", "value": "average_rating", "fill": "#4a90d9"}
                ],
                scales={"bottom": {"text": "title"}, "left": {"max": 5}},
                data=chart_rows,
            ),
        )

    def handle_toolbar_click(self, id, event):
        """Handle toolbar button clicks."""
        if id == "hamburger":
            self.toggle_sidebar()

    def toggle_sidebar(self, event=None):
        """Toggle the sidebar collapse/expand state."""
        if self.sidebar_collapsed:
            # Expand the sidebar (show text)
            self.sidebar.toggle()
            self.sidebar_collapsed = False
        else:
            # Collapse the sidebar (hide text, show only icons)
            self.sidebar.toggle()
            self.sidebar_collapsed = True

