## 📌 General Notes

* Version 1.5 focuses on various things such as the save as and how the file extension is saved, and on the help window that show you how to use the software, and about the shortcuts and some fixes.

---

## 🖥️ Software Information

| Field Name              | Value                          |
| ----------------------- | ------------------------------ |
| Software Name           | Overnote                       |
| Software Type           | GUI (Graphical User Interface) |
| Software Purpose        | Text Editor                    |
| Software Version        | 1.5                            |
| Software Update Init    | 2026-01-26                     |
| Software Release Update | 2026-02-11                     |
| Software Made By        | Treadway                       |
| Programming Language    | Python                         |
| Code Size (approx.)     | 2887 lines - ※**Medium**※      |
| Abstract Level          | High-Level                     |

---

## 🔄 Updates To The (Tab System & Markdown System & File System) — (Functionality & Widget)

📅 Plan Update — Created on **2026-01-23**

---

| Feature / Task                                       | Status | Detailed Instruction / Value                                                                                                                                                                                                                                                               |
| ---------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Add to Functionality → Save / Save As                | 🟢D    | add the .md to the ext when saving a file so it show or save the file as .md / have it to say if you want to keep formatting save as .md, if not then save it as .txt / allow the markdown redner to zoom in or out                                                                        |
| Add to Open With → Overnote.exe                      | 🟢D    | allow files to open with Overnote.exe and load the file like any other software                                                                                                                                                                                                            |
| Add to Functionality → Keyboard Shortcut in Settings | 🟢D    | fix the saving button so when i open a file and click save it save to it /// make a keyboard shortcut in each menu so you can access or enable something using a keyboard key  <br>  <br>> make sure to give functionality to all the shortcut that mentioned in the shortcut help window. |
| Add to Functionality → Tab System File Name          | 🟢D    | add that when open a file it show the name of the file on the tab and when i double click open a window and allow changing the name of the tab  <br>  <br>- (80% working) - open one new tap per window                                                                                    |
| Add to Functionality → Settings Right Frame          | 🟢D    | in the setting section right frame add a help button that will open a window and show how to use this whole software /// how to add headings or bold text and how to remove them or how to switch from markdown syntax to rendered and all of the things you can do in the app             |
| Add to Functionality → Markdown Over Tab System      | 🟢D    | When I render a tab - i can't switch tabs nor render them all at once - must fix - (LIMITED)                                                                                                                                                                                               |
| Add to Functionality → Text Widget Border            | 🟢D    | remove the border so the text widget and the render have the same text widget appearance                                                                                                                                                                                                   |
| Add to Functionality → Tab System Deleting Tabs      | 🟢D    | put all the create tabs in a list and then when i select delete tab it delete from the list one by one.  <br>  <br>add a delete button to the tabs theme self to delete them individually                                                                                                  |

---

| Done | Pending |
| ---- | ------- |
| 🟢D  | 🔴P     |



---

# Project Name

A Python project built with **Python 3.12.9** using a local virtual environment (`.venv`).
The virtual environment is **not committed** to the repository and must be created locally.

---

## ⚙️ Requirements

Before doing anything, make sure you have:

- **Python 3.12.9** installed  
  Check with:
  ```bash
  python --version
```

If this does not show **3.12.9**, install Python from: [Download Python | Python.org](https://www.python.org/downloads/)

* **Git** installed
* A terminal (PowerShell, Command Prompt, VS Code terminal, etc.)

---

## 📦 Project Setup (Required)

### 1️⃣ Clone the repository

```bash
git clone <REPO_URL>
cd <REPO_FOLDER>
```

---

### 2️⃣ Create a virtual environment

This creates a local `.venv` folder (ignored by Git):

```bash
py -3.12 -m venv .venv
```

You should now see a `.venv/` folder in the project directory.

---

### 3️⃣ Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

When activated, your terminal will show:

```
(.venv)
```

If you don’t see this, stop. The environment is not active.

---

### 4️⃣ Install dependencies

All required libraries are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

This installs everything **inside the virtual environment only**.

---

### 5️⃣ Run the project

```bash
python app.py
```

(Replace `app.py` with the correct entry file if different.)

---

## 🧪 Optional: Create an executable (.exe)

If you want to turn the project into a standalone Windows executable.

### 1️⃣ Install PyInstaller (inside venv)

Make sure the virtual environment is active:

```bash
pip install pyinstaller
```

---

### 2️⃣ Build the executable

```bash
pyinstaller --clean --noconfirm --onefile --windowed --icon="assets/o_icon.ico" --add-data "assets/o_icon.ico;assets" "<appname>.py"
```

```
dist/
└── app.exe
```

This `.exe` can be run on Windows systems **without Python installed**.

---

### 3️⃣ (Optional) Clean build files

PyInstaller creates extra folders. You can delete:

```
build/
__pycache__/
*.spec
```

The important output is inside `dist/`.

---

## 📁 Project Structure

```
project/
├── .gitignore        # Prevents committing .venv and junk files
├── README.md         # This file
├── requirements.txt  # Dependency list
├── app.py            # Main entry point
└── .venv/            # Local virtual environment (NOT committed)
```

---

## 🚫 What is NOT committed (by design)

* `.venv/`
* `__pycache__/`
* Build artifacts

These are intentionally excluded to keep the repository clean and portable.

---

## 🧠 Notes

* Always activate `.venv` before running or installing anything

* If dependencies change, update them with:
  
  ```bash
  pip freeze > requirements.txt
  ```

* Anyone cloning the repo must recreate the virtual environment locally

---
