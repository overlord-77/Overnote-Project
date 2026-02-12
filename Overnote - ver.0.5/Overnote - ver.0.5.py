import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
# import ttkbootstrap as ttb
# from ttkbootstrap.toast import ToastNotification

"""
Overnote version 0.5 on Branch -> Exe <- From Branch -> Main <-

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
        self.pack(expand = False, fill='both')

        left_option_bar = LeftOptionsBar(self)
        
class LeftOptionsBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="left")


       

        # menus tabs
        left_option_bar_menu = tk.Menu(self)

        #widgets 
        file_menu = File_Menu(left_option_bar_menu)
        edit_menu = Edit_Menu(left_option_bar_menu)
        view_menu = View_Menu(left_option_bar_menu)

        heading_tab = Heading_Tab(left_option_bar_menu)
        list_type_tab = List_Type_Tab(left_option_bar_menu)


        

        def link_tab_func():
            link_tab = Link_Tab(self)

        def setting_window_func():
            setting_window = Setting_Window(self)

        left_option_bar_menu.add_cascade(label='File', menu=file_menu)
        left_option_bar_menu.add_cascade(label='Edit', menu=edit_menu)
        left_option_bar_menu.add_cascade(label='View', menu=view_menu)

        left_option_bar_menu.add_cascade(label='H1', menu=heading_tab)
        left_option_bar_menu.add_cascade(label='☰', menu=list_type_tab)
        left_option_bar_menu.add_cascade(label='𝐁', command= lambda: print('Bold Text - Add Button Clicked kinda type'))
        left_option_bar_menu.add_cascade(label='𝐼', command= lambda: print('Italic Text - Add Button Clicked kinda type'))


        left_option_bar_menu.add_command(label='🔗', command = link_tab_func)
        left_option_bar_menu.add_cascade(label='🅰️⌫', command= lambda: print('Clear Formatting'))
        

        left_option_bar_menu.add_cascade(label='⚙️', command= setting_window_func)  


        # Apply menu bar to the top-level window, not this frame
        self.winfo_toplevel().config(menu=left_option_bar_menu)


        

class File_Menu(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(parent, tearoff=False)

        self.add_cascade(label='New Tab')
        self.add_cascade(label='New Window')

        self.add_cascade(label='New Markdown Tab')
        self.add_cascade(label='Open')
        self.add_cascade(label='Recent')
        self.add_cascade(label='Save')
        self.add_cascade(label='Save As')
        self.add_cascade(label='Save All')
        self.add_cascade(label='Page Setup')

        self.add_cascade(label='Print')
        self.add_cascade(label='Close Tab')
        self.add_cascade(label='Close Window')
        self.add_cascade(label='Exit')


class Edit_Menu(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(parent, tearoff=False)

        self.add_cascade(label='Undo')
        self.add_cascade(label='Cut')
        self.add_cascade(label='Copy')
        self.add_cascade(label='Paste')
        self.add_cascade(label='Delete')
        self.add_cascade(label='Clear Formatting')
        self.add_cascade(label='Find')
        self.add_cascade(label='Find Next')
        self.add_cascade(label='Find Previous')
        self.add_cascade(label='Replace')
        self.add_cascade(label='Go To')
        self.add_cascade(label='Select All')
        self.add_cascade(label='Time/Date')
        self.add_cascade(label='Font')

class View_Menu(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(parent, tearoff=False)

        self.add_cascade(label='Zoom')
        self.add_cascade(label='Status Bar')
        self.add_cascade(label='Word Wrap')
        self.add_cascade(label='Markdown')


class Heading_Tab(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(parent, tearoff=False)

        self.add_cascade(label='Title')
        self.add_cascade(label='Subtitle')
        self.add_cascade(label='Heading')
        self.add_cascade(label='Subheading')

        self.add_cascade(label='Section')
        self.add_cascade(label='Subsection')
        self.add_cascade(label='Body')


class List_Type_Tab(tk.Menu):
    def __init__(self, parent, tearoff=False):
        super().__init__(parent, tearoff=False)

        self.add_cascade(label='Bulleted List')
        self.add_cascade(label='Numbered Lis')


class Link_Tab(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)


        self.geometry('400x400')

        frame = ctk.CTkFrame(self)
        frame.pack(expand = True, fill='both')


        label_link = ctk.CTkLabel(frame, text= 'Link')
        label_link.pack()


        label_display = ctk.CTkLabel(frame, text= 'Display Text')
        label_display.pack()


        entry_widget = ttk.Entry(frame)
        entry_widget.pack()

        entry_widget.insert(0, "Text for the link (optional)")

        label_address = ctk.CTkLabel(frame, text= 'Address')
        label_address.pack()


        entry_widget2 = ttk.Entry(frame)
        entry_widget2.pack()

        entry_widget2.insert(0, "Link to an existing webpage")


        frame4 = ctk.CTkFrame(self)
        frame4.pack()

        button = ttk.Button(frame4, text= 'Insert')
        button.pack(side='left')

        button2 = ttk.Button(frame4, text= 'Cancel')
        button2.pack()



class Setting_Window(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Setting")
        self.geometry('1200x600')


        setting_label = ctk.CTkLabel(self, text= 'Setting')
        setting_label.pack()

        left_frame = ctk.CTkFrame(self)
        left_frame.pack(expand = True, fill='both')
        
        right_frame = ctk.CTkFrame(self)
        right_frame.pack(expand = True, fill='both')


        # appearance frame widgets --------------------------------------------------------------
        appearance_frame = ctk.CTkFrame(left_frame)
        appearance_frame.pack()
        appearance_label = ctk.CTkLabel(appearance_frame, text= 'Appearance')
        appearance_label.pack()


        app_theme_frame = ctk.CTkFrame(appearance_frame)
        app_theme_frame.pack()


        app_theme_dropdown = ctk.CTkOptionMenu(app_theme_frame, values=["App Theme","Light", "Dark", 'Use System Setting'])
        app_theme_dropdown.pack()


        # text formatting widgets -------------------------------------------------------------------------
        text_formatting_frame = ctk.CTkFrame(left_frame)
        text_formatting_frame.pack(pady=25)

        text_formatting_label = ctk.CTkLabel(text_formatting_frame, text= 'Text Formatting')
        text_formatting_label.pack()

        font_frame = ctk.CTkFrame(text_formatting_frame)
        font_frame.pack()


        family_dropdown = ctk.CTkOptionMenu(font_frame, values=["Century Gothic","Times New Roman", "Calibri"])
        family_dropdown.pack()


        style_dropdown = ctk.CTkOptionMenu(font_frame, values=["Regular","Italic", "Bold", "Bold Italic"])
        style_dropdown.pack()


        size_dropdown = ctk.CTkOptionMenu(font_frame, values=["9", "10", "11", "12", "13", '14'])
        size_dropdown.pack()


      


        def word_wrap_toggle_switch():
        # check the switch's current value
            if switch_var_wordwrap.get() == "on":
                word_wrap_switch.configure(text="Word wrap - On")
            else:
                word_wrap_switch.configure(text="Word wrap - Off")

        switch_var_wordwrap = ctk.StringVar(value="off")

        word_wrap_switch = ctk.CTkSwitch(
            font_frame,
            text="Word wrap - Off",  # default text
            variable=switch_var_wordwrap,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=word_wrap_toggle_switch  # function to run when clicked
)
        word_wrap_switch.pack(pady=5)








        def formatting_toggle_switch():
        # check the switch's current value
            if switch_var_formatting.get() == "on":
                formatting_switch.configure(text="Formatting - On")
            else:
                formatting_switch.configure(text="Formatting - Off")

        switch_var_formatting = ctk.StringVar(value="off")

        formatting_switch = ctk.CTkSwitch(
            font_frame,
            text="Formatting - Off",  # default text
            variable=switch_var_formatting,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=formatting_toggle_switch  # function to run when clicked
)
        formatting_switch.pack()


        # Opening Notepad widgets ------------------------------------------------------------------
        opening_notepad_frame = ctk.CTkFrame(left_frame)
        opening_notepad_frame.pack(pady=25)

        opening_notepad_label = ctk.CTkLabel(opening_notepad_frame, text= 'Opening Notepad')
        opening_notepad_label.pack()

        opening_files_dropdown = ctk.CTkOptionMenu(opening_notepad_frame, values=["Open in a new tab","Open in a new window"])
        opening_files_dropdown.pack()

        when_notepad_starts_dropdown = ctk.CTkOptionMenu(opening_notepad_frame, values=["Continue previous session","Start new session and discard unsaved changes"])
        when_notepad_starts_dropdown.pack()


        def recent_files_toggle_switch():
        # check the switch's current value
            if switch_var_recent_files.get() == "on":
                recent_files_switch.configure(text="Recent Files - On")
            else:
                recent_files_switch.configure(text="Recent Files - Off")

        switch_var_recent_files = ctk.StringVar(value="off")

        recent_files_switch = ctk.CTkSwitch(
            opening_notepad_frame,
            text="Recent Files - Off",  # default text
            variable=switch_var_recent_files,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=recent_files_toggle_switch  # function to run when clicked
)
        recent_files_switch.pack()




        # Spelling widgets ------------------------------------------------------------------------------
        spelling_frame = ctk.CTkFrame(left_frame)
        spelling_frame.pack(pady=25)

        spelling_frame_label = ctk.CTkLabel(spelling_frame, text= 'Spelling')
        spelling_frame_label.pack()



        def spell_check_toggle_switch():
        # check the switch's current value
            if switch_var_spell_check.get() == "on":
                spell_check_switch.configure(text="Spell Check - On")
            else:
                spell_check_switch.configure(text="Spell Check - Off")

        switch_var_spell_check = ctk.StringVar(value="off")

        spell_check_switch = ctk.CTkSwitch(
            spelling_frame,
            text="Spell Check - Off",  # default text
            variable=switch_var_spell_check,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=spell_check_toggle_switch  # function to run when clicked
)
        spell_check_switch.pack()



        def autocorrect_toggle_switch():
        # check the switch's current value
            if switch_var_autocorrect.get() == "on":
                autocorrect_switch.configure(text="Autocorrect - On")
            else:
                autocorrect_switch.configure(text="Autocorrect - Off")

        switch_var_autocorrect = ctk.StringVar(value="off")

        autocorrect_switch = ctk.CTkSwitch(
            spelling_frame,
            text="Autocorrect - Off",  # default text
            variable=switch_var_autocorrect,
            fg_color="#4D4B4B",
            progress_color="#FC7676",
            onvalue="on",
            offvalue="off",
            command=autocorrect_toggle_switch  # function to run when clicked
)
        autocorrect_switch.pack()
















MainApp('OverNote', (1400,700) )