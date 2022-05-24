import tkinter as tk
import logging
from project import globals
from project.template_widgets import WidgetResizableContainer, WidgetRoot


class WidgetChangelog(WidgetRoot):
    def __init__(self,
                 program_root,
                 program_canvas,
                 parent: tk.LabelFrame,
                 ):

        super().__init__()
        self.program_root = program_root
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Changelog loading")

        self.window = tk.Toplevel()
        self.window.title = "Change Log"
        self.scrollable_container = WidgetResizableContainer.WidgetResizableContainer(self.window)
        self.populate()
        self.show()

    def populate(self):
        for item in globals.changelog:
            message = "{} - {}".format(item.get('date'), item.get('change'))
            label = tk.Label(self.scrollable_container.frame, text=message)
            label.pack(side=tk.TOP, fill='x')

    def show(self):
        super().show()
        self.scrollable_container.show()

    def hide(self):
        super.hide()
        self.scrollable_container.hide()
