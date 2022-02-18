import configparser
import logging
import os
import sys
import tkinter as tk
from tkinter import ttk
import pystray
from PIL import Image
from pystray import MenuItem as item
import globals
from Widgets import WidgetChangelog
from Widgets import WidgetTextbox

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

class Program():
    def __init__(self):
        # Frame.__init__(self, master)
        self.master = tk.Tk()
        # self.master.overrideredirect(1)
        self.master.geometry("1000x600")

        self.style = ttk.Style(self.master)
        # https://stackoverflow.com/questions/42958927/how-to-change-tkinter-lableframe-border-color
        # self.style.configure("TLabelframe", background='black')
        # self.style.configure("TLabelframe", background='#808080')

        self.master.title(globals.title)
        self.logger = logging.getLogger('global')

        self.config_file = os.path.join(os.getcwd(), 'config.ini')
        self.config = None
        self.load_config_file()


        # Declare widgets and containers here, pack/place/grid in render_content()
        self.container_console = tk.LabelFrame(self.master)
        self.console = WidgetTextbox.WidgetTextbox(self.container_console, container_text="Console")
        text_handler = WidgetTextbox.TextHandler(self.console)
        self.logger.addHandler(text_handler)
        self.render_content()
        self.logger.info("Application Loaded")

        center(self.master)
        self.master.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.master.mainloop()


    def load_config_file(self):
        logger.info("Loading Config File")
        if not os.path.exists(self.config_file):
            with open(self.config_file, 'w') as openedConfigFile:
                openedConfigFile.write('[SETTINGS]')
                openedConfigFile.close()


            self.reset_config_file()
            logger.warning("Config file not found, creating a new one with defaulted values")
            return

        self.config = configparser.RawConfigParser()
        self.config.read(self.config_file)

        directories = [
            os.path.exists(self.config.get("SETTINGS", 'export_directory'))
        ]

        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)



    def reset_config_file(self):

        self.config = configparser.RawConfigParser()
        self.config.read(self.config_file)

        relative_output_directory = os.path.join(os.getcwd(), "Exports")
        if not os.path.exists(relative_output_directory):
            os.makedirs(relative_output_directory)

        self.config.set('SETTINGS', 'export_directory', str(relative_output_directory))

        self.config_save()

    def resync_children_config(self):
        pass
        # self.child_widget.update_config(self.config)

    def config_save(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def render_content(self):

        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file = tk.Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        help_menu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="View Changelog", command=self.show_changelog)

        self.console.show()
        self.container_console.pack(side=tk.BOTTOM, fill='x', anchor='s')


    def show_changelog(self):
        WidgetChangelog.WidgetChangelog()

    def client_exit(self):
        sys.exit()

    # Define a function for quit the window
    def quit_window(self, icon, item):
        icon.stop()
        self.master.destroy()

    def show_window(self, icon, item):
        icon.stop()
        self.master.after(0,self.master.deiconify())

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

