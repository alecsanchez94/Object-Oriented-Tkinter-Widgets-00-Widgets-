from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import logging
import os
from project.template_widgets import WidgetResizableContainer
from project.template_widgets import WidgetRoot


class Widget_Config(WidgetRoot.WidgetRoot):
    def __init__(self,
                 parent: tk.LabelFrame,
                 config,
                 callback_config_save_value,
                 parent_canvas: tk.Canvas,
                 program_root: tk.Tk
                 ):
        super().__init__()
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Config loading")
        self.config = config
        self.config_save_value = callback_config_save_value
        self.parent = parent
        self.parent_canvas = parent_canvas
        self.program_root = program_root

        self.dynamic_container = WidgetResizableContainer.WidgetResizableContainer(self.parent,
                                                                                   self,
                                                                                   self.program_root,
                                                                                   self.parent_canvas,
                                                                                   )
        self.container = ttk.LabelFrame(self.dynamic_container.frame, text="Config Widget")

        self.container_ingest = ttk.LabelFrame(self.container, text="Ingest Settings")
        self.button_update_ingest = ttk.Button(self.container_ingest, text="Update Ingest Directory", command=self.select_ingest_directory)
        self.label_ingest = ttk.Label(self.container_ingest, text=self.config.get("SETTINGS", "ingest_directory"))

        self.container_export = ttk.LabelFrame(self.container, text="Export Settings")
        self.button_update_export = ttk.Button(self.container_export, text="Update Export Directory", command=self.select_export_directory)
        self.label_export = ttk.Label(self.container_export, text=self.config.get("SETTINGS", "export_directory"))

        # self.parent_canvas.bind("<Configure>", self.on_frame_update)
        # self.program_root.bind("<Configure>", self.on_frame_update)


    def repack(self):
        self.container.pack(side=tk.TOP, fill='both', expand=True, anchor='center', padx=10, pady=10)
        self.container_ingest.pack(fill='x', expand=True)
        self.container_export.pack(fill='x', expand=True)

        self.button_update_ingest.pack(side=tk.LEFT, padx=10, pady=10)
        self.label_ingest.pack(side=tk.LEFT, fill='x', expand=True)

        self.button_update_export.pack(side=tk.LEFT, padx=10, pady=10)
        self.label_export.pack(side=tk.LEFT, fill='x', expand=True)

    def on_frame_update(self, event=None):
        if not self.is_visible:
            return

        self.dynamic_container.on_frame_configure()
        # self.hide()
        # self.show()
        # self.container.update_idletasks()


    def on_save_click(self):
        email = self.val_dropdown_selection.get()
        behalf_of = self.val_on_behalf_of.get()
        self.config_save_value("EMAIL", "from_email", email)
        self.config_save_value("EMAIL", "behalf_of", behalf_of)
        messagebox.showinfo(title="Saved", message="Save Success")

    def resync_config(self, new_config):
        super().resync_config(new_config)
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
        super().show()
        self.dynamic_container.show()
        self.repack()


    def hide(self):
        super().hide()
        # self.container.pack_forget()
        self.dynamic_container.hide()
