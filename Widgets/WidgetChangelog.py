import tkinter as tk
import logging
import globals
from Widgets import WidgetResizableContainer


class WidgetChangelog():
    def __init__(self,
                 program_root
                 ):
        self.program_root = program_root
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Changelog loading")

        self.window = tk.Toplevel()
        self.window.title = "Change Log"
        self.scrollable_container = WidgetDynamicContainer.WidgetResizableContainer(self.window)
        self.populate()
        self.show()

    def populate(self):
        for item in globals.changelog:
            message = "{} - {}".format(item.get('date'), item.get('change'))
            label = tk.Label(self.scrollable_container.frame, text=message)
            label.pack(side=tk.TOP, fill='x')

    def show(self):
        self.scrollable_container.show(self.window)

    def hide(self):
        self.scrollable_container.hide()
