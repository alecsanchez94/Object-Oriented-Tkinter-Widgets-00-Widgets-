import sqlite3
from tkinter import ttk
import tkinter as tk
import logging
from project.template_widgets import WidgetResizableContainer, WidgetTableWithFilter
from project.template_widgets import WidgetRoot
import pandas as pd
from project import globals


class WidgetDataExplorer(WidgetRoot.WidgetRoot):
    def __init__(self,
                 parent,
                 config,
                 program_root,
                 program_canvas):
        super().__init__()

        self.config = config
        self.parent = parent
        self.logger = logging.getLogger('global')
        self.program_root = program_root
        self.program_canvas = program_canvas

        self.dynamic_container = WidgetResizableContainer.WidgetResizableContainer(self.parent,
                                                                                   self,
                                                                                   self.program_root,
                                                                                   self.program_canvas)

        self.container = ttk.LabelFrame(self.dynamic_container.frame, text="Config Widget")
        self.container.pack(fill=tk.BOTH, expand=True)

        self.group1 = tk.Frame(self.container)
        self.group2 = tk.Frame(self.container)

        self.group1.pack(fill=tk.BOTH, expand=True)
        self.group2.pack(fill=tk.BOTH, expand=True)

        self.table = WidgetTableWithFilter.Widget_TableWithFilter(self.group1,
                                                                  globals.db_path,
                                                                  self.config,
                                                                  "Data Explorer",
                                                                  self.get_tables()[0]
                                                                  )

        self.table.show()







    def get_tables(self) -> []:
        conn = sqlite3.connect(globals.db_path)

        sql_statement = """
        SELECT
            name
        FROM
            sqlite_master
        WHERE
            type ='table' 
        
        """

        data = pd.read_sql(sql_statement, conn)
        conn.close()

        return data['name'].unique().tolist()



    def resync_config(self, new_config):
        super().resync_config(new_config)

    def show(self):
        super().show()
        self.dynamic_container.show()

    def hide(self):
        super().hide()
        self.dynamic_container.hide()
