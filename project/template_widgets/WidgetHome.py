from tkinter import ttk
import tkinter as tk
import logging
from tkhtmlview import HTMLLabel
from project import globals
import os

class WidgetHome():
    def __init__(self,
                 parent: tk.LabelFrame,
                 container_text: str,
                 ):
        self.logger = logging.getLogger('global')
        self.container = ttk.LabelFrame(parent, text=container_text)
        self.label_html = None
        self.load_html_data()
        self.logger.info("Home widget loaded")

    def load_html_data(self):
        data = ""
        html_file = os.path.join(os.path.join(globals.parent_directory, "template_documentation"), "docs.html")

        with open(html_file) as f:
            data = f.read()
            f.close()

        self.label_html = HTMLLabel(self.container, html=data)
        self.label_html.pack(fill='both', expand=True)


    def show(self):
        self.container.pack(side=tk.TOP,fill='both', expand=True, anchor='center')

    def hide(self):
        self.container.pack_forget()