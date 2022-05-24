from tkinter import ttk
import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd
import logging
from threading import Thread
from WidgetRoot import WidgetRoot

class WidgetIngest(WidgetRoot):
    def __init__(self, parent, config):
        self.logger = logging.getLogger('global')
        self.parent = parent
        self.config = config
        self.main_container = tk.LabelFrame(parent, text="Ingest")
        self.button_ingest = ttk.Button(self.main_container, text="Update Export Directory",
                                               command=self.on_ingest_click())

        self.button_ingest.pack()

    def show(self):
        self.main_container.pack()

    def hide(self):
        self.main_container.pack_forget()

    def resync_config(self, new_config):
        super().resync_config()


    def on_ingest_click(self):


        def handle_flat_file(file_path, table_name):
            data = pd.read_csv(file_path)



        def task():

            file = tk.filedialog.askopenfilename()
            table_name = simpledialog.Dialog(title="Table Name",
                                             prompt="What is the table name?")

            # if file.endswith("csv") or file.endswith(".txt")


            pass

        t1 = Thread(target=task).start()




