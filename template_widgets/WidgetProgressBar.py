from tkinter import ttk
import tkinter as tk
import logging

class WidgetProgressTextAndBar():
    def __init__(self, parent, container_text):
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Progress loading")
        self.container = ttk.LabelFrame(parent, text=container_text)
        self.progress_text = ttk.Label(self.container, text="Progress")
        self.progress_text.pack(side=tk.LEFT, padx=10)

        self.progress_bar = ttk.Progressbar(self.container, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress_bar.pack(side=tk.BOTTOM, fill='x')
        self.logger.info("Widget Progress started")

    def show(self):
        self.container.pack(side=tk.BOTTOM, fill='x')

    def hide(self):
        self.container.pack_forget()

    def update_progress_bar(self, new_value: int):
        if(self.progress_bar == None):
            return
        self.progress_bar['value'] = new_value

    def update_progress_text(self, new_value: str):
        self.progress_text.config(text=new_value)
