from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import logging
import os
from Widgets import WidgetRoot

class WidgetDataExplorer(WidgetRoot.WidgetRoot):
    def __init__(self,
                 parent,
                 config):
        self.config = config
        self.parent = parent


        self.logger = logging.getLogger('global')


    def resync_config(self, new_config):
        super().resync_config()


