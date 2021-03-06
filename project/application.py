import configparser
import logging
import os
import tkinter as tk
from tkinter import ttk
import pystray
from PIL import Image
from pystray import MenuItem as item
import globals
from project.template_widgets import WidgetHome, WidgetConfig
from project.template_widgets import WidgetChangelog, WidgetDataExplorer, WidgetTextbox

logger = logging.getLogger('global')


def configure_logging():
    logger.setLevel(logging.DEBUG)
    # Format for our loglines
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # Setup console logging
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    # Setup file logging as well
    fh = logging.FileHandler('log.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)


class Program:
    def __init__(self):
        self.master = tk.Tk()
        self.master.withdraw()
        self.master.geometry("600x500")
        self.style = ttk.Style(self.master)
        self.master.title(globals.title)
        self.logger = logging.getLogger('global')

        self.style = ttk.Style(self.master)
        # https://stackoverflow.com/questions/42958927/how-to-change-tkinter-lableframe-border-color
        # self.style.configure("TLabelframe", background='black')
        # self.style.configure("TLabelframe", background='#808080')

        self.master_canvas = tk.Canvas(master=self.master)
        self.master_canvas.pack(fill="both", expand=True)

        # Main Layout
        self.left_column = tk.LabelFrame(self.master_canvas, text="Steps")
        self.main_content = tk.LabelFrame(self.master_canvas, text="Content")
        self.container_console = tk.LabelFrame(self.master_canvas)

        self.console = WidgetTextbox.WidgetTextbox(self.container_console, container_text="Console")
        text_handler = WidgetTextbox.TextHandler(self.console)
        self.logger.addHandler(text_handler)

        # Load config file
        self.config_file = os.path.join(os.getcwd(), 'config.ini')
        self.config = None
        self.load_config_file()

        # Left Colum Buttons
        self.button_home = tk.Button(self.left_column, text="Home", command=self.on_home_click)
        self.button_config = tk.Button(self.left_column, text="Config", command=self.on_config_click)
        self.button_ingest = tk.Button(self.left_column, text="Ingest", command=self.on_ingest_click)
        self.button_data_explorer = tk.Button(self.left_column, text="Data Explorer",
                                              command=self.on_data_explorer_click)
        # Widgets
        self.widget_home = WidgetHome.WidgetHome(self.main_content, "Home")
        self.widget_config = WidgetConfig.Widget_Config(self.main_content,
                                                        self.config,
                                                        self.callback_update_config,
                                                        self.master_canvas,
                                                        self.master
                                                        )
        self.widget_data_explorer = WidgetDataExplorer.WidgetDataExplorer(
            self.main_content,
            self.config,
            self.master,
            self.master_canvas
        )

        self.render_window()
        self.widget_home.show()
        self.logger.info("Application Initialized")

        center(self.master)
        self.master.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.master.mainloop()

    def on_data_explorer_click(self):
        self.hide_widgets()
        self.widget_data_explorer.show()

    def on_ingest_click(self):
        pass

    def refresh_children(self):
        pass

    def callback_update_config(self, section, key, new_value):
        self.config.set(section, key, new_value)
        self.config_save()
        self.resync_children_config()

    def resync_children_config(self):
        self.widget_config.resync_config(self.config)
        self.widget_data_explorer.resync_config(self.config)

    def hide_widgets(self):
        self.widget_home.hide()
        self.widget_config.hide()
        self.widget_data_explorer.hide()

    def on_home_click(self):
        self.hide_widgets()
        self.widget_home.show()

    def on_config_click(self):
        self.hide_widgets()
        self.resync_children_config()
        self.widget_config.show()

    def reset_config_file(self):

        if os.path.exists(self.config_file):
            return

        logger.warning("Config file not found, creating a new one with defaulted values")
        with open(self.config_file, 'w') as openedConfigFile:
            openedConfigFile.write('[SETTINGS]')
            openedConfigFile.close()

        self.config.read(self.config_file)

        ingest_directory = os.path.join(os.getcwd(), "IngestFiles")
        if not os.path.exists(ingest_directory):
            os.makedirs(ingest_directory)

        export_directory = os.path.join(os.getcwd(), "Exports")
        if not os.path.exists(export_directory):
            os.makedirs(export_directory)

        self.config.set('SETTINGS', 'ingest_directory', str(ingest_directory))
        self.config.set('SETTINGS', 'export_directory', str(export_directory))

        self.config_save()

    def config_save(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def load_config_file(self):
        logger.info("Loading Config File")
        self.config = configparser.RawConfigParser()
        self.reset_config_file()  # < -- Returns if config exists
        self.config.read(self.config_file)

        directories = [
            os.path.exists(self.config.get("SETTINGS", 'ingest_directory')),
            os.path.exists(self.config.get("SETTINGS", 'export_directory'))
        ]

        for dir in directories:
            if not os.path.exists(dir):
                os.makedirs(dir)

    def render_window(self):

        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file = tk.Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        help_menu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="View Changelog", command=self.show_changelog)

        self.button_home.pack(side=tk.TOP, fill='x')
        self.button_config.pack(side=tk.TOP, fill='x')
        self.button_data_explorer.pack(side=tk.TOP, fill='x')
        self.container_console.pack(side=tk.BOTTOM, fill='x', anchor='s')
        self.left_column.pack(side=tk.LEFT, fill='y', padx=3, pady=3, ipadx=15)
        self.main_content.pack(fill='both', expand=True)

        self.console.show()

    def show_changelog(self):
        WidgetChangelog.WidgetChangelog(self.master, self.master_canvas, self)

    def client_exit(self):
        self.master.destroy()

    def quit_window(self, icon):
        icon.stop()
        self.master.destroy()

    def show_window(self, icon):
        icon.stop()
        self.master.after(0, self.master.deiconify())

    def hide_window(self):
        self.master.withdraw()
        image = Image.open(os.path.join(globals.parent_directory, "Images", "data.ico"))
        menu = (item('Quit', self.quit_window), item('Show', self.show_window))
        icon = pystray.Icon("name", image, "My System Tray Icon", menu)
        icon.run()


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


if __name__ == "__main__":
    configure_logging()
    logger.debug("New Log Method Test")
    app = Program()
