## 📌 General Notes

* Add what this update is about to see if we can replace the current menu with something else like the code below

---

## 🖥️ Software Information

| Field Name              | Value                          |
| ----------------------- | ------------------------------ |
| Software Name           | Overnote                       |
| Software Type           | GUI (Graphical User Interface) |
| Software Purpose        | Text Editor                    |
| Software Version        | 0.8                            |
| Software Update Init    | 2025-10-10                     |
| Software Release Update | 2025-10-10                     |
| Software Made By        | Treadway                       |
| Programming Language    | Python                         |
| Code Size (approx.)     | 1064 lines - ※**Medium**※      |
| Level                   | High-Level                     |

---

## 🔄 Updates To The Main Menu Bar (Layout & Design)

📅 Plan Update — Created on **2025-10-09**

We currently have a working **menu system** built using `tk.Menu`.  
However, the goal now is to **replace it with a more flexible and modern layout**.

⚙️ Overview of the New Menu System

The new design approach is straightforward:

Instead of creating a single `tk.Menu` bar, we will structure the interface using **three dedicated frames** inside the main `MainOptionBar` frame:

* LeftOptionsBar

* CenterOptionsBar

* RightOptionsBar

Each of these frames will contain a `tk.Menubutton`, and each `Menubutton` will have a `tk.Menu` attached as its parent.

For example:

menu_button = tk.Menubutton(LeftOptionsBar, text="File")
menu = tk.Menu(menu_button, tearoff=False)
menu_button.config(menu=menu)

```
menu_button = tk.Menubutton(LeftOptionsBar, text="File")
menu = tk.Menu(menu_button, tearoff=False)
menu_button.config(menu=menu)
```

This method allows for more **customization**, **flexibility**, and **modern visual arrangement** compared to the traditional `tk.Menu` bar.

Second Example:

# Create a Menubutton (like "File")

file_btn = tk.Menubutton(menubar, text="File", bg="#333", fg="white", relief="flat")
file_btn.pack(side="left", padx=5, pady=2)

# Create a dropdown menu for that button

file_menu = tk.Menu(file_btn, tearoff=0)

```
# Create a Menubutton (like "File")
file_btn = tk.Menubutton(menubar, text="File", bg="#333", fg="white", relief="flat")
file_btn.pack(side="left", padx=5, pady=2)

# Create a dropdown menu for that button
file_menu = tk.Menu(file_btn, tearoff=0)
```

| Feature/Task                                             | Status  |
| -------------------------------------------------------- | ------- |
| Adding to the MainOptionBar, a -> LeftOptionsBar         | 🟢 Done |
| Adding to the MainOptionBar, a -> CenterOptionsBar       | 🟢 Done |
| Adding to the MainOptionBar, a -> RightOptionsBar        | 🟢 Done |
| Connect old Menu’s classes to the new frames             | 🟢 Done |
| Fix the new menus layout -> Checklist Below              | 🟢 Done |
| Adding to the LeftOptionBar, a -> File Menubutton        | ✅ Done  |
| Adding to the LeftOptionBar, a -> Edit Menubutton        | ✅ Done  |
| Adding to the LeftOptionBar, a -> View Menubutton        | ✅ Done  |
| Adding to the CenterOptionBar, a -> Heading Menubutton   | ✅ Done  |
| Adding to the CenterOptionBar, a -> List-Type Menubutton | ✅ Done  |
| Adding to the CenterOptionBar, a -> Bold Menubutton      | ✅ Done  |
| Adding to the CenterOptionBar, a -> Italic Menubutton    | ✅ Done  |
| Adding to the CenterOptionBar, a -> Link-Tab Button      | ✅ Done  |
| Adding to the CenterOptionBar, a -> Clear-Formatt Button | ✅ Done  |
| Adding to the RightOptionBar, a -> Setting Button        | ✅ Done  |

---

# The Alternative Menu System:

import tkinter as tk
root = tk.Tk()
root.title("Menubutton Dropdown Example")

# Simulated custom menu bar

menubar = tk.Frame(root, bg="#333", height=30)
menubar.pack(side="top", fill="x")

# Create a Menubutton (like "File")

file_btn = tk.Menubutton(menubar, text="File", bg="#333", fg="white", relief="flat")
file_btn.pack(side="left", padx=5, pady=2)

# Create a dropdown menu for that button

file_menu = tk.Menu(file_btn, tearoff=0)
file_menu.add_command(label="New File", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Attach menu to the button

file_btn.config(menu=file_menu)

# Add another dropdown

edit_btn = tk.Menubutton(menubar, text="Edit", bg="#333", fg="white", relief="flat")
edit_btn.pack(side="left", padx=5, pady=2)
edit_menu = tk.Menu(edit_btn, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: print("Undo"))
edit_menu.add_command(label="Redo", command=lambda: print("Redo"))
edit_btn.config(menu=edit_menu)

# Add another dropdown

view_btn = tk.Menubutton(menubar, text="View", bg="#333", fg="white", relief="flat")
view_btn.pack(side="left", padx=5, pady=2)
view_menu = tk.Menu(view_btn, tearoff=0)
view_menu.add_command(label="Zoom", command=lambda: print("Undo"))
view_menu.add_command(label="Status Bar", command=lambda: print("Redo"))
view_btn.config(menu=view_menu)

# Add extra widgets to the menubar

search_entry = tk.Entry(menubar, width=20)
search_entry.pack(side="right", padx=10)
search_btn = tk.Button(menubar, text="Search")
search_btn.pack(side="right", padx=5)
root.mainloop()

```
import tkinter as tk

root = tk.Tk()
root.title("Menubutton Dropdown Example")

# Simulated custom menu bar
menubar = tk.Frame(root, bg="#333", height=30)
menubar.pack(side="top", fill="x")

# Create a Menubutton (like "File")
file_btn = tk.Menubutton(menubar, text="File", bg="#333", fg="white", relief="flat")
file_btn.pack(side="left", padx=5, pady=2)

# Create a dropdown menu for that button
file_menu = tk.Menu(file_btn, tearoff=0)
file_menu.add_command(label="New File", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Attach menu to the button
file_btn.config(menu=file_menu)

# Add another dropdown
edit_btn = tk.Menubutton(menubar, text="Edit", bg="#333", fg="white", relief="flat")
edit_btn.pack(side="left", padx=5, pady=2)

edit_menu = tk.Menu(edit_btn, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: print("Undo"))
edit_menu.add_command(label="Redo", command=lambda: print("Redo"))
edit_btn.config(menu=edit_menu)



# Add another dropdown
view_btn = tk.Menubutton(menubar, text="View", bg="#333", fg="white", relief="flat")
view_btn.pack(side="left", padx=5, pady=2)

view_menu = tk.Menu(view_btn, tearoff=0)
view_menu.add_command(label="Zoom", command=lambda: print("Undo"))
view_menu.add_command(label="Status Bar", command=lambda: print("Redo"))
view_btn.config(menu=view_menu)

# Add extra widgets to the menubar
search_entry = tk.Entry(menubar, width=20)
search_entry.pack(side="right", padx=10)

search_btn = tk.Button(menubar, text="Search")
search_btn.pack(side="right", padx=5)

root.mainloop()
```
