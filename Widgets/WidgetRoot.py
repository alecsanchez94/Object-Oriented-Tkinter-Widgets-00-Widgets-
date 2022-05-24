from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import logging

class WidgetRoot:
    def __init__(self):
        self.config = None
        self.parent = None
        self.logger = logging.getLogger('global')


    def resync_config(self, new_config):
        self.config = new_config





