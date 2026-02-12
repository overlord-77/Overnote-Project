import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
# import ttkbootstrap as ttb
# from ttkbootstrap.toast import ToastNotification

"""
Overnote version 0.1

"""

class MainApp(ctk.CTk):
    def __init__(self, title, size):

        # Main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')

        # main frame widget - all widgets will be stored inside of it.
        main_frame_widget = MainFrameWidget(self)

        # Run the app
        self.mainloop()

class MainFrameWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand = True, fill='both')

        # main widgets
        main_text_area = MainTextArea(self)
        main_option_bar = MainOptionsBar(self)

class MainTextArea(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)
                        
        self.pack(expand = True, fill = 'both', side='bottom')

        # Example: Apply default styling
        self.configure(
            wrap="word",       # Wrap text at word boundaries
            bg="#1e1e1e",      # Dark background
            fg="#ffffff",      # White text
            insertbackground="white",  # White cursor
            foreground='darkgoldenrod', 
            highlightbackground='darkgray', 
            highlightthickness=3, 
            selectbackground = 'grey', 
            font=('Arial', 17))
        
        # scrollbar
        self.scrollbar = ctk.CTkScrollbar(self, command= self.yview)

        self.configure(yscrollcommand= self.scrollbar.set)
        self.scrollbar.place(relx= 1, rely= 0, relheight= 1, anchor= 'ne')    

class MainOptionsBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand = True, fill='both')

        left_option_bar = LeftOptionsBar(self)
        
class LeftOptionsBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="left")

        left_option_bar_menu = tk.Menu(self)
        file_menu = File_Menu(left_option_bar_menu)
        left_option_bar_menu.add_cascade(label='File')
        # left_option_bar_menu.add_cascade(label='File', menu=file_menu)
        left_option_bar_menu.add_cascade(label='Edit')
        left_option_bar_menu.add_cascade(label='View')

        left_option_bar_menu.add_cascade(label='H1')
        left_option_bar_menu.add_cascade(label='☰')
        left_option_bar_menu.add_cascade(label='𝐁')
        left_option_bar_menu.add_cascade(label='𝐼')
        left_option_bar_menu.add_cascade(label='🔗')
        left_option_bar_menu.add_cascade(label='🅰️⌫')
        
        left_option_bar_menu.add_cascade(label='⚙️')

        # Apply menu bar to the top-level window, not this frame
        self.winfo_toplevel().config(menu=left_option_bar_menu)

class File_Menu(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(parent, tearoff=False)
        self.add_cascade(label='New Tab')

MainApp('OverNote', (1400,700) )