## 📌 General Notes

* Version 1.0 focuses on developing the Tab System for Overnote — a feature that allows multiple notes (documents) to exist within one shared text editor.

---

## 🖥️ Software Information

| Field Name              | Value                          |
| ----------------------- | ------------------------------ |
| Software Name           | Overnote                       |
| Software Type           | GUI (Graphical User Interface) |
| Software Purpose        | Text Editor                    |
| Software Version        | 1.0                            |
| Software Update Init    | 2025-10-23                     |
| Software Release Update | 2025-10-31                     |
| Software Made By        | Treadway                       |
| Programming Language    | Python                         |
| Code Size (approx.)     | 1168 lines - ※**Medium**※      |
| Level                   | High-Level                     |

---

## 🔄 Updates To The (Tab System) — (Functional & Layout & Logic & Design)

📅 Plan Update — Created on **2025-10-23**

This is Part 2 of the Tab System

We are now introducing a fully dynamic Tab System to Overnote, allowing:

* Unlimited tabs created with a “+” button

* Tabs that can be renamed

* Tabs that can be closed individually

* Each tab’s content saved individually (even when multiple tabs are open)

The design uses one shared text area, and each tab’s content is stored in memory separately and optionally saved to disk.

---

### ⚙️ Overview of the New Tab System

The layout will include two main visual components under the main window:

1. TabBarFrame — top area holding all tab buttons and a “+ New Tab” button.

2. TextEditorFrame — bottom area containing the shared text area widget.

Each tab will store its own content in a Python dictionary or per-tab file.

---

## 🔄 Full Tab System Development Roadmap — Overnote v0.9 (Beginner-Friendly, Expanded)

### 🧱 Logic

🟢D

🔴P

| Feature / Task                            | Status | Detailed Instruction / Value                                                     |
| ----------------------------------------- | ------ | -------------------------------------------------------------------------------- |
| Add to TabSystemFrame → Save Function     | 🟢D    | allow to save from the File menu as a .txt (80% functionality)                   |
| Add to TabSystemFrame → Save As Function  | 🟢D    | allow to save from the File menu as more than one extension                      |
| Add to TabSystemFrame → Open Function     | 🟢D    | allow to open files into the app                                                 |
| Fix the text area widget layout           | 🟢D    | make the text area widget to fill all the empty bottom space                     |
| Bind a left mouse click to the tab button | 🟢D    | when double clicked, it open a small window to change name (No functionality)    |
| Add function to Line Count                | 🟢D    | when a cursor is on line it state that line in numbers                           |
| Add function to Column Count              | 🟢D    | when a cursor is on column it state that column in numbers                       |
| Add function to Character Count           | 🟢D    | state the amount of characters - but set a limit to how much this number can get |
