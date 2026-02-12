## 📌 General Notes

* Version 1.4 focuses the renovation - re do what I need to redo to fit the markdown syntax tag system

* I must remove all old codes that don’t fit with the new markdown syntax system

* apply the new markdown syntax system to all respective code from now and on after all all word processing software either use visible syntax or hidden syntax in the plain text file that you may get access or not.

* Everything that will be inserted to the plain text file shall be in markdown syntax system but in app will be rendered

* -> In software (by default): all the text inside of the text area widget will be as plain text or markdown syntax

* -> File type will change from plain text or markdown syntax to formatted (auto rendering), when ever formatting is added to the text in the text widget, like changing the font

* -> File that end with file(.md), software will open with text widget converted to formatted and toggle between formatted and markdown syntax is enabled

* -> File that end with file(.txt) the software will open with text widget as plain text, it won’t have the markdown syntax to formatted toggle enabled, but any formatting added to the text widget of a file(.txt) then it will be converted to formatted therefore you can switch from formatting to markdown syntax, but you must save the file as file(.md) or otherwise you will see the syntax tag and you won’t see your formatting.

* -> Example of bold text in syntax tag | **bold text**

* -> Example of italic text in syntax tag | *italic text*

* -> Example of bulleted text in syntax tag | * bulleted

* -> Example of numbered text in syntax tag | 1. numbered text

* -> Example of link in syntax tag | [Youtube][https://www.youtube.com/](https://www.youtube.com/ "https://www.youtube.com/"))

---

## 🖥️ Software Information

| Field Name              | Value                          |
| ----------------------- | ------------------------------ |
| Software Name           | Overnote                       |
| Software Type           | GUI (Graphical User Interface) |
| Software Purpose        | Text Editor                    |
| Software Version        | 1.4                            |
| Software Update Init    | 2025-12-14                     |
| Software Release Update | 2026-01-22                     |
| Software Made By        | Treadway                       |
| Programming Language    | Python                         |
| Code Size (approx.)     | 2526 lines - ※**Medium**※      |
| Level                   | High-Level                     |

---

## 🔄 Updates To The (View Menu & Center Main Menu Widgets & Status bar) — (Renovation & Functional & Logic)

📅 Plan Update — Created on **2025-12-11**

---

| Feature / Task                                                               | Status | Detailed Instruction / Value                                                                                                                                                              |
| ---------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add to Functionality → Markdown                                              | 🟢D    | On = when file ext is .md - allow to write markdown syntax and turn it to formatted                                                                                                       |
| Add to Functionality → H1                                                    | 🟢D    | different type of font size such as headings and subheadings                                                                                                                              |
| Add to Functionality → List Type                                             | 🟢D    | bulleted and numbered list - (Numbered List Need Upgrade in Future)                                                                                                                       |
| Add to Functionality → Bold                                                  | 🟢D    | set sel text to bold \| -> Example of bold text in syntax tag \| **bold text**                                                                                                            |
| Add to Functionality → Italic                                                | 🟢D    | set sel text to italic \| -> Example of italic text in syntax tag \| *italic text*                                                                                                        |
| Add to Functionality → Link                                                  | 🟢D    | link adding, and allow link naming -> Example in syntax tag \| [Youtube][https://www.youtube.com/](https://www.youtube.com/ "Ctrl-click to open: https://www.youtube.com/"))              |
| Add to Functionality → Clear Formatting                                      | 🟢D    | clear all type of formatting such as font size or font family or even link and so on                                                                                                      |
| Add to Functionality → Selected Characters                                   | 🟢D    | When highlight it read the number of characters that are selected for example 65 out 121 characters                                                                                       |
| Add to Functionality → Formatted / Markdown syntax in status bar / Detection | 🟢D    | Formatted mean .txt \| Markdown syntax mean .md - the file type and features plus detecting format and auto rendering                                                                     |
| Add to Functionality → Windows (CRLF)                                        | 🟢D    | Windows (CRLF) refers to the line ending style used by Windows operating systems. It tells how a new line is represented inside a text file. - (Python Already handle that automatically) |
| Add to Functionality → UTF-8                                                 | 🟢D    | **UTF-8** refers to the **text encoding** used to save the file. -(use Markdown to render imojies)                                                                                        |

---

| Done | Pending |
| ---- | ------- |
| 🟢D  | 🔴P     |

---

```markdown
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
