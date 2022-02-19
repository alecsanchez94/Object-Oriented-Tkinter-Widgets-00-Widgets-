from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import logging
import os


class WidgetConfig():
    def __init__(self,
                 parent: tk.LabelFrame,
                 container_text: str,
                 config,
                 callback_config_save_value
                 ):
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Config loading")
        self.config = config
        self.config_save_value = callback_config_save_value

        self.container = ttk.LabelFrame(parent, text=container_text)

        self.container_ingest = ttk.LabelFrame(self.container, text="Ingest Settings")
        self.button_update_ingest = ttk.Button(self.container_ingest, text="Update Ingest Directory", command=self.select_ingest_directory)
        self.label_ingest = ttk.Label(self.container_ingest, text=self.config.get("SETTINGS", "ingest_directory"))
        self.button_update_ingest.pack(side=tk.LEFT, padx=10, pady=10)
        self.label_ingest.pack(side=tk.LEFT)

        self.container_export = ttk.LabelFrame(self.container, text="Export Settings")
        self.button_update_export = ttk.Button(self.container_export, text="Update Export Directory", command=self.select_export_directory)
        self.label_export = ttk.Label(self.container_export, text=self.config.get("SETTINGS", "export_directory"))
        self.button_update_export.pack(side=tk.LEFT, padx=10, pady=10)
        self.label_export.pack(side=tk.LEFT)

        self.container_ingest.pack(fill='x')
        self.container_export.pack(fill='x')


    def on_save_click(self):
        email = self.val_dropdown_selection.get()
        behalf_of = self.val_on_behalf_of.get()
        self.config_save_value("EMAIL", "from_email", email)
        self.config_save_value("EMAIL", "behalf_of", behalf_of)
        messagebox.showinfo(title="Saved", message="Save Success")



    def resync_config_from_parent(self, config):
        self.config = config
        self.label_ingest.config(text=self.config.get("SETTINGS", "ingest_directory"))
        self.label_export.config(text=self.config.get("SETTINGS", "export_directory"))

    def select_ingest_directory(self):
        ingest_directory = filedialog.askdirectory(initialdir=os.getcwd(),
                                                   title="Please select the data ingest directory")


        self.config_save_value("SETTINGS", "ingest_directory", ingest_directory)

    def select_export_directory(self):
        export_directory = filedialog.askdirectory(initialdir=os.getcwd(), title="Please select the export directory")
        self.config_save_value("SETTINGS", "export_directory", export_directory)

    def show(self):
        self.container.pack(side=tk.TOP, fill='both', expand=True, anchor='center', padx=10, pady=10)

    def hide(self):
        self.container.pack_forget()
