import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import os, sys
import pyautogui
import time
import win32print
import win32ui


try: 
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

"""
Overnote version 1.1 on Branch -> Exe <- From Branch -> Main <-

"""
class MainApp(ctk.CTk):
    def __init__(self, title, size):

        # Main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        
        # Change title bar color
        self.change_title_bar_color()

        # Load and set the icon safely (works for PyInstaller and normal run)
        icon_path = self.resource_path("D:/X-OneDrive/Python/- Python Scripts - Projects  -/Overnote/Overnote - ver.1.1/assets/o_icon.ico") #------------------------------> Un-comment once turning it into an exe | re comment it once being updates 
        self.iconbitmap(icon_path)

        # main frame widget - all widgets will be stored inside of it.
        self.main_frame_widget = MainFrameWidget(self)

        # Run the app
        self.mainloop()

    def change_title_bar_color(self):
        # change the color of the title bar
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = 0x00111111

            windll.dwmapi.DwmSetWindowAttribute(
                HWND, 
                DWMWA_ATTRIBUTE, 
                byref(c_int(COLOR)),
                sizeof(c_int)
            )
        except:
            pass

    def resource_path(self, relative_path):
        """Get the absolute path to the resource (works for PyInstaller and normal Python)."""
        try:
            # PyInstaller stores files in a temporary folder called _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

class MainFrameWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand = True, fill='both')

        # main widgets
        self.main_option_bar = MainOptionsBar(self)

class MainTextArea(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)
                        
        self.grid(column = 0, row = 2, columnspan = 3, sticky = 'nwse', padx=0, pady=0)

        # Example: Apply default styling
        self.configure(
            wrap="word",       # Wrap text at word boundaries
            bg="#272727",      # Dark background
            fg="#ffffff",      # White text
            insertbackground="white",  # White cursor
            foreground='white', 
            highlightbackground='darkgray', 
            highlightthickness=3, 
            selectbackground = "#85c1ef", 
            font=('Calibri', 17))
    
        # scrollbar
        self.scrollbar = ctk.CTkScrollbar(self, command= self.yview)

        self.configure(yscrollcommand= self.scrollbar.set)
        self.scrollbar.place(relx= 1, rely= 0, relheight= 1, anchor= 'ne')    

class MainOptionsBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= '#202022')
        self.pack(expand = True, fill='both')

        frame_to_hold = ctk.CTkFrame(self, fg_color= '#202022')
        frame_to_hold.pack(expand = True, fill = 'both')

        self.main_text_area = MainTextArea(frame_to_hold)
        self.tab_system_frame = TabSystemFrame(frame_to_hold, self.main_text_area)
        self.status_bar_frame = StatusBarFrame(frame_to_hold, self.main_text_area)

        # layout
        frame_to_hold.columnconfigure((0,1,2), weight=1)
        frame_to_hold.rowconfigure((0,1,2,3), weight=1)

        self.left_option_bar = LeftOptionsBar(frame_to_hold,  self.status_bar_frame, self.tab_system_frame)
        self.center_option_bar = CenterOptionsBar(frame_to_hold)
        self.right_option_bar = RightOptionsBar(frame_to_hold)
        
class LeftOptionsBar(ctk.CTkFrame):
    def __init__(self, parent, status_bar_frame, tab_system_frame):
        super().__init__(parent, fg_color= '#202022')
        self.grid(column = 0, row = 0, sticky = 'w', padx=0, pady=0)

        # File Menubutton ----------------------
        file_menubutton = tk.Menubutton(self, text="File", bg="#202022", fg="white", relief="flat", activebackground = '#333333', activeforeground= 'white')
        file_menubutton.pack(side="left", padx=2, pady=2)
        file_menu = File_Menu(file_menubutton, tab_system_frame)

        # Attach menu to the button
        file_menubutton.config(menu=file_menu)

        # Edit Menubutton ----------------------
        edit_menubutton = tk.Menubutton(self, text="Edit", bg="#202022", fg="white", relief="flat", activebackground = '#333333', activeforeground= 'white')
        edit_menubutton.pack(side="left", padx=2, pady=2)
        edit_menu = Edit_Menu(edit_menubutton)

        # Attach menu to the button
        edit_menubutton.config(menu=edit_menu)

        # View Menubutton ----------------------
        view_menubutton = tk.Menubutton(self, text="View", bg="#202022", fg="white", relief="flat", activebackground = '#333333', activeforeground= 'white')
        view_menubutton.pack(side="left", padx=2, pady=2)
        view_menu = View_Menu(view_menubutton, status_bar_frame)

        # Attach menu to the button
        view_menubutton.config(menu=view_menu)

class CenterOptionsBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= '#202022')
        self.grid(column = 1, row = 0, padx=0, pady=0)

        # Heading Menubutton ----------------------
        heading_menubutton = tk.Menubutton(self, text="H1", bg="#202022", fg="white", relief="flat", activebackground = '#333333', activeforeground= 'white')
        heading_menubutton.pack(side="left", padx=2, pady=2)
        heading_tab = Heading_Tab(heading_menubutton)

        # Attach menu to the button
        heading_menubutton.config(menu=heading_tab)

        # List Type Menubutton ----------------------
        list_type_menubutton = tk.Menubutton(self, text="☰", bg="#202022", fg="white", relief="flat", activebackground = '#333333', activeforeground= 'white')
        list_type_menubutton.pack(side="left", padx=2, pady=2)
        list_type_tab = List_Type_Tab(list_type_menubutton)

        # Attach menu to the button
        list_type_menubutton.config(menu=list_type_tab)

        # Bold Text Checkbutton ----------------------
        is_bold = tk.BooleanVar(value=False)
        def toggle_bold():
            if is_bold.get():
                bold_text_checkbutton.config(fg="#ff4d6d", selectcolor= '#333333', relief="sunken", bg="#202022", activebackground="#202022")
            else:
                bold_text_checkbutton.config(fg="#bfbfbf", relief="flat", bg="#202022", activebackground="#202022")

        bold_text_checkbutton = tk.Checkbutton(
            self,
            text="𝐁",
            font=("Segoe UI", 14),
            variable=is_bold,
            onvalue=True,
            offvalue=False,
            indicatoron=False,
            width=3,
            height=1,
            bg="#202022",           # default bg
            fg="#bfbfbf",           # default gray text
            activebackground="#202022",  # prevent white flash
            activeforeground="#ff4d6d",  # color when hovered
            bd=0,
            relief="flat",
            highlightthickness=0,        # removes border highlight
            overrelief="flat",
            command=toggle_bold)
        bold_text_checkbutton.pack(side="left", padx=2, pady=2)

        # Italic Text Checkbutton ----------------------
        is_italic = tk.BooleanVar(value=False)

        def toggle_italic():
            if is_italic.get():
                italic_text_checkbutton.config(fg="#ff4d6d", relief="flat", selectcolor= '#333333', bg="#202022", activebackground="#202022")
            else:
                italic_text_checkbutton.config(fg="#bfbfbf", relief="flat", bg="#202022", activebackground="#202022")

        italic_text_checkbutton = tk.Checkbutton(
            self,
            text="𝐼",
            font=("Segoe UI", 14),
            variable=is_italic,
            onvalue=True,
            offvalue=False,
            indicatoron=False,
            width=3,
            height=1,
            bg="#202022",           # default bg
            fg="#bfbfbf",           # default gray text
            activebackground="#202022",  # prevent white flash
            activeforeground="#ff4d6d",  # color when hovered
            bd=0,
            relief="flat",
            highlightthickness=0,        # removes border highlight
            overrelief="flat",
            command=toggle_italic)
        italic_text_checkbutton.pack(side="left", padx=2, pady=2)

        # Link Tab Button ----------------------
        is_link_tab = tk.StringVar(value="🔗")

        def toggle_link_tab():
            if is_link_tab.get():
                link_tab = Link_Tab(self)
                link_tab_button.config(
                    fg="#bfbfbf",    # reddish pink
                    selectcolor= '#202022',
                    
                    relief="sunken",
                    bg="#202022",    # lock dark background
                    activebackground="#202022"
                )
        
        link_tab_button = tk.Button(
            self, 
            text="🔗", 
            font=("Segoe UI", 14),
            textvariable = is_link_tab,
            width=3,
            height=1,
            bg="#202022",           # default bg
            fg="#bfbfbf",           # default gray text
            activebackground="#202022",  # prevent white flash
            activeforeground="#ff4d6d",  # color when hovered
            bd=0,
            relief="flat",
            highlightthickness=0,        # removes border highlight
            overrelief="flat",
            command= toggle_link_tab
            )
        link_tab_button.pack(side="left", padx=2, pady=2)

        # Clear Format Button ----------------------
        clearformatt_button = tk.Button(
            self, 
            text= 'C-F', 
            font=("Segoe UI", 14),
            width=3,
            height=1,
            bg="#202022",           # default bg
            fg="#bfbfbf",           # default gray text
            activebackground="#1e1e1e",  # prevent white flash
            activeforeground="#ff4d6d",  # color when hovered
            bd=0,
            relief="flat",
            highlightthickness=0,        # removes border highlight
            overrelief="flat",
            )
        clearformatt_button.pack(side="left", padx=2, pady=2)

class RightOptionsBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= '#202022')
        self.grid(column = 2, row = 0, sticky = 'e', padx=0, pady=0)

        # Settings Winodw Button ----------------------
        is_setting_window = tk.StringVar(value= "⚙️")

        def toggle_setting_window():
            if is_setting_window.get():
                setting_window = Setting_Window(self)
                settings_window_button.config(
                    fg="#bfbfbf",    # reddish pink
                    selectcolor= '#202022',
                    
                    relief="sunken",
                    bg="#202022",    # lock dark background
                    activebackground="#202022"
                )
        
        settings_window_button = tk.Button(
            self, 
            text="⚙️", 
            font=("Segoe UI", 14),
            textvariable =is_setting_window,
            width=3,
            height=1,
            bg="#202022",           # default bg
            fg="#bfbfbf",           # default gray text
            activebackground="#202022",  # prevent white flash
            activeforeground="#ff4d6d",  # color when hovered
            bd=0,
            relief="flat",
            highlightthickness=0,        # removes border highlight
            overrelief="flat",
            command= toggle_setting_window
            )
        settings_window_button.pack(side="left", padx=2, pady=2)

