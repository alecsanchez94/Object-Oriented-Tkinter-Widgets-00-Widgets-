import tkinter as tk
from project.template_widgets import WidgetRoot


class WidgetResizableContainer(tk.Frame):

    def __init__(self, parent_container: tk.LabelFrame,
                 parent: WidgetRoot.WidgetRoot,
                 program_root: tk.Tk,
                 program_canvas: tk.Canvas
                 ):
        tk.Frame.__init__(self, parent_container)

        self.parent = parent

        self.parent_container = parent_container
        self.program_root = program_root
        self.program_canvas = program_canvas


        self.canvas = tk.Canvas(master=self)
        self.frame = tk.Frame(master=self.canvas)

        self.y_scrollbar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.x_scrollbar = tk.Scrollbar(self, orient='horizontal', command=self.canvas.xview)
        self.y_scrollbar.pack(side=tk.RIGHT, fill='y')
        # self.x_scrollbar.pack(side=tk.BOTTOM, fill='x')
        self.canvas.create_window((0,0), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.canvas.configure(xscrollcommand=self.x_scrollbar.set)
        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("")



    def bind_parent_config_update(self, dynamic_container_root):
        dynamic_container_root.bind("<Configure>", self.on_frame_configure)
        self.program_canvas.bind("<Configure>", self.on_frame_configure)
        self.program_root.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event=None):
        '''Reset the scroll region to encompass the inner frame'''
        if not self.parent.is_visible:
            return

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.itemconfigure('self.frame',width=self.canvas.winfo_width())



    def hide(self):
        self.pack_forget()

    def show(self):
        self.bind_parent_config_update(self.parent_container)
        self.on_frame_configure()
        self.canvas.pack(fill='both',expand=True)
        self.pack(fill='both', expand=True)



class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame,
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)

    def onFrameConfigure(self, event=None):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.itemconfigure('self.frame',width=self.canvas.winfo_width())

    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"
        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    def update(self):
        "Update the canvas and the scrollregion"
        self.update_idletasks()



