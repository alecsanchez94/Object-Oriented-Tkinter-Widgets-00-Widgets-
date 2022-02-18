from tkinter import ttk, scrolledtext
import tkinter as tk
import logging
from datetime import datetime

class WidgetTextbox():

    def __init__(self, parent, container_text):
        self.container = ttk.LabelFrame(master=parent, text=container_text)
        self.textlogger = scrolledtext.ScrolledText(
            master=self.container,
            wrap='word',  # wrap text at full words only
            width=60,  # characters
            height=5,  # text lines
            bg='#FFFBFB')

        self.textlogger.pack(fill='both', expand=True)

    def insert_text(self, text: str):
        self.textlogger.insert(tk.END, "{} \n".format(text))
        self.textlogger.see(tk.END)

    def clear(self):
        self.textlogger.delete('1.0', tk.END)

    def show(self):
        self.container.pack(fill='both', expand=True)



class TextHandler(logging.Handler):
    def __init__(self, textbox: WidgetTextbox):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = textbox

    def emit(self, record):
        msg = self.format(record)
        def append():
            now = datetime.now()
            dt_string = now.strftime("%d-%b-%Y %H-%M-%S")
            self.text.insert_text("{} - {}".format(dt_string, msg))
        # This is necessary because we can't modify the Text from other threads
        self.text.textlogger.after(0, append)