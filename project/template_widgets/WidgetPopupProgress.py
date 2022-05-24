from tkinter import ttk, messagebox
import tkinter as tk
from project.template_widgets import WidgetProgressBar
import logging


def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y))
    toplevel.title("Centered!")


class WidgetPopupProgress():
    def __init__(self,
                 parent,
                 cancel_callback
                 ):
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Popup Progress loading")

        self.cancel_callback = cancel_callback

        self.window = tk.Toplevel(parent)
        self.container = ttk.LabelFrame(self.window)
        self.text_label = ttk.Label(self.container, text="Operation Pending")
        self.text_label.pack(fill='both',expand=True)

        self.progress_bar = WidgetProgressBar.WidgetProgressTextAndBar(self.container, "Progress")
        self.progress_bar.show()

        self.button_cancel = ttk.Button(self.container, text="Cancel", command=self.cancel_callback)
        self.button_cancel.pack(side=tk.BOTTOM, fill='x', expand=True)



        self.logger.info("Widget Home First Test")
        center(self.window)

    def complete(self):
        self.button_cancel.pack_forget()
        self.window.destroy()
        messagebox.showinfo(title="Operation Status", message="Operation Complete")

    def show(self):
        self.container.pack(side=tk.TOP,fill='both', expand=True, anchor='center')

    def hide(self):
        self.container.pack_forget()