class File_Menu(tk.Menu):
    def __init__(self, parent, tab_system_frame, tearoff=False):
        super().__init__(
            parent, 
            tearoff=False, 
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef'
            
            )
        # Track the current file path globally or inside your class
        self.current_file_path = None
                
        def save_function():
            # If no file yet, ask where to save
            if not self.current_file_path:
                file_path = filedialog.asksaveasfilename(
                    defaultextension='.txt',
                    filetypes=[
                        ('Text Files', '*.txt'),
                        ('All Files', '*.*'),
                        ('Python Files', '*.py'),
                        ('HTML Files', '*.html')
                    ]
                )

                if not file_path:
                    return  # user cancelled

                # Optional: handle auto-rename if file exists
                base, ext = os.path.splitext(file_path)
                count = 2
                while os.path.exists(file_path):
                    file_path = f"{base} ({count}){ext}"
                    count += 1

                self.current_file_path = file_path  # save path for next time

            # Save content to current file
            with open(self.current_file_path, "w", encoding="utf-8") as f:
                content = tab_system_frame.main_text_area.get("1.0", "end-1c")
                f.write(content)
                
        def save_as_function():
            self.current_file_path = filedialog.asksaveasfilename(
                defaultextension = '.txt', filetypes =[('Text Files', '*.txt'), ('All Files', '*.*'), ('Python Files', '*.py'), ('Html Files', '*.html'), ('Css Files', '*.css'), ('JaveScript Files', '*.js')])

            with open(self.current_file_path, 'x', encoding="utf-8") as f:
                content = tab_system_frame.main_text_area.get("1.0", "end-1c")
                f.write(content)

        def open_file_function():
            self.current_file_path = filedialog.askopenfilename()
            
            if self.current_file_path:  # Only proceed if the user selected a file
                file_name = os.path.basename(self.current_file_path)
                # print(self.file_name)
                with open(self.current_file_path, 'r', encoding="utf-8") as file:
                    content = file.read()
                    tab_system_frame.main_text_area.delete("1.0", "end")  # Clear the current text
                    tab_system_frame.main_text_area.insert("1.0", content)  # Insert the file content at the beginning

        def open_new_tap():
            tab_system_frame.initiate_tab()
            
        def page_setup():

            page_setup = ctk.CTkToplevel()
            page_setup.title('Page Setup')
            page_setup.geometry('535x325')
            page_setup.maxsize(width=535, height=325)
            page_setup.minsize(width=535, height=325)
            page_setup.attributes("-topmost", True)

            widget_holder = ctk.CTkFrame(page_setup)
            widget_holder.pack(expand = True, fill = 'both')  
 
            widget_holder.rowconfigure(0, weight = 1, uniform = 't')
            widget_holder.columnconfigure((0,1,2), weight = 1, uniform = 't')

            widget_frame_1 = ctk.CTkFrame(widget_holder)
            widget_frame_1.grid(row = 0, column = 0, columnspan = 3, sticky = 'nswe')

            widget_frame_1.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 10, uniform = 'a')
            widget_frame_1.columnconfigure((0,1), weight = 1, uniform = 'a')

            widget_frame_2 = ctk.CTkFrame(widget_holder)
            widget_frame_2.grid(row = 0, column = 2, sticky = 'nswe')

            widget_frame_2.rowconfigure((0,1,2), weight = 1, uniform = 'c')
            widget_frame_2.columnconfigure(0, weight = 1, uniform = 'c')


            paper_label = ctk.CTkLabel(widget_frame_1, text= 'Paper')
            paper_label.grid(row = 0, column = 0, sticky = 'w', padx = 10)

            size_label = ctk.CTkLabel(widget_frame_1, text= 'Size')
            size_label.grid(row = 1, column = 0, sticky = 'w', padx = 10)

            size_optionmenu = ctk.CTkOptionMenu(widget_frame_1, values = ['Select', 'one', 'two', 'three'])
            size_optionmenu.grid(row = 1, column = 0, sticky = 'e')

            source_label = ctk.CTkLabel(widget_frame_1, text= 'Source')
            source_label.grid(row = 2, column = 0, sticky = 'w', padx = 10)

            source_optionmenu = ctk.CTkOptionMenu(widget_frame_1, values = ['Select', 'one', 'two', 'three'])
            source_optionmenu.grid(row = 2, column = 0, sticky = 'e')

            orientation_margin_frame = ctk.CTkFrame(widget_frame_1)
            orientation_margin_frame.grid(row = 3, column = 0, columnspan = 2, sticky = 'nswe')

            orientation_margin_frame.rowconfigure((0,1,2), weight = 1, uniform = 'b')
            orientation_margin_frame.columnconfigure((0,1), weight = 1, uniform = 'b') 

            orientation_label = ctk.CTkLabel(orientation_margin_frame, text= 'Orientation')
            orientation_label.grid(row = 0, column = 0, sticky = 'w', padx = 10)

            portrait_radio_button = ctk.CTkRadioButton(orientation_margin_frame, text = 'Portrait')
            portrait_radio_button.grid(row = 1, column = 0, sticky = 'w', padx = 10)

        def print_page():

            print_page_toplevel = ctk.CTkToplevel()
            print_page_toplevel.title('Print Page')
            print_page_toplevel.geometry('850x700')
            print_page_toplevel.maxsize(width=850, height=700)
            print_page_toplevel.minsize(width=850, height=700)
            print_page_toplevel.attributes("-topmost", True)

            print_page_frame_holder = ctk.CTkFrame(print_page_toplevel)
            print_page_frame_holder.pack(expand = True, fill = 'both', side = 'left')

            printer_lable = ctk.CTkLabel(print_page_frame_holder, text= "Printer", font=('Arial', 21))
            printer_lable.pack()

            printer_message_lable = ctk.CTkLabel(print_page_frame_holder, text= "Currently, only print into pdf", font=('Arial', 15))
            printer_message_lable.pack()

            buttom_frame = ctk.CTkFrame(print_page_frame_holder)
            buttom_frame.pack(expand = True, fill = 'x', side = 'bottom')

            message_at_bottom = ctk.CTkLabel(buttom_frame, text='Printing to pdf only (For now)')
            message_at_bottom.pack(side = 'left', padx = 100)

            def print_func():

                printer_name = win32print.GetDefaultPrinter()

                # Create a printer device context
                hDC = win32ui.CreateDC()
                hDC.CreatePrinterDC(printer_name)

                # Start a print job
                hDC.StartDoc("Python Direct Print")
                hDC.StartPage()

                text_content = tab_system_frame.main_text_area.get("1.0", "end-1c")  # get all text

                # Print some text at position (x=100, y=100)
                hDC.TextOut(100, 100, text_content)

                # End the page and document
                hDC.EndPage()
                hDC.EndDoc()
                hDC.DeleteDC()

            print_button = ctk.CTkButton(buttom_frame, text='Print', command= print_func)
            print_button.pack(side = 'left', padx = 10)

            cancel_print_button = ctk.CTkButton(buttom_frame, text='Cancel', command= lambda: print_page_toplevel.destroy())
            cancel_print_button.pack(side = 'left')

        self.add_cascade(label='New Tab', command = open_new_tap)
        self.add_cascade(label='New Window', command= lambda: MainApp('OverNote', (1400,800)))
        self.add_cascade(label='New Markdown Tab')
        self.add_cascade(label='Open', command = open_file_function)
        self.add_cascade(label='Recent')
        self.add_cascade(label='Save', command= save_function)        
        # Bind Ctrl+S to allow saving using keyboard
        self.bind_all("<Control-s>", lambda event: save_function())

        self.add_cascade(label='Save As', command = save_as_function)
        self.add_cascade(label='Save All')
        self.add_separator()
        self.add_cascade(label='Page Setup', command = page_setup)
        self.add_cascade(label='Print', command = print_page)
        self.add_separator()
        def destory_a_tab():
                if tab_system_frame.tab_count:
                    tab_system_frame.tab_button.pack_forget()
                
        self.add_cascade(label='Close Tab', command= destory_a_tab)
        self.add_cascade(label='Close Window', command= lambda: self.quit())
        self.add_cascade(label='Exit', command= lambda: self.quit())

