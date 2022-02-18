from tkinter import ttk
import tkinter as tk
import pandas as pd
import logging

class WidgetTable():

    def __init__(self, parent, container_text: str, dataframe: pd.DataFrame, b_force_empty_table: bool=False):
        """
        Requires an array of columns
        :param parent:
        :param container_text:
        """
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Table loading")
        self.main_container = tk.LabelFrame(parent, text=container_text)

        self.table_container = tk.LabelFrame(self.main_container, text="Table")

        self.container_summary = tk.LabelFrame(self.main_container, text="Stats")

        self.label_count = ttk.Label(self.container_summary, text='Record Count: {}'.format(0))
        self.label_count.pack(side=tk.RIGHT, padx=10, pady=0)

        self.table = ttk.Treeview(self.table_container, columns=(dataframe.columns), show='headings')
        self.scroll_x = ttk.Scrollbar(self.table_container, orient='horizontal')
        self.scroll_y = ttk.Scrollbar(self.table_container, orient='vertical')
        self.scroll_x.configure(command=self.table.xview)
        self.scroll_y.configure(command=self.table.yview)

        self.table.configure(xscrollcommand=self.scroll_x.set)
        self.table.configure(yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=tk.TOP, fill='x')
        self.scroll_y.pack(side=tk.RIGHT, fill='y')
        self.table.pack(fill='both', expand=True, padx=10, pady=10)
        self.table_container.pack(side=tk.TOP, fill='both', expand=True, padx=10, pady=10)
        self.container_summary.pack(side=tk.BOTTOM, fill='x', expand=True, padx=10, pady=10)
        self.columns = dataframe.columns

        self.setup_table(dataframe, b_force_empty_table)

        self.container_summary.pack(fill='x')
        self.logger.info("Table started")

    def update_record_count(self, new_count: int):
        self.label_count.config(text="Record Count: {}".format(new_count))

    def show(self):
        self.main_container.pack(fill='both', padx=10, pady=10, expand=True)

    def hide(self):
        self.main_container.pack_forget()
        # self.container.pack_forget()

    def refresh_table(self, dataframe: pd.DataFrame):
        self.setup_table(dataframe)
        self.update_record_count(len(dataframe.reset_index(drop=True)))

    def clear_table_content(self):
        for col in self.table['columns']:
            self.table.heading(col, text='')
        self.table.delete(*self.table.get_children())

    def setup_table(self, dataframe: pd.DataFrame, force_empty_table: bool=False):
        self.clear_table_content()
        self.table['columns'] = dataframe.columns

        self.setup_columns(dataframe)
        self.update_table_records(dataframe, force_empty_table)

    def setup_columns(self, dataframe: pd.DataFrame):
        if(len(dataframe.columns) == 0):
            return
        fieldIndex = 0
        for col in dataframe.columns:
            max_width = dataframe[col].astype(str).str.len().max() + 30 * 3
            if (pd.isna(max_width)):
                max_width = 10 + 30 * 3

            self.table.column(fieldIndex, minwidth=45, width=max_width, stretch=True)
            self.table.heading(fieldIndex, text=col)

            fieldIndex += 1

    def update_table_records(self, dataframe: pd.DataFrame, force_empty_table: bool):
        # Clears the table records before we add
        self.table.delete(*self.table.get_children())

        if (force_empty_table):
            return

        for index, row in dataframe.iterrows():
            values = []
            for x in row:
                values.append(x)
            self.table.insert('', 'end', values=values)
