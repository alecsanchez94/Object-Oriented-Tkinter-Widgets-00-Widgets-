from tkinter import ttk, messagebox
import tkinter as tk
import pandas as pd
# from interface.TkWidgets.widget_table import CustomTable
from WidgetTable import WidgetTable
from datetime import datetime
import os
import logging
import sqlite3


class Widget_TableWithFilter:
    def __init__(self,
                 parent,
                 db_path,
                 config,
                 data_name,
                 table,
                 forced_sql_statement: str = None
                 ):

        # Declare data references
        self.forced_sql_statement = None
        if forced_sql_statement is not None:
            self.forced_sql_statement = forced_sql_statement
        self.table_name = table
        self.parent = parent
        # self.program_root = program_root
        self.db_path = db_path
        self.config = config
        self.logger = logging.getLogger('global')
        self.logger.info("Widget Exceptions loading")
        self.data_reference = pd.DataFrame
        self.refresh_data()

        # Widget Containers
        self.container = ttk.LabelFrame(parent, text=data_name)
        self.table_container = ttk.LabelFrame(self.container)
        self.filter_container = ttk.LabelFrame(self.container)
        self.table_container.pack(side=tk.TOP, fill='x')
        self.filter_container.pack(side=tk.BOTTOM, fill='x', pady=2)

        self.table = WidgetTable(self.table_container, "", self.data_reference)
        self.table.table.bind("<Double-1>", self.on_record_click)
        self.table.show()

        self.dropdown_selection = tk.StringVar(self.container)
        self.search_string = tk.StringVar(self.container)

        self.lbl_filter_by = ttk.Label(self.filter_container, text="Filter By:")
        self.lbl_filter_by.pack(side=tk.LEFT)
        columns = self.data_reference.columns
        self.fieldSelection = ttk.OptionMenu(self.filter_container, self.dropdown_selection, "Select Column",
                                             *self.data_reference.columns)
        self.fieldSelection.pack(side=tk.LEFT, padx=10, pady=1, anchor='w')

        self.search_box = ttk.Entry(self.filter_container, textvariable=self.search_string)
        self.search_box.pack(side=tk.LEFT, padx=6)
        self.btn = ttk.Button(self.filter_container, text="Search", command=self.search)
        self.btn.pack(side=tk.LEFT, pady=10)

        self.search_box.bind('<Return>', self.search)

        self.reset_button = ttk.Button(self.filter_container, text="Reset", command=self.reset_table_and_search)
        self.reset_button.pack(side=tk.LEFT, anchor='w', padx=10, pady=10)

        self.label_record_count = ttk.Label(self.filter_container,
                                            text="Record Count: {}".format(len(self.data_reference)))
        self.label_record_count.pack(side=tk.BOTTOM)

        self.reset_table_and_search()

    def refresh_data(self):
        conn = sqlite3.connect(self.db_path)
        self.logger.info("Table: {}".format(self.table_name))

        if self.forced_sql_statement is not None:
            self.data_reference = pd.read_sql(self.forced_sql_statement, conn)
        else:
            self.data_reference = pd.read_sql("select * from {}".format(self.table_name), conn)

        conn.close()

    def on_record_click(self, event=None):
        table_ref = self.table.table.focus()
        selected_item = self.table.table.item(table_ref)

        form_values = list(selected_item.values())[2]
        #
        # self.var_document.set(form_values[0])
        # self.var_gtc.set(form_values[1])
        # self.var_financial_poc_name.set(form_values[2])
        # self.var_financial_poc_email.set(form_values[3])
        # self.var_technical_poc_name.set(form_values[4])
        # self.var_technical_poc_email.set(form_values[5])
        # self.var_organization_name.set(form_values[6])
        # self.var_is_exception.set(form_values[7])
        # self.var_exception_comment.set(form_values[8])

    def get_selection(self):
        table_ref = self.table.table.focus()
        selected_item = self.table.table.item(table_ref)
        form_values = list(selected_item.values())[2]

        return form_values

    def clear_table_contents(self):
        self.table.table.delete(*self.table.table.get_children())

    def reset_table_and_search(self, ):

        # Reset table data

        self.refresh_data()
        self.clear_table_contents()
        # self.solve_navy_count(admin_data)

        # Reset search form
        self.dropdown_selection.set("Select an Option")
        self.search_string.set("")
        self.table.refresh_table(self.data_reference)
        self.refresh_record_count()

    def search(self, event=None, b_force_refresh=False):
        fieldName = self.dropdown_selection.get()
        value = self.search_string.get()

        if (fieldName == "Select an Option" or value == ""):

            if (b_force_refresh):
                self.reset_table_and_search()
            else:
                messagebox.showinfo("Query Exception",
                                    "Please select a field and provide a value")
            return

        conn = sqlite3.connect(self.db_path)

        if self.forced_sql_statement is not None:
            df = pd.read_sql("""
                WITH RECURSIVE CTE AS (
                    {sql_statement}
                )
                SELECT * from CTE where `{fieldname}` like '%{queryvalue}%'

            """.format(sql_statement=self.forced_sql_statement,
                       tablename=self.table_name,
                       fieldname=fieldName,
                       queryvalue=value), conn)

        else:
            df = pd.read_sql("SELECT * from {} where `{}` like '%{}%'".format(self.table_name, fieldName, value), conn)

        conn.close()
        self.table.refresh_table(df)
        self.refresh_record_count()

    def refresh_record_count(self):
        self.label_record_count.configure(text="Record Count: {}".format(len(self.data_reference)))

    def show(self):
        self.container.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.container.pack_forget()







