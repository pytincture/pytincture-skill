"""
Minimal dhxpyt UI: layout + toolbar + grid.

Note the entrypoint pattern: subclass MainWindow and implement `load_ui()`.
Do NOT override `__init__` to call `load_ui()` yourself -- dhxpyt's
`LoadUICaller` metaclass already calls it once the instance is constructed
(see dhxpyt/layout/layout.py). Calling it again builds the whole UI twice.
"""
import sys

from dhxpyt.layout import MainWindow


class testui(MainWindow):
    def load_ui(self):
        self.set_theme("light")

        # Create a column based layout and add it to the mainwindow
        # left column will be for a sidebar
        # right column will be for a toolbar and a grid
        self.base_layout = self.add_layout(
            layout_config={
                "css": "dhx_toolbar--text_color_white",
                "cols": [
                    {"width": "auto", "id": "left"},
                    {"width": "100%", "id": "right"}
                ]
            }
        )

        # Create a layout for the right column
        # top row will be for a toolbar
        # bottom row will be for a grid
        self.sub_layout = self.base_layout.add_layout(
            id="right",
            layout_config={
                "css": "dhx_layout-cell--bordered",
                "type": "line",
                "rows": [
                    {"height": "auto", "id": "top"},
                    {"height": "100%", "id": "bottom"}
                ]
            }
        )

        # Create a toolbar and add it to the top row
        self.maintb = self.sub_layout.add_toolbar(
            id="top",
            toolbar_config={
                "css": "dhx_toolbar--text_color_white",
                "data": [
                    {"id": "file", "type": "button", "value": "File"},
                    {"id": "help", "type": "button", "value": "Help"},
                ],
            },
        )

        # Attach a signal to the main toolbar to handle clicks
        self.maintb.on_click(self.menu_clicked)

        # Create a grid and add it to the bottom row
        self.grid = self.sub_layout.add_grid(
            id="bottom",
            grid_config={
                "height": "100%",
                "width": "100%",
                "selection": "row",
                "multiselection": True,
                "columns": [
                    {"id": "col1", "header": [{"text": "Column 1"}]},
                    {"id": "col2", "header": [{"text": "Column 2"}]},
                    {"id": "col3", "header": [{"text": "Column 3"}]}
                ],
                "data": [
                    {"id": 1, "col1": "Row 1, Col 1", "col2": "Row 1, Col 2", "col3": "Row 1, Col 3"},
                    {"id": 2, "col1": "Row 2, Col 1", "col2": "Row 2, Col 2", "col3": "Row 2, Col 3"},
                    {"id": 3, "col1": "Row 3, Col 1", "col2": "Row 3, Col 2", "col3": "Row 3, Col 3"}
                ]
            }
        )

    def menu_clicked(self, id, event):
        """Handle toolbar button clicks."""
        print(f"toolbar item clicked: {id}")


if __name__ == "__main__" and sys.platform != "emscripten":
    from pytincture import launch_service
    launch_service()
