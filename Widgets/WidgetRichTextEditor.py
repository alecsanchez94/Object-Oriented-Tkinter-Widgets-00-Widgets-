from tkinter import ttk, messagebox, Frame, Button, filedialog, simpledialog, colorchooser, font
import tkinter as tk
import logging
from PIL import ImageTk, Image
from globals import parent_directory
import os


class WidgetRichTextEditor:
    def __init__(self,
                 parent):

        # ------------- CREATING - MENUBAR AND ITS MENUS, TOOLS BAR, FORMAT BAR, STATUS BAR AND TEXT AREA -----------#

        self.parent = parent
        self.master = tk.LabelFrame(parent)
        # TOOLBAR
        self.toolbar = Frame(self.master, pady=2)

        # TOOLBAR BUTTONS
        # new
        self.new_button = Button(name="toolbar_b2", borderwidth=1, command=self.new, width=20, height=20)

        self.photo_new = Image.open(os.path.join(parent_directory, "icons", "new.png"))
        self.photo_new = self.photo_new.resize((18, 18), Image.ANTIALIAS)
        self.image_new = ImageTk.PhotoImage(self.photo_new)
        self.new_button.config(image=self.image_new)
        self.new_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # save
        self.save_button = Button(name="toolbar_b1", borderwidth=1, command=self.save, width=20, height=20)

        self.photo_save = Image.open(os.path.join(parent_directory, "icons", "save.png"))
        self.photo_save = self.photo_save.resize((18, 18), Image.ANTIALIAS)
        self.image_save = ImageTk.PhotoImage(self.photo_save)
        self.save_button.config(image=self.image_save)
        self.save_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # open
        self.open_button = Button(name="toolbar_b3", borderwidth=1, command=self.open_file, width=20, height=20)

        self.photo_open = Image.open(os.path.join(parent_directory, "icons", "open.png"))
        self.photo_open = self.photo_open.resize((18, 18), Image.ANTIALIAS)
        self.image_open = ImageTk.PhotoImage(self.photo_open)
        self.open_button.config(image=self.image_open)
        self.open_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # copy
        self.copy_button = Button(name="toolbar_b4", borderwidth=1, command=self.copy, width=20, height=20)

        self.photo_copy = Image.open(os.path.join(parent_directory, "icons", "copy.png"))
        self.photo_copy = self.photo_copy.resize((18, 18), Image.ANTIALIAS)
        self.image_copy = ImageTk.PhotoImage(self.photo_copy)
        self.copy_button.config(image=self.image_copy)
        self.copy_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # cut
        self.cut_button = Button(name="toolbar_b5", borderwidth=1, command=self.cut, width=20, height=20)

        self.photo_cut = Image.open(os.path.join(parent_directory, "icons", "cut.png"))
        self.photo_cut = self.photo_cut.resize((18, 18), Image.ANTIALIAS)
        self.image_cut = ImageTk.PhotoImage(self.photo_cut)
        self.cut_button.config(image=self.image_cut)
        self.cut_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # paste
        self.paste_button = Button(name="toolbar_b6", borderwidth=1, command=self.paste, width=20, height=20)

        self.photo_paste = Image.open(os.path.join(parent_directory, "icons", "paste.png"))
        self.photo_paste = self.photo_paste.resize((18, 18), Image.ANTIALIAS)
        self.image_paste = ImageTk.PhotoImage(self.photo_paste)
        self.paste_button.config(image=self.image_paste)
        self.paste_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # redo
        self.redo_button = Button(name="toolbar_b7", borderwidth=1, command=self.redo, width=20, height=20)

        self.photo_redo = Image.open(os.path.join(parent_directory, "icons", "redo.png"))
        self.photo_redo = self.photo_redo.resize((18, 18), Image.ANTIALIAS)
        self.image_redo = ImageTk.PhotoImage(self.photo_redo)
        self.redo_button.config(image=self.image_redo)
        self.redo_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # undo
        self.undo_button = Button(name="toolbar_b8", borderwidth=1, command=self.undo, width=20, height=20)

        self.photo_undo = Image.open(os.path.join(parent_directory, "icons", "undo.png"))
        self.photo_undo = self.photo_undo.resize((18, 18), Image.ANTIALIAS)
        self.image_undo = ImageTk.PhotoImage(self.photo_undo)
        self.undo_button.config(image=self.image_undo)
        self.undo_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # find
        self.find_button = Button(name="toolbar_b9", borderwidth=1, command=self.find_text, width=20, height=20)

        self.photo_find = Image.open(os.path.join(parent_directory, "icons", "find.png"))
        self.photo_find = self.photo_find.resize((18, 18), Image.ANTIALIAS)
        self.image_find = ImageTk.PhotoImage(self.photo_find)
        self.find_button.config(image=self.image_find)
        self.find_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

        # FORMATTING BAR
        self.formattingbar = Frame(self.master, padx=2, pady=2)

        # FORMATTING BAR COMBOBOX - FOR FONT AND SIZE
        # font combobox

        self.all_fonts = tk.StringVar()
        self.font_menu = ttk.Combobox(self.formattingbar, textvariable=self.all_fonts, state="readonly")
        self.font_menu.pack(in_=self.formattingbar, side="left", padx=4, pady=4)
        self.font_menu['values'] = (
        'Courier', 'Helvetica', 'Liberation Mono', 'OpenSymbol', 'Century Schoolbook L', 'DejaVu Sans Mono',
        'Ubuntu Condensed', 'Ubuntu Mono', 'Lohit Punjabi', 'Mukti Narrow', 'Meera', 'Symbola', 'Abyssinica SIL')
        self.font_menu.bind('<<ComboboxSelected>>', self.change_font)
        self.font_menu.current(2)

        # size combobox
        self.all_size = tk.StringVar()
        self.size_menu = ttk.Combobox(self.formattingbar, textvariable=self.all_size, state='readonly', width=5)
        self.size_menu.pack(in_=self.formattingbar, side="left", padx=4, pady=4)
        self.size_menu['values'] = ('10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30')
        self.size_menu.bind('<<ComboboxSelected>>', self.change_size)
        self.size_menu.current(1)

        # FORMATBAR BUTTONS
        # bold
        self.bold_button = Button(name="formatbar_b1", borderwidth=1, command=self.bold, width=20, height=20, pady=10, padx=10)

        self.photo_bold = Image.open(os.path.join(parent_directory, "icons", "bold.png"))
        self.photo_bold = self.photo_bold.resize((18, 18), Image.ANTIALIAS)
        self.image_bold = ImageTk.PhotoImage(self.photo_bold)
        self.bold_button.config(image=self.image_bold)
        self.bold_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # italic
        self.italic_button = Button(name="formatbar_b2", borderwidth=1, command=self.italic, width=20, height=20)

        self.photo_italic = Image.open(os.path.join(parent_directory, "icons", "italic.png"))
        self.photo_italic = self.photo_italic.resize((18, 18), Image.ANTIALIAS)
        self.image_italic = ImageTk.PhotoImage(self.photo_italic)
        self.italic_button.config(image=self.image_italic)
        self.italic_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # underline
        self.underline_button = Button(name="formatbar_b3", borderwidth=1, command=self.underline, width=20, height=20)

        self.photo_underline = Image.open(os.path.join(parent_directory, "icons", "underline.png"))
        self.photo_underline = self.photo_underline.resize((18, 18), Image.ANTIALIAS)
        self.image_underline = ImageTk.PhotoImage(self.photo_underline)
        self.underline_button.config(image=self.image_underline)
        self.underline_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # strike
        self.strike_button = Button(name="formatbar_b4", borderwidth=1, command=self.strike, width=20, height=20)

        self.photo_strike = Image.open(os.path.join(parent_directory, "icons", "strike.png"))
        self.photo_strike = self.photo_strike.resize((18, 18), Image.ANTIALIAS)
        self.image_strike = ImageTk.PhotoImage(self.photo_strike)
        self.strike_button.config(image=self.image_strike)
        self.strike_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # font_color
        self.font_color_button = Button(name="formatbar_b5", borderwidth=1, command=self.change_color, width=20, height=20)

        self.photo_font_color = Image.open(os.path.join(parent_directory, "icons", "font-color.png"))
        self.photo_font_color = self.photo_font_color.resize((18, 18), Image.ANTIALIAS)
        self.image_font_color = ImageTk.PhotoImage(self.photo_font_color)
        self.font_color_button.config(image=self.image_font_color)
        self.font_color_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # highlight
        self.highlight_button = Button(name="formatbar_b6", borderwidth=1, command=self.highlight, width=20, height=20)

        self.photo_highlight = Image.open(os.path.join(parent_directory, "icons", "highlight.png"))
        self.photo_highlight = self.photo_highlight.resize((18, 18), Image.ANTIALIAS)
        self.image_highlight = ImageTk.PhotoImage(self.photo_highlight)
        self.highlight_button.config(image=self.image_highlight)
        self.highlight_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # align_center
        self.align_center_button = Button(name="formatbar_b7", borderwidth=1, command=self.align_center, width=20, height=20)

        self.photo_align_center = Image.open(os.path.join(parent_directory, "icons", "align-center.png"))
        self.photo_align_center = self.photo_align_center.resize((18, 18), Image.ANTIALIAS)
        self.image_align_center = ImageTk.PhotoImage(self.photo_align_center)
        self.align_center_button.config(image=self.image_align_center)
        self.align_center_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # align_justify
        self.align_justify_button = Button(name="formatbar_b8", borderwidth=1, command=self.align_justify, width=20, height=20)

        self.photo_align_justify = Image.open(os.path.join(parent_directory, "icons", "align-justify.png"))
        self.photo_align_justify = self.photo_align_justify.resize((18, 18), Image.ANTIALIAS)
        self.image_align_justify = ImageTk.PhotoImage(self.photo_align_justify)
        self.align_justify_button.config(image=self.image_align_justify)
        self.align_justify_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # align_left
        self.align_left_button = Button(name="formatbar_b9", borderwidth=1, command=self.align_left, width=20, height=20)

        self.photo_align_left = Image.open(os.path.join(parent_directory, "icons", "align-left.png"))
        self.photo_align_left = self.photo_align_left.resize((18, 18), Image.ANTIALIAS)
        self.image_align_left = ImageTk.PhotoImage(self.photo_align_left)
        self.align_left_button.config(image=self.image_align_left)
        self.align_left_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # align_right
        self.align_right_button = Button(name="formatbar_b10", borderwidth=1, command=self.align_right, width=20, height=20)

        self.photo_align_right = Image.open(os.path.join(parent_directory, "icons", "align-right.png"))
        self.photo_align_right = self.photo_align_right.resize((18, 18), Image.ANTIALIAS)
        self.image_align_right = ImageTk.PhotoImage(self.photo_align_right)
        self.align_right_button.config(image=self.image_align_right)
        self.align_right_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

        # STATUS BAR
        self.status = tk.Label(self.master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)

        # CREATING TEXT AREA - FIRST CREATED A FRAME AND THEN APPLIED TEXT OBJECT TO IT.
        self.text_frame = Frame(self.master, borderwidth=1, relief="sunken")
        self.text = tk.Text(wrap="word", font=("Liberation Mono", 12), background="white", borderwidth=0, highlightthickness=0,
                    undo=True)
        self.text.pack(in_=self.text_frame, side="left", fill="both", expand=True)  # pack text object.

        # PACK TOOLBAR, FORMATBAR, STATUSBAR AND TEXT FRAME.
        self.toolbar.pack(side="top", fill="x")
        self.formattingbar.pack(side="top", fill="x")
        self.status.pack(side="bottom", fill="x")
        self.text_frame.pack(side="bottom", fill="both", expand=True)
        self.text.focus_set()

        # MENUBAR CREATION

        self.menu = tk.Menu(self.master)
        # self.master.config(menu=self.menu)

        # File menu.
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu, underline=0)

        self.file_menu.add_command(label="New", command=self.new, compound='left', image=self.image_new, accelerator='Ctrl+N',
                              underline=0)  # command passed is here the method defined above.
        self.file_menu.add_command(label="Open", command=self.open_file, compound='left', image=self.image_open, accelerator='Ctrl+O',
                              underline=0)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save, compound='left', image=self.image_save, accelerator='Ctrl+S',
                              underline=0)
        self.file_menu.add_command(label="Save As", command=self.save_as, accelerator='Ctrl+Shift+S', underline=1)
        self.file_menu.add_command(label="Rename", command=self.rename, accelerator='Ctrl+Shift+R', underline=0)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close", command=self.close, accelerator='Alt+F4', underline=0)

        # Edit Menu.
        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu, underline=0)

        self.edit_menu.add_command(label="Undo", command=self.undo, compound='left', image=self.image_undo, accelerator='Ctrl+Z',
                              underline=0)
        self.edit_menu.add_command(label="Redo", command=self.redo, compound='left', image=self.image_redo, accelerator='Ctrl+Y',
                              underline=0)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut, compound='left', image=self.image_cut, accelerator='Ctrl+X',
                              underline=0)
        self.edit_menu.add_command(label="Copy", command=self.copy, compound='left', image=self.image_copy, accelerator='Ctrl+C',
                              underline=1)
        self.edit_menu.add_command(label="Paste", command=self.paste, compound='left', image=self.image_paste, accelerator='Ctrl+P',
                              underline=0)
        self.edit_menu.add_command(label="Delete", command=self.delete, underline=0)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all, accelerator='Ctrl+A', underline=0)
        self.edit_menu.add_command(label="Clear All", command=self.delete_all, underline=6)

        # Tool Menu
        self.tool_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Tools", menu=self.tool_menu, underline=0)

        self.tool_menu.add_command(label="Change Color", command=self.change_color)
        self.tool_menu.add_command(label="Search", command=self.find_text, compound='left', image=self.image_find,
                              accelerator='Ctrl+F')

        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu, underline=0)
        self.help_menu.add_command(label="About", command=self.about, accelerator='Ctrl+H', underline=0)

        # ----- BINDING ALL KEYBOARD SHORTCUTS ---------- #
        self.text.bind('<Control-n>', self.new)
        self.text.bind('<Control-N>', self.new)

        self.text.bind('<Control-o>', self.open_file)
        self.text.bind('<Control-O>', self.open_file)

        self.text.bind('<Control-s>', self.save)
        self.text.bind('<Control-S>', self.save)

        self.text.bind('<Control-Shift-s>', self.save_as)
        self.text.bind('<Control-Shift-S>', self.save_as)

        self.text.bind('<Control-r>', self.rename)
        self.text.bind('<Control-R>', self.rename)

        self.text.bind('<Alt-F4>', self.close)
        self.text.bind('<Alt-F4>', self.close)

        self.text.bind('<Control-x>', self.cut)
        self.text.bind('<Control-X>', self.cut)

        self.text.bind('<Control-c>', self.copy)
        self.text.bind('<Control-C>', self.copy)

        self.text.bind('<Control-p>', self.paste)
        self.text.bind('<Control-P>', self.paste)

        self.text.bind('<Control-a>', self.select_all)
        self.text.bind('<Control-A>', self.select_all)

        self.text.bind('<Control-h>', self.about)
        self.text.bind('<Control-H>', self.about)

        self.text.bind('<Control-f>', self.find_text)
        self.text.bind('<Control-F>', self.find_text)

        self.text.bind('<Control-Shift-i>', self.italic)
        self.text.bind('<Control-Shift-I>', self.italic)

        self.text.bind('<Control-b>', self.bold)
        self.text.bind('<Control-B>', self.bold)

        self.text.bind('<Control-u>', self.underline)
        self.text.bind('<Control-U>', self.underline)

        self.text.bind('<Control-Shift-l>', self.align_left)
        self.text.bind('<Control-Shift-L>', self.align_left)

        self.text.bind('<Control-Shift-r>', self.align_right)
        self.text.bind('<Control-Shift-R>', self.align_right)

        self.text.bind('<Control-Shift-c>', self.align_center)
        self.text.bind('<Control-Shift-C>', self.align_center)



        self.new_button.bind("<Enter>", lambda event, str="New, Command - Ctrl+N": self.on_enter(event, str))
        self.new_button.bind("<Leave>", self.on_leave)

        self.save_button.bind("<Enter>", lambda event, str="Save, Command - Ctrl+S": self.on_enter(event, str))
        self.save_button.bind("<Leave>", self.on_leave)

        self.open_button.bind("<Enter>", lambda event, str="Open, Command - Ctrl+O": self.on_enter(event, str))
        self.open_button.bind("<Leave>", self.on_leave)

        self.copy_button.bind("<Enter>", lambda event, str="Copy, Command - Ctrl+C": self.on_enter(event, str))
        self.copy_button.bind("<Leave>", self.on_leave)

        self.cut_button.bind("<Enter>", lambda event, str="Cut, Command - Ctrl+X": self.on_enter(event, str))
        self.cut_button.bind("<Leave>", self.on_leave)

        self.paste_button.bind("<Enter>", lambda event, str="Paste, Command - Ctrl+P": self.on_enter(event, str))
        self.paste_button.bind("<Leave>", self.on_leave)

        self.undo_button.bind("<Enter>", lambda event, str="Undo, Command - Ctrl+Z": self.on_enter(event, str))
        self.undo_button.bind("<Leave>", self.on_leave)

        self.redo_button.bind("<Enter>", lambda event, str="Redo, Command - Ctrl+Y": self.on_enter(event, str))
        self.redo_button.bind("<Leave>", self.on_leave)

        self.find_button.bind("<Enter>", lambda event, str="Find, Command - Ctrl+F": self.on_enter(event, str))
        self.find_button.bind("<Leave>", self.on_leave)

        self.bold_button.bind("<Enter>", lambda event, str="Bold, Command - Ctrl+B": self.on_enter(event, str))
        self.bold_button.bind("<Leave>", self.on_leave)

        self.italic_button.bind("<Enter>", lambda event, str="Italic, Command - Ctrl+Shift+I": self.on_enter(event, str))
        self.italic_button.bind("<Leave>", self.on_leave)

        self.underline_button.bind("<Enter>", lambda event, str="Underline, Command - Ctrl+U": self.on_enter(event, str))
        self.underline_button.bind("<Leave>", self.on_leave)

        self.align_justify_button.bind("<Enter>", lambda event, str="Justify": self.on_enter(event, str))
        self.align_justify_button.bind("<Leave>", self.on_leave)

        self.align_left_button.bind("<Enter>",
                               lambda event, str="Align Left, Command - Control-Shift-L": self.on_enter(event, str))
        self.align_left_button.bind("<Leave>", self.on_leave)

        self.align_right_button.bind("<Enter>",
                                lambda event, str="Align Right, Command - Control-Shift-R": self.on_enter(event, str))
        self.align_right_button.bind("<Leave>", self.on_leave)

        self.align_center_button.bind("<Enter>",
                                 lambda event, str="Align Center, Command - Control-Shift-C": self.on_enter(event, str))
        self.align_center_button.bind("<Leave>", self.on_leave)

        self.strike_button.bind("<Enter>", lambda event, str="Strike": self.on_enter(event, str))
        self.strike_button.bind("<Leave>", self.on_leave)

        self.font_color_button.bind("<Enter>", lambda event, str="Font Color": self.on_enter(event, str))
        self.font_color_button.bind("<Leave>", self.on_leave)

        self.highlight_button.bind("<Enter>", lambda event, str="Highlight": self.on_enter(event, str))
        self.highlight_button.bind("<Leave>", self.on_leave)

        self.strike_button.bind("<Enter>", lambda event, str="Strike": self.on_enter(event, str))
        self.strike_button.bind("<Leave>", self.on_leave)


    # Help Menu
    def about(self, event=None):
        messagebox.showinfo("About",
                            "Text Editor\nCreated in Python using Tkinter\nCopyright with Amandeep and Harmanpreet, 2017")

    # ---------- SETTING EVENTS FOR THE STATUS BAR -------------- #
    def on_enter(self, event, str):
        self.status.configure(text=str)

    def on_leave(self, event):
        self.status.configure(text="")

    def make_tag(self):
        current_tags = self.text.tag_names()
        if "bold" in current_tags:
            weight = "bold"
        else:
            weight = "normal"

        if "italic" in current_tags:
            slant = "italic"
        else:
            slant = "roman"

        if "underline" in current_tags:
            underline = 1
        else:
            underline = 0

        if "overstrike" in current_tags:
            overstrike = 1
        else:
            overstrike = 0

        big_font = font.Font(self.text, self.text.cget("font"))
        big_font.configure(slant=slant, weight=weight, underline=underline, overstrike=overstrike,
                           family=current_font_family, size=current_font_size)
        self.text.tag_config("BigTag", font=big_font, foreground=fontColor, background=fontBackground)
        if "BigTag" in current_tags:
            self.text.tag_remove("BigTag", 1.0, tk.END)
        self.text.tag_add("BigTag", 1.0, tk.END)

    def new(self, event=None):
        file_name = ""
        ans = messagebox.askquestion(title="Save File", message="Would you like to save this file")
        if ans is True:
            self.save()
        self.delete_all()

    def open_file(self, event=None):
        self.new()

        file = filedialog.askopenfile()
        global file_name
        file_name = file.name
        self.text.insert(tk.INSERT, file.read())

    def save(self, event=None):
        global file_name
        if file_name == "":
            path = filedialog.asksaveasfilename()
            file_name = path
        self.master.title(file_name + " - Script Editor")
        write = open(file_name, mode='w')
        write.write(self.text.get("1.0", tk.END))

    def save_as(self, event=None):
        if file_name == "":
            self.save()
            return "break"
        f = filedialog.asksaveasfile(mode='w')
        if f is None:
            return
        text2save = str(self.text.get(1.0, tk.END))
        f.write(text2save)
        f.close()

    new_name = ""  # Used for renaming the file

    def rename(self, event=None):
        global file_name
        if file_name == "":
            self.open_file()

        arr = file_name.split('/')
        path = ""
        for i in range(0, len(arr) - 1):
            path = path + arr[i] + '/'

        new_name = simpledialog.askstring("Rename", "Enter new name")
        os.rename(file_name, str(path) + str(new_name))
        file_name = str(path) + str(new_name)
        self.master.title(file_name + " - Script Editor")

    def close(self, event=None):
        self.save()
        self.master.quit()

    # EDIT MENU METHODS

    def cut(self, event=None):
        # first clear the previous text on the clipboard.
        self.master.clipboard_clear()
        self.text.clipboard_append(string=self.text.selection_get())
        # index of the first and yhe last letter of our selection.
        self.text.delete(index1=tk.SEL_FIRST, index2=tk.SEL_LAST)

    def copy(self, event=None):
        # first clear the previous text on the clipboard.
        print(self.text.index(tk.SEL_FIRST))
        print(self.text.index(tk.SEL_LAST))
        self.master.clipboard_clear()
        self.text.clipboard_append(string=self.text.selection_get())

    def paste(self, event=None):
        # get gives everyting from the clipboard and paste it on the current cursor position
        # it does'nt removes it from the clipboard.
        self.text.insert(tk.INSERT, self.master.clipboard_get())

    def delete(self):
        self.text.delete(index1=tk.SEL_FIRST, index2=tk.SEL_LAST)

    def undo(self):
        self.text.edit_undo()

    def redo(self):
        self.text.edit_redo()

    def select_all(self,event=None):

        self.text.tag_add(tk.SEL, "1.0", tk.END)

    def delete_all(self):
        self.text.delete(1.0, tk.END)

    # TOOLS MENU METHODS

    def change_color(self):
        color = colorchooser.askcolor(initialcolor='#ff0000')
        color_name = color[1]
        global fontColor
        fontColor = color_name
        current_tags = self.text.tag_names()
        if "font_color_change" in current_tags:
            # first char is bold, so unbold the range
            self.text.tag_delete("font_color_change", 1.0, tk.END)
        else:
            # first char is normal, so bold the whole selection
            self.text.tag_add("font_color_change", 1.0, tk.END)
        self.make_tag()

    # Adding Search Functionality

    def check(self,value):
        self.text.tag_remove('found', '1.0', tk.END)
        self.text.tag_config('found', foreground='red')
        list_of_words = value.split(' ')
        for word in list_of_words:
            idx = '1.0'
            while idx:
                idx = self.text.search(word, idx, nocase=1, stopindex=tk.END)
                if idx:
                    lastidx = '%s+%dc' % (idx, len(word))
                    self.text.tag_add('found', idx, lastidx)
                    print
                    lastidx
                    idx = lastidx

    # implementation of search dialog box - calling the check method to search and find_text_cancel_button to close it
    def find_text(self,event=None):

        search_toplevel = tk.Toplevel(self.master)
        search_toplevel.title('Find Text')
        search_toplevel.transient(self.master)
        search_toplevel.resizable(False, False)
        tk.Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
        search_entry_widget = tk.Entry(search_toplevel, width=25)
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        search_entry_widget.focus_set()
        Button(search_toplevel, text="Ok", underline=0, command=lambda: self.check(search_entry_widget.get())).grid(
            row=0, column=2, sticky='e' + 'w', padx=2, pady=5)
        Button(search_toplevel, text="Cancel", underline=0,
               command=lambda: self.find_text_cancel_button(search_toplevel)).grid(row=0, column=4, sticky='e' + 'w',
                                                                              padx=2, pady=2)

    # remove search tags and destroys the search box
    def find_text_cancel_button(self,search_toplevel):
        self.text.tag_remove('found', '1.0', tk.END)
        search_toplevel.destroy()
        return "break"

    # FORMAT BAR METHODS

    def bold(self,event=None):
        current_tags = self.text.tag_names()
        if "bold" in current_tags:
            # first char is bold, so unbold the range
            self.text.tag_delete("bold", 1.0, tk.END)
        else:
            # first char is normal, so bold the whole selection
            self.text.tag_add("bold", 1.0, tk.END)
        self.make_tag()

    def italic(self,event=None):
        current_tags = self.text.tag_names()
        if "italic" in current_tags:
            self.text.tag_add("roman", 1.0, tk.END)
            self.text.tag_delete("italic", 1.0, tk.END)
        else:
            self.text.tag_add("italic", 1.0, tk.END)
        self.make_tag()

    def underline(self,event=None):
        current_tags = self.text.tag_names()
        if "underline" in current_tags:
            self.text.tag_delete("underline", 1.0, tk.END)
        else:
            self.text.tag_add("underline", 1.0, tk.END)
        self.make_tag()

    def strike(self):
        current_tags = self.text.tag_names()
        if "overstrike" in current_tags:
            self.text.tag_delete("overstrike", "1.0", tk.END)

        else:
            self.text.tag_add("overstrike", 1.0, tk.END)

        self.make_tag()

    def highlight(self):
        color = colorchooser.askcolor(initialcolor='white')
        color_rgb = color[1]
        global fontBackground
        fontBackground = color_rgb
        current_tags = self.text.tag_names()
        if "background_color_change" in current_tags:
            self.text.tag_delete("background_color_change", "1.0", tk.END)
        else:
            self.text.tag_add("background_color_change", "1.0", tk.END)
        self.make_tag()

    # To make align functions work properly
    def remove_align_tags(self):
        all_tags = self.text.tag_names(index=None)
        if "center" in all_tags:
            self.text.tag_remove("center", "1.0", tk.END)
        if "left" in all_tags:
            self.text.tag_remove("left", "1.0", tk.END)
        if "right" in all_tags:
            self.text.tag_remove("right", "1.0", tk.END)

    # align_center
    def align_center(self,event=None):
        self.remove_align_tags()
        self.text.tag_configure("center", justify='center')
        self.text.tag_add("center", 1.0, "end")

    # align_justify
    def align_justify(self):
        self.remove_align_tags()

    # align_left
    def align_left(self,event=None):
        self.remove_align_tags()
        self.text.tag_configure("left", justify='left')
        self.text.tag_add("left", 1.0, "end")

    # align_right
    def align_right(self,event=None):
        self.remove_align_tags()
        self.text.tag_configure("right", justify='right')
        self.text.tag_add("right", 1.0, "end")

    # Font and size change functions - BINDED WITH THE COMBOBOX SELECTION
    # change font and size are methods binded with combobox, calling fontit and sizeit
    # called when <<combobox>> event is called

    def change_font(self,event):
        f = self.all_fonts.get()
        global current_font_family
        current_font_family = f
        self.make_tag()

    def change_size(self,event):
        sz = int(self.all_size.get())
        global current_font_size
        current_font_size = sz
        self.make_tag()



    def show(self):
        self.master.pack(fill='both')

    def hide(self):
        self.master.pack_forget()