class Edit_Menu(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(
            parent, 
            tearoff=False,
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef')

        self.add_cascade(label='Undo')
        self.add_separator()
        self.add_cascade(label='Cut')
        self.add_cascade(label='Copy')
        self.add_cascade(label='Paste')
        self.add_cascade(label='Delete')
        self.add_separator()
        self.add_cascade(label='Clear Formatting')
        self.add_separator()
        self.add_cascade(label='Find')
        self.add_cascade(label='Find Next')
        self.add_cascade(label='Find Previous')
        self.add_cascade(label='Replace')
        self.add_cascade(label='Go To')
        self.add_separator()
        self.add_cascade(label='Select All')
        self.add_cascade(label='Time/Date')
        self.add_separator()
        self.add_cascade(label='Font')

class View_Menu(tk.Menu):
    def __init__(self, parent, status_bar_frame, tearoff=False):
        super().__init__(
            parent, 
            tearoff=False, 
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef')
        
        self.status_bar_frame = status_bar_frame

        # Zoom Submenu
        zoom_submenu = tk.Menu(
            tearoff=False, 
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef')
        zoom_submenu.add_cascade(label='Zoom In')
        zoom_submenu.add_cascade(label='Zoom Out')
        zoom_submenu.add_cascade(label='Zoom Restore default zoom')

        # Markdown Submenu
        markdown_submenu= tk.Menu(
            tearoff=False, 
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef')
        markdown_submenu.add_cascade(label='Formatted')
        markdown_submenu.add_cascade(label='Syntax')

        self.add_cascade(label='Zoom', menu= zoom_submenu)

        def status_bar_func():
            if status_bar_var.get() == "on":
                self.status_bar_frame.main_status_frame.pack(expand = False, fill='x', side= 'bottom')
    
            else:
                self.status_bar_frame.main_status_frame.pack_forget()

        status_bar_var = tk.StringVar(value='on')

        self.add_checkbutton(
            label='Status Bar', 
            command= status_bar_func, 
            offvalue = 'off',
            onvalue = 'on', 
            variable= status_bar_var, 
            state= 'active', 
            selectcolor='#FF5D5D')
        
        self.add_cascade(label='Word Wrap')
        self.add_cascade(label='Markdown', menu= markdown_submenu)

class ShowRecentList(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(
            parent, 
            tearoff=False, 
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef')

class Heading_Tab(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(
            parent, 
            tearoff=False, 
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef')

        self.add_cascade(label='Title', font= ('Arial', 30))
        self.add_cascade(label='Subtitle', font= ('Arial', 27))
        self.add_cascade(label='Heading', font= ('Arial', 24))
        self.add_cascade(label='Subheading', font= ('Arial', 21))

        self.add_cascade(label='Section', font= ('Arial', 18))
        self.add_cascade(label='Subsection', font= ('Arial', 15))
        self.add_cascade(label='Body', font= ('Arial', 12))

class List_Type_Tab(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(
            parent, 
            tearoff=False, 
            activebackground= "#FF5D5D", 
            activeforeground="#130F0F", 
            bg='black', 
            fg='#85c1ef')

        self.add_cascade(label='Bulleted List')
        self.add_cascade(label='Numbered Lis')

class Link_Tab(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('350x350')
        self.maxsize(width=350, height=350)
        self.minsize(width=350, height=350)

        w, h = 350, 350
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

        self.overrideredirect(True)   # removes title bar (X, minimize, maximize)

        frame = ctk.CTkFrame(self, width= 400, height=300)
        frame.pack(expand = True, fill= 'both')

        frame.grid_columnconfigure(0, weight=1)  # left column
        frame.grid_rowconfigure((0,1,2,3,4), weight=1, pad=0)  # Row

        label_link = ctk.CTkLabel(frame, text= 'Link', font= ("Arial", 24))
        label_link.grid(row=0, column=0, sticky="w", pady=5, padx= 20)

        label_display = ctk.CTkLabel(frame, text= 'Display Text', font= ("Arial", 17))
        label_display.grid(row=1, column=0, sticky="w", pady=1, padx= 20)

        entry_widget = ctk.CTkEntry(frame, placeholder_text= 'Text for the link (optional)')
        entry_widget.grid(row=2, column=0, sticky="we", pady=1, padx= 20)

        entry_widget.bind('<FocusIn>', lambda event: entry_widget.configure(border_color='#FF8383'))
        entry_widget.bind('<FocusOut>', lambda event: entry_widget.configure(border_color="#474141"))

        label_address = ctk.CTkLabel(frame, text= 'Address', font= ("Arial", 17))
        label_address.grid(row=3, column=0, sticky="w", pady=1, padx= 20)

        entry_widget2 = ctk.CTkEntry(frame, placeholder_text="Link to an existing webpage")
        entry_widget2.grid(row=4, column=0, sticky="we", pady=1, padx= 20)
        entry_widget2.bind('<FocusIn>', lambda event: entry_widget2.configure(border_color='#FF8383'))
        entry_widget2.bind('<FocusOut>', lambda event: entry_widget2.configure(border_color="#474141"))

        frame4 = ctk.CTkFrame(self, fg_color="#272626")
        frame4.pack(expand= True, fill='both')

        frame4.grid_columnconfigure((0,1), weight=1)  # left column
        frame4.grid_rowconfigure((0), weight=1)  # Row

        button = ctk.CTkButton(frame4, text= 'Insert', fg_color= "#FF8383", text_color='black', hover_color= "#BB6D6D")
        button.grid(row=0, column=0, sticky="e", pady=3, padx= 10)

        def exit_link_widget():
            top = self.winfo_toplevel()  # get the Toplevel window
            top.destroy()

        button2 = ctk.CTkButton(frame4, text= 'Cancel', fg_color= "#393838", hover_color= "#525050", command= exit_link_widget)
        button2.grid(row=0, column=1, sticky="w", pady=3)

class Setting_Window(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Setting")
        self.geometry('1200x700')
        self.attributes("-topmost", True)   # always on top

        w, h = 1200, 700
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

        setting_label_frame = ctk.CTkFrame(self, fg_color= '#202020')
        setting_label_frame.pack(fill = 'x')

        setting_label = ctk.CTkLabel(setting_label_frame, text= 'Settings', font= ('Arial', 27))
        setting_label.pack(side = 'left', pady = 15, padx = 30)

        # LEFT FRAME (80%)
        left_frame = ctk.CTkScrollableFrame(self, fg_color= "#202020")
        left_frame.pack(side="left", fill="both", expand=True)

        # RIGHT FRAME (20%)
        right_frame = ctk.CTkFrame(self, fg_color= "#202020")
        right_frame.pack(side="left", fill="both", expand=False)

        right_frame.columnconfigure((0), weight= 2, pad=0)
        right_frame.rowconfigure((0,1,2), weight= 1, pad=0)

        inside_right_frame = ctk.CTkFrame(right_frame, fg_color= '#202020')
        inside_right_frame.grid(column = 0, row = 0, sticky = 'nswe')

        about_this_app_label = ctk.CTkLabel(inside_right_frame, text= 'About this app')
        about_this_app_label.pack(expand=False, fill= 'both')

        about_this_app_label2 = ctk.CTkLabel(inside_right_frame, text= 'Overnote 0.9')
        about_this_app_label2.pack(expand=False, fill= 'both')

        about_this_app_label3 = ctk.CTkLabel(inside_right_frame, text= '© 2025 Treadway. All rights reserved.')
        about_this_app_label3.pack(expand=False, fill= 'both')

        # Manually control width ratio
        self.update_idletasks()  # make sure window size is updated
        total_width = self.winfo_width()
        left_frame.configure(width=int(total_width*0.8))
        right_frame.configure(width=int(total_width*0.2))

        # Add multiple reusable sections
        theme_section_frame = ctk.CTkFrame(left_frame, fg_color='#202020')
        theme_section_frame.pack(fill='both')

        appearance_label_frame = ctk.CTkFrame(theme_section_frame, fg_color= '#202020')
        appearance_label_frame.pack(fill = 'x')

        appearance_label = ctk.CTkLabel(appearance_label_frame, text= 'Appearance', font= ('Arial', 17), fg_color='#202020')
        appearance_label.pack(fill='x', side= 'left', pady = 5, padx = 30)

        theme_section = CollapsibleSection(theme_section_frame, "App Theme", ["Light", "Dark", "Use System Setting"])
        theme_section.pack(fill="x", padx=20, pady=1)

        # text formatting widgets -------------------------------------------------------------------------
        
        text_formatting_frame = ctk.CTkFrame(left_frame, fg_color='#202020')
        text_formatting_frame.pack(pady=5, fill='both')

        text_formatting_label_frame = ctk.CTkFrame(text_formatting_frame, fg_color= '#202020')
        text_formatting_label_frame.pack(fill = 'x')

        text_formatting_label = ctk.CTkLabel(text_formatting_label_frame, text= 'Text Formatting', font= ('Arial', 17), fg_color='#202020')
        text_formatting_label.pack(fill='x', side= 'left', pady = 5, padx = 30)

        font_frame = ctk.CTkFrame(text_formatting_frame, fg_color='#202020')
        font_frame.pack(fill='both')

        section = CollapsibleSection_Empty(font_frame, "Font", '')
        section.pack(fill="x", padx=20, pady=5)

        section.options_frame.columnconfigure((0,1), weight=1, uniform='a')
        section.options_frame.rowconfigure((0,1,2,3), weight=1, uniform='a')

        family_label = ctk.CTkLabel(section.options_frame, text='Family')
        family_label.grid(column = 0, row = 0, sticky = 'w', padx= 25)

        style_label = ctk.CTkLabel(section.options_frame, text='Style')
        style_label.grid(column = 0, row = 1, sticky = 'w', padx= 25, pady= 7)

        size_label = ctk.CTkLabel(section.options_frame, text='Size')
        size_label.grid(column = 0, row = 2, sticky = 'w', padx= 25)

        family_dropdown = ctk.CTkOptionMenu(
            section.options_frame, values=["Century Gothic","Times New Roman", "Calibri"], fg_color= '#444444', button_color= '#444444', button_hover_color= '#555555')

        family_dropdown.grid(column = 1, row = 0, sticky = 'e', padx= 25)

        style_dropdown = ctk.CTkOptionMenu(
            section.options_frame, values=["Regular","Italic", "Bold", "Bold Italic"], fg_color= '#444444', button_color= '#444444', button_hover_color= '#555555')
        style_dropdown.grid(column = 1, row = 1, sticky = 'e', padx= 25)

        # Dropdown menu
        def change_font_size(choice):
            test_label.configure(font=("Arial", int(choice)))

        size_dropdown = ctk.CTkOptionMenu(
        section.options_frame, 
        values=['9', '10', '11', '12', '13', '14'],
        fg_color= '#444444', 
        button_color= '#444444',
        button_hover_color= '#555555',
        command=change_font_size  # callback when a value is picked
        )
        size_dropdown.grid(column = 1, row = 2, sticky = 'e', padx= 25)

        # Test label
        test_label = ctk.CTkLabel(
            section.options_frame, 
            text="The sound of ocean waves calms my soul.", 
            font=("Arial", 9)
            )
        test_label.grid(column = 0, columnspan = 2, row = 3, sticky = 's')

        word_wrap_frame = ctk.CTkFrame(font_frame, fg_color= '#313131')
        word_wrap_frame.pack(fill="x", padx=27, pady=5)

        word_wrap_label = ctk.CTkLabel(word_wrap_frame, text= 'Word wrap')
        word_wrap_label.pack(side = 'left', padx = 10, pady=10)

        def word_wrap_toggle_switch():
        # check the switch's current value
            if switch_var_wordwrap.get() == "on":
                word_wrap_switch.configure(text="On")
            else:
                word_wrap_switch.configure(text="Off")

        switch_var_wordwrap = ctk.StringVar(value="off")

        word_wrap_switch = ctk.CTkSwitch(
            word_wrap_frame,
            text="Off",  # default text
            variable=switch_var_wordwrap,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=word_wrap_toggle_switch  # function to run when clicked
)
        word_wrap_switch.pack(pady=5, side= 'right')
        
        formatting_frame = ctk.CTkFrame(font_frame, fg_color= '#313131')
        formatting_frame.pack(fill="x", padx=27, pady=5)

        formatting_label = ctk.CTkLabel(formatting_frame, text= 'Formatting')
        formatting_label.pack(side = 'left', padx = 10, pady=10)

        def formatting_toggle_switch():
        # check the switch's current value
            if switch_var_formatting.get() == "on":
                formatting_switch.configure(text="On")
            else:
                formatting_switch.configure(text="Off")

        switch_var_formatting = ctk.StringVar(value="off")

        formatting_switch = ctk.CTkSwitch(
            formatting_frame,
            text="Off",  # default text
            variable=switch_var_formatting,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=formatting_toggle_switch  # function to run when clicked
)
        formatting_switch.pack(pady=5, side= 'right')

        # Opening Notepad widgets ------------------------------------------------------------------
        opening_notepad_frame = ctk.CTkFrame(left_frame, fg_color= "#202020")
        opening_notepad_frame.pack(pady=5, fill='both')

        opening_notepad_label_frame = ctk.CTkFrame(opening_notepad_frame, fg_color= '#202020')
        opening_notepad_label_frame.pack(fill = 'x')

        opening_notepad_label = ctk.CTkLabel(opening_notepad_label_frame, text= 'Opening Notepad', font= ('Arial', 17), fg_color='#202020')
        opening_notepad_label.pack(fill='x', side= 'left', pady = 5, padx = 30)

        opening_files_dropdown_frame = ctk.CTkFrame(opening_notepad_frame, fg_color= '#313131')
        opening_files_dropdown_frame.pack(fill="x", padx=27, pady=5)

        opening_files_label = ctk.CTkLabel(opening_files_dropdown_frame, text= 'Opening files')
        opening_files_label.pack(side = 'left', padx= 15, pady = 10)

        opening_files_dropdown = ctk.CTkOptionMenu(
            opening_files_dropdown_frame, 
            values=["Open in a new tab","Open in a new window"], 
            fg_color= '#444444', button_color= '#444444', button_hover_color= '#555555'
            )
        
        opening_files_dropdown.pack(side = 'right', padx= 15)

        when_notepad_starts_dropdown = CollapsibleSection(opening_notepad_frame, "When Notepad starts", ["Continue previous session", "Start new session and discard unsaved changes"])
        when_notepad_starts_dropdown.pack(fill="x", padx=20, pady=1)


        recent_files_switch_frame = ctk.CTkFrame(opening_notepad_frame, fg_color= '#313131')
        recent_files_switch_frame.pack(fill="x", padx=27, pady=5)

        recent_files_label = ctk.CTkLabel(recent_files_switch_frame, text= 'Recent Files')
        recent_files_label.pack(side = 'left', padx= 10)

        def recent_files_toggle_switch():
        # check the switch's current value
            if switch_var_recent_files.get() == "on":
                recent_files_switch.configure(text="On")
            else:
                recent_files_switch.configure(text="Off")

        switch_var_recent_files = ctk.StringVar(value="off")

        recent_files_switch = ctk.CTkSwitch(
            recent_files_switch_frame,
            text="Off",  # default text
            variable=switch_var_recent_files,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=recent_files_toggle_switch  # function to run when clicked
)
        recent_files_switch.pack(pady=10, side= 'right')

        # Spelling widgets ------------------------------------------------------------------------------
        spelling_frame = ctk.CTkFrame(left_frame, fg_color= "#202020")
        spelling_frame.pack(pady=5, fill='both')

        spelling_frame_label_frame = ctk.CTkFrame(spelling_frame, fg_color= '#202020')
        spelling_frame_label_frame.pack(fill = 'x')

        spelling_frame_label = ctk.CTkLabel(spelling_frame_label_frame, text= 'Spelling', font= ('Arial', 17), fg_color='#202020')
        spelling_frame_label.pack(fill='x', side= 'left', pady = 5, padx = 30)

        spelling_section = CollapsibleSection_Empty(spelling_frame, "Spell Check", '')
        spelling_section.pack(fill="x", padx=20, pady=10)

        # Spell Check
        def spell_check_toggle_switch():
        # check the switch's current value
            if switch_var_spell_check.get() == "on":
                spell_check_switch.configure(text="On")
            else:
                spell_check_switch.configure(text="Off")

        switch_var_spell_check = ctk.StringVar(value="off")

        spell_check_switch = ctk.CTkSwitch(
            spelling_section.header_frame,
            text="Off",  # default text
            variable=switch_var_spell_check,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=spell_check_toggle_switch  # function to run when clicked
)
        spell_check_switch.pack(side= 'right')

        # .txt check
        txt_toggle_switch_frame = ctk.CTkFrame(spelling_section.options_frame)
        txt_toggle_switch_frame.pack(fill="x", pady=5)

        txt_toggle_switch_label = ctk.CTkLabel(txt_toggle_switch_frame, text='.txt')
        txt_toggle_switch_label.pack(side = 'left', padx= 20)

        def txt_toggle_switch():
        # check the switch's current value
            if switch_var_txt.get() == "on":
                txt_switch.configure(text="On")
            else:
                txt_switch.configure(text="Off")

        switch_var_txt = ctk.StringVar(value="off")

        txt_switch = ctk.CTkSwitch(
            txt_toggle_switch_frame,
            text="Off",  # default text
            variable=switch_var_txt,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=txt_toggle_switch  # function to run when clicked
)
        txt_switch.pack(side = 'right')

        # .md check
        md_toggle_switch_frame = ctk.CTkFrame(spelling_section.options_frame)
        md_toggle_switch_frame.pack(fill="x", pady=5)

        md_toggle_switch_label = ctk.CTkLabel(md_toggle_switch_frame, text='.md')
        md_toggle_switch_label.pack(side = 'left', padx= 20)

        def md_toggle_switch():
        # check the switch's current value
            if switch_var_md.get() == "on":
                md_switch.configure(text="On")
            else:
                md_switch.configure(text="Off")

        switch_var_md = ctk.StringVar(value="off")

        md_switch = ctk.CTkSwitch(
            md_toggle_switch_frame,
            text="Off",  # default text
            variable=switch_var_md,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=md_toggle_switch  # function to run when clicked
)
        md_switch.pack(side = 'right')

        # .srt/.ass check
        srt_ass_toggle_switch_frame = ctk.CTkFrame(spelling_section.options_frame)
        srt_ass_toggle_switch_frame.pack(fill="x", pady=5)

        srt_ass_toggle_switch_label = ctk.CTkLabel(srt_ass_toggle_switch_frame, text='.srt / .ass')
        srt_ass_toggle_switch_label.pack(side = 'left', padx= 20)

        def srt_ass_toggle_switch():
        # check the switch's current value
            if switch_var_srt_ass.get() == "on":
                srt_ass_switch.configure(text="On")
            else:
                srt_ass_switch.configure(text="Off")

        switch_var_srt_ass = ctk.StringVar(value="off")

        srt_ass_switch = ctk.CTkSwitch(
            srt_ass_toggle_switch_frame,
            text="Off",  # default text
            variable=switch_var_srt_ass,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=srt_ass_toggle_switch  # function to run when clicked
)
        srt_ass_switch.pack(side= 'right')

        autocorrect_toggle_switch_frame = ctk.CTkFrame(spelling_frame, fg_color= '#313131')
        autocorrect_toggle_switch_frame.pack(fill="x", padx=27, pady=5)

        autocorrect_toggle_switch_frame_label = ctk.CTkLabel(autocorrect_toggle_switch_frame, text= 'Autocorrect', font= ('Arial', 17))
        autocorrect_toggle_switch_frame_label.pack(side = 'left', padx = 10, pady=10)


        def autocorrect_toggle_switch():
        # check the switch's current value
            if switch_var_autocorrect.get() == "on":
                autocorrect_switch.configure(text="On")
            else:
                autocorrect_switch.configure(text="Off")

        switch_var_autocorrect = ctk.StringVar(value="off")

        autocorrect_switch = ctk.CTkSwitch(
            autocorrect_toggle_switch_frame,
            text="Off",  # default text
            variable=switch_var_autocorrect,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=autocorrect_toggle_switch  # function to run when clicked
)
        autocorrect_switch.pack(padx=0, side= 'right')

class CollapsibleSection(ctk.CTkFrame):
    def __init__(self, parent, title, options=None):
        super().__init__(parent, fg_color= "#202020")

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color= '#313131')
        self.header_frame.pack(fill="x", padx=10, pady=5)

        self.header_label = ctk.CTkLabel(
            self.header_frame, text=title, anchor="w", font=("Segoe UI", 16)
        )
        self.header_label.pack(side="left", padx=10, pady=10)

        self.arrow_label = ctk.CTkLabel(
            self.header_frame, text=">", font=("Segoe UI", 16)
        )
        self.arrow_label.pack(side="right", padx=5)

        # --- Options Frame (hidden by default) ---
        self.options_frame = ctk.CTkFrame(self, fg_color='#262626')
        self.options_visible = False

        # Add radio buttons (or any widget) if provided
        if options:   # this create a radio button everytime you add an arg whenever you are calling the main class
            for opt in options: # or this is much accurate comment ---- # creates a radio button for each option provided when instantiating the class
                ctk.CTkRadioButton(
                    self.options_frame, 
                    text=opt, 
                    fg_color="#F97373", 
                    border_width_unchecked = 1.5, 
                    border_width_checked = 5, 
                    hover_color= "#B94848"
                    
                ).pack(anchor="w", padx=20, pady=2)

        # --- Bind Toggle ---
        self.header_frame.bind("<Button-1>", lambda e: self.toggle_options())
        self.header_label.bind("<Button-1>", lambda e: self.toggle_options())
        self.arrow_label.bind("<Button-1>", lambda e: self.toggle_options())

    def toggle_options(self):
        if self.options_visible:
            self.options_frame.pack_forget()
            self.arrow_label.configure(text=">")
        else:
            self.options_frame.pack(fill="x", padx=10, pady=(0, 5))
            self.arrow_label.configure(text="<")
        self.options_visible = not self.options_visible

class CollapsibleSection_Empty(ctk.CTkFrame):
    def __init__(self, parent, title="Section", title2='Section'):
        super().__init__(parent, fg_color= "#202020")

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color= '#313131')
        self.header_frame.pack(fill="x", padx=10, pady=5)

        self.header_label = ctk.CTkLabel(self.header_frame, text=title, anchor="w", font=("Segoe UI", 16))
        
        self.header_label2 = ctk.CTkLabel(self.header_frame, text=title2, anchor="e", font=("Segoe UI", 16))
        
        self.header_label.pack(side="left", padx=10, pady=10)
        self.header_label2.pack(side="right", padx=10, pady=10)

        self.arrow_label = ctk.CTkLabel(
            self.header_frame, text=">", font=("Segoe UI", 16)
        )
        self.arrow_label.pack(side="right", padx=5)

        # --- Options Frame (hidden by default) ---
        self.options_frame = ctk.CTkFrame(self, fg_color='#262626')
        self.options_visible = False

        # --- Bind Toggle ---
        self.header_frame.bind("<Button-1>", lambda e: self.toggle_options())
        self.header_label.bind("<Button-1>", lambda e: self.toggle_options())
        self.arrow_label.bind("<Button-1>", lambda e: self.toggle_options())

    def toggle_options(self):
        if self.options_visible:
            self.options_frame.pack_forget()
            self.arrow_label.configure(text=">")
        else:
            self.options_frame.pack(fill="x", padx=10, pady=(0, 5))
            self.arrow_label.configure(text="<")
        self.options_visible = not self.options_visible

class StatusBarFrame(ctk.CTkFrame):
    def __init__(self, parent, main_text_area):
        super().__init__(parent, fg_color="#202020", height= 75)

        self.grid(column = 0, row = 3, columnspan = 3, sticky = 'we')

        self.main_text_area = main_text_area
        self.main_text_area.bind("<KeyPress>", self.update_status)
        self.winfo_toplevel().bind("<Motion>", self.update_status)

        # this frame for keeping the status bar from chaning the height of the text area
        self.main_status_frame = ctk.CTkFrame(self)
        self.main_status_frame.pack(expand = False, fill='x', side= 'bottom')

        # frames for seperating
        frame_one_text_count = ctk.CTkFrame(self.main_status_frame, fg_color="#202020")
        frame_one_text_count.pack(expand = True, side= 'left', fill = 'x')

        frame_two_text_formatted = ctk.CTkFrame(self.main_status_frame, fg_color="#202020")
        frame_two_text_formatted.pack(expand = True, side= 'left', fill = 'x')

        frame_three_text_type = ctk.CTkFrame(self.main_status_frame, fg_color="#202020")
        frame_three_text_type.pack(expand = True, side= 'right', fill = 'x')

        # Frame 1 table ------------------------
        frame_one_text_count.columnconfigure((0,1), uniform='a') 
        frame_one_text_count.rowconfigure(0, uniform='a')

        self.cursor_line_and_col_count_and_character = ctk.CTkLabel(frame_one_text_count, text= 'Ln 1, Col 1 | 0 characters')
        self.cursor_line_and_col_count_and_character.grid(column = 0, row = 0, sticky="w", padx=25)

        # Frame 2 table ------------------------
        frame_two_text_formatted.columnconfigure(0, weight=1, uniform='a') 
        frame_two_text_formatted.rowconfigure(0, weight=1, uniform='a')

        formatted_markdownsyntax = ctk.CTkLabel(frame_two_text_formatted, text= 'Formatted')
        formatted_markdownsyntax.grid(column = 0, row = 0, sticky="w", padx=1)

        # Frame 3 table ------------------------
        frame_three_text_type.columnconfigure((0,1,2), weight=1, uniform='a') 
        frame_three_text_type.rowconfigure(0, weight=1, uniform='a')

        zoom_percentage = ctk.CTkLabel(frame_three_text_type, text= '100%')
        zoom_percentage.grid(column = 0, row = 0, sticky="w", padx=5)

        windows_crlf = ctk.CTkLabel(frame_three_text_type, text= 'Windows (CRLF)')
        windows_crlf.grid(column = 1, row = 0, sticky="w", padx=5)

        text_type = ctk.CTkLabel(frame_three_text_type, text= 'UTF-8')
        text_type.grid(column = 2, row = 0, sticky="w", padx=5)

    def update_status(self, event=None):
                # Get the current cursor position
                cursor_position = self.main_text_area.index(tk.INSERT)
                line, column = cursor_position.split(".")

                # Count all characters
                content = self.main_text_area.get("1.0", "end-1c")
                char_count = len(content)

                # Update label
                self.cursor_line_and_col_count_and_character.configure(text=f"Ln {line} | Col {int(column)+1} | {char_count} characters")

class TabSystemFrame(ctk.CTkFrame):
    def __init__(self, parent, main_text_area):
        super().__init__(parent)
        self.grid(column = 0, row = 1, columnspan = 3, sticky = 'we', padx=0, pady=0)

        # Store tab data
        tabs_data = {}
        self.current_tab = None
        self.tab_count = 0

        def new_tab():
            def rename_box():
                # setup
                rename_box = ctk.CTkToplevel(tab_bar)
                rename_box.attributes("-topmost", True)

                w, h = 250, 250
                ws = self.winfo_screenwidth()
                hs = self.winfo_screenheight()
                x = (ws // 2) - (w // 2)
                y = (hs // 2) - (h // 2)
                rename_box.geometry(f"{w}x{h}+{x}+{y}")

                # widgets
                rename_entry_label = ctk.CTkLabel(rename_box, text = "Rename Tab")
                rename_entry_label.pack()
                
                self.rename_entry = ctk.CTkEntry(rename_box)
                self.rename_entry.pack()

            self.tab_count += 1
            name = f"Tab {self.tab_count}"
            tabs_data[name] = ""
            self.tab_button = ctk.CTkButton(tab_bar, text=name, command=lambda n=name: switch_tab(n), fg_color= '#202020', hover_color='#303030')
            self.tab_button.pack(side="left", padx=2)
            switch_tab(name)

            self.tab_button.bind("<Double-1>", lambda event: rename_box())

        def switch_tab(name):
            # Save old content before switching
            if self.current_tab:
                tabs_data[self.current_tab] = self.main_text_area.get("1.0", "end-1c")
            # Load new tab’s content
            self.main_text_area.delete("1.0", "end")
            self.main_text_area.insert("1.0", tabs_data[name])
            self.current_tab = name

        tab_bar = ctk.CTkScrollableFrame(self, height=40, orientation='horizontal')
        tab_bar.pack(side="top", fill="x")

        # "+" button to create new tabs
        self.add_button = ctk.CTkButton(tab_bar, text="+", width=40, command= lambda: new_tab(), fg_color= '#202020', hover_color='#303030')
        self.add_button.pack(side="right", padx=5)
        self.after(100, new_tab) # this here - I can't click the plus everytime to start the tab system so this will do it auto

        self.initiate_tab = new_tab

        self.main_text_area = main_text_area

# ---------------------------------------------------#
if __name__ == "__main__":                           #
    MainApp('OverNote', (1400, 800)) # Start the app #
# ---------------------------------------------------#