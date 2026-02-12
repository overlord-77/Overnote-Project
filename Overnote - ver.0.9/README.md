## 📌 General Notes

* Version 0.9 focuses on developing the Tab System for Overnote — a feature that allows multiple notes (documents) to exist within one shared text editor.

* Each tab represents a different note, and clicking between tabs will erase and replace the text area’s content with the correct data stored for that tab.

* This system will allow unlimited tabs, each with rename, close (×), and individual save capabilities.

---

## 🖥️ Software Information

| Field Name              | Value                          |
| ----------------------- | ------------------------------ |
| Software Name           | Overnote                       |
| Software Type           | GUI (Graphical User Interface) |
| Software Purpose        | Text Editor                    |
| Software Version        | 0.9                            |
| Software Update Init    | 2025-10-13                     |
| Software Release Update | 2025-10-23                     |
| Software Made By        | Treadway                       |
| Programming Language    | Python                         |
| Code Size (approx.)     | 1111 lines - ※**Medium**※      |
| Level                   | High-Level                     |

---

## 🔄 Updates To The (Tab System) — (Functional & Layout & Logic & Design)

📅 Plan Update — Created on **2025-10-11**

This is Part 1 of the Tab System

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

### 🧱 Layout & Widget Construction

| Feature / Task                                  | Status | Detailed Instruction / Value                                            |
| ----------------------------------------------- | ------ | ----------------------------------------------------------------------- |
| Add to Overnote.py-> TabSystemFrame             | 🟢 D   | Create a class container inside main window to hold all the tab widgets |
| Add to TabSystemFrame → MainTextArea            | 🟢 D   | the text area class widget for tab reuse                                |
| Add to TabSystemFrame → Variable -> tabs_data   | 🟢 D   | {}       - add an empty dictionary                                      |
| Add to TabSystemFrame → Variable -> current_tab | 🟢 D   | None                                                                    |
| Add to TabSystemFrame → Variable -> tab_count   | 🟢 D   | 0                                                                       |
| Add to TabSystemFrame → function -> new_tab     | 🟢 D   | ()                                                                      |
| Add to TabSystemFrame → function -> switch_tab  | 🟢 D   | (name)                                                                  |
| Add to TabSystemFrame -> add_button             | 🟢 D   | (self, text=“+”, width=40, command=new_tab)                             |
| Add to TabSystemFrame -> add_button.pack()      | 🟢 D   | (side=“right”, padx=5)                                                  |

### new_tab function statusc

| Feature / Task                                  | Status | Detailed Instruction / Value                               |
| ----------------------------------------------- | ------ | ---------------------------------------------------------- |
| Add to new_tab -> global tab_count, current_tab | 🟢 D   | …                                                          |
| Add to new_tab -> tab_count                     | 🟢 D   | += 1                                                       |
| Add to new_tab -> name                          | 🟢 D   | f"Tab {tab_count}"                                         |
| Add to new_tab -> tabs_data[name]               | 🟢 D   | = “”                                                       |
| Add to new_tab -> ctk.CTkButton()               | 🟢 D   | (tab_bar, text=name, command=lambda n=name: switch_tab(n)) |
| Add to new_tab -> button.pack()                 | 🟢 D   | (side=“left”, padx=2)                                      |
| Add to new_tab -> switch_tab()                  | 🟢 D   | (name)                                                     |

### switch_tab function status

| Feature / Task                               | Status | Detailed Instruction / Value                                                           |
| -------------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| Add to switch_tab -> global current_tab      | 🟢 D   | …                                                                                      |
| Add to switch_tab -> if statment             | 🟢 D   | if current_tab:  <br>     tabs_data[current_tab] = main_text_area.get(“1.0”, “end-1c”) |
| Add to switch_tab -> main_text_area.delete() | 🟢 D   | (“1.0”, “end”)                                                                         |
| Add to switch_tab -> main_text_area.insert() | 🟢 D   | (“1.0”, tabs_data[name])                                                               |
| Add to switch_tab -> current_tab = name      | 🟢 D   | assign name to the current_tab                                                         |

| Feature / Task                                                                    | Status    | Detailed Instruction                                                                                                                                                                                                |
| --------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add `TabSystemFrame` to main app window (parent container for all tab components) | 🔴Pending | Create a top-level container inside your main window to hold the tab bar and editor area. Give it padding and make it fill available space. Think: main app layout = menu / TabSystemFrame / status bar (optional). |
| Create `TabBarFrame` (top area for tabs and + button)                             | 🔴Pending | Inside `TabSystemFrame` add a horizontal container for tabs. Reserve space on the far right for the “+” button. Use consistent horizontal padding.                                                                  |
| Create `TextEditorFrame` (below TabBarFrame for shared text area)                 | 🔴Pending | Place a large container below the tab bar. This will hold the single shared text widget and scrollbars. Make it expand with the window.                                                                             |
| Add shared text widget inside `TextEditorFrame`                                   | 🔴Pending | Use one text editing widget (e.g., a text box) with word-wrap and vertical scrollbar. Assign a clear font and insert-caret color. Make sure the widget supports `get` and `delete` operations.                      |
| Add a right-aligned “+ New Tab” button inside `TabBarFrame`                       | 🔴Pending | Place a button visually separated from tabs. Clicking it triggers the tab creation flow (see Detailed Tab Creation steps).                                                                                          |
| Make tab area horizontally scrollable (if many tabs)                              | 🔴Pending | If tabs overflow, let the tab row scroll horizontally. Use a canvas or scrollable frame inside `TabBarFrame` so users can reach all tabs.                                                                           |
| Reserve space for a per-tab close icon (×)                                        | 🔴Pending | Each tab needs a small close control near its label. Plan small hit area and spacing to avoid accidental clicks.                                                                                                    |
| Provide visual spacing for the active tab and inactive ones                       | 🔴Pending | Make active tab visually distinct (background, underline, or border). Keep inactive tabs neutral. Decide on colors and corner radius.                                                                               |

---

### 🧩 Tab Creation & Representation (UI & Data)

| Feature / Task                                            | Status    | Detailed Instruction                                                                                                                                                                                                                                             |
| --------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Decide tab identity model (label + unique id + file_path) | 🔴Pending | Every tab should have: **display name** (what user sees), **internal id** (unique string/number used internally), and **file_path** (None or full path). Internal id ensures renaming doesn’t break references.                                                  |
| Use a dictionary or map to hold per-tab data              | 🔴Pending | Plan: `tabs_data[tab_id] = {"name": display_name, "content": "...", "file_path": None, "dirty": False, "widget_refs": {...}}`. The `dirty` flag marks unsaved edits. `widget_refs` can store the tab UI frame/button references for easy destruction or updates. |
| Create small frame for each tab (label + close button)    | 🔴Pending | For each new tab, build a compact composite: clickable label area (selects the tab) and a tiny close button to the right. Keep both inside a small frame so you can pack/destroy it easily.                                                                      |
| Generate unique internal tab IDs                          | 🔴Pending | When adding a tab, create a sequential or timestamp-based id (e.g., `tab_1`, `tab_2`, or `id_169...`) to avoid collisions when names are duplicate.                                                                                                              |
| Default names for new tabs                                | 🔴Pending | When user creates a tab, give it a default display name like “Untitled” or “New Tab 1”. Track count to avoid duplicates in names.                                                                                                                                |

---

### 🧠 Class & Method Structure (Design, no code)

| Feature / Task                                            | Status    | Detailed Instruction                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a top-level class `OvernoteApp` to host everything | 🔴Pending | The class is responsible for GUI creation, data, and logic. Use instance attributes for frames, text widget, and `tabs_data`.                                                                                                                                                                                                                                                                       |
| Plan the main attributes                                  | 🔴Pending | Suggested attributes: `self.tab_system_frame`, `self.tab_bar`, `self.editor_frame`, `self.text_widget`, `self.tabs_data` (dict), `self.active_tab_id` (None initially), `self.tab_count` (int), `self.session_file` (optional path).                                                                                                                                                                |
| Plan the key methods (names and responsibilities)         | 🔴Pending | Example method responsibilities (implement later): `initialize_ui()`, `add_new_tab(name=None, content=None, file_path=None)`, `switch_tab(tab_id)`, `close_tab(tab_id)`, `rename_tab(tab_id, new_name)`, `save_current_tab()`, `save_tab_to_file(tab_id, path=None)`, `open_file_to_tab(path)`, `load_session()`, `save_session()`, `mark_tab_dirty(tab_id, True/False)`, `highlight_active_tab()`. |
| Keep UI logic and data handling separated                 | 🔴Pending | UI methods should call data methods, and data methods should not directly manipulate UI widgets — instead return values or call small UI-updater helpers. This separation makes debugging simpler.                                                                                                                                                                                                  |

---

### ➕ Detailed Steps: Add New Tab Flow (very granular)

| Feature / Task                                           | Status    | Detailed Instruction                                                                                                                 |
| -------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Button click triggers `add_new_tab`                      | 🔴Pending | Clicking “+” starts a linear flow: generate id, create data entry, create UI, make it active.                                        |
| Generate new internal tab id and display name            | 🔴Pending | Use incremental counter: increment `tab_count`, set id = `tab_{tab_count}`, display name = `Untitled` + number.                      |
| Create the tab data entry in `tabs_data`                 | 🔴Pending | Add a dict entry with empty content, file_path=None, dirty=False.                                                                    |
| Build tab UI frame (label + close) and pack into tab bar | 🔴Pending | Create label element (clickable) and close button. Bind the click event to `switch_tab(tab_id)`. Pack to left before the “+” button. |
| Set new tab as active and load its content               | 🔴Pending | Call `switch_tab(new_id)` so the text area is cleared and new (empty) content inserted.                                              |
| Handle focus and caret position on new tab               | 🔴Pending | After switching, focus the text widget and move caret to end so user can start typing immediately.                                   |
| Update tab counter / UI elements                         | 🔴Pending | If you show tab counts or tooltips, update them now.                                                                                 |

---

### ↔️ Detailed Steps: Switch Tab Flow (very granular)

| Feature / Task                                          | Status    | Detailed Instruction                                                                                                                                          |
| ------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User clicks a tab label → call `switch_tab(tab_id)`     | 🔴Pending | Event binding should pass the internal tab id, not the display name.                                                                                          |
| Save current tab before switching                       | 🔴Pending | If `active_tab_id` is set: read text from text widget, store to `tabs_data[active_tab_id]["content"]`, and set `dirty` flag based on whether content changed. |
| Optionally, auto-save to file on switch                 | 🔴Pending | If you want, write that tab’s content to its `file_path` on switch. This is per-tab saving behavior.                                                          |
| Clear text widget, then insert selected tab content     | 🔴Pending | Delete the editor content and insert `tabs_data[tab_id]["content"]`. If empty, leave blank.                                                                   |
| Update `active_tab_id` and highlight UI                 | 🔴Pending | Set `active_tab_id = tab_id` and update visual highlight for tabs. Reset unsaved indicator if saved.                                                          |
| Ensure scroll position / selection resets appropriately | 🔴Pending | Optionally set view to line 1 or remember scroll per tab for better UX.                                                                                       |

---

### ✖️ Detailed Steps: Close Tab Flow (very granular)

| Feature / Task                                                 | Status    | Detailed Instruction                                                                                                                        |
| -------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| User clicks tab “×” → call `close_tab(tab_id)`                 | 🔴Pending | Bind close click to the internal id.                                                                                                        |
| Confirm unsaved changes (optional)                             | 🔴Pending | If `tabs_data[tab_id]["dirty"]` is true, prompt the user: Save / Discard / Cancel. Implement modal confirmation.                            |
| If Save chosen → perform `save_tab_to_file(tab_id)` or Save As | 🔴Pending | Use the file_path if exists, else open Save As dialog.                                                                                      |
| Remove tab data and UI                                         | 🔴Pending | Destroy the tab UI frame and delete `tabs_data[tab_id]`.                                                                                    |
| Choose new active tab (if closed tab was active)               | 🔴Pending | If the closed tab was active, choose the nearest left tab; if none, choose the first available; if no tabs left, create a new untitled tab. |
| Update counters / session state                                | 🔴Pending | Decrement counters, update session storage, and UI.                                                                                         |

---

### ✍️ Rename Tab Flow (very granular)

| Feature / Task                                       | Status    | Detailed Instruction                                                                                                                           |
| ---------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Trigger rename via double-click or context menu      | 🔴Pending | Bind a double-click on the tab label or add “Rename” in a right-click menu.                                                                    |
| Replace label temporarily with a small input control | 🔴Pending | Overlay a small entry field in the tab frame; prefill with current name and focus it.                                                          |
| On Enter or focus-out, commit change                 | 🔴Pending | Validate new name (non-empty). Update `tabs_data[tab_id]["name"]` and update the visible label. Restore clickable label view.                  |
| Keep file_path separate                              | 🔴Pending | Renaming a tab label should not change `file_path`. If user wants the file renamed on disk, provide a separate “Save As / Rename File” action. |

---

### 💾 File Handling (Open / Save / Save As / Per-tab files)

| Feature / Task                                                 | Status    | Detailed Instruction                                                                                                                                                                                                                    |
| -------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add `file_path` property for each tab                          | 🔴Pending | When creating tab data, include `file_path=None`. When opening or saving, update this.                                                                                                                                                  |
| Implement `open_file_to_tab(path)` flow                        | 🔴Pending | On Open-dialog selection: read file content; if file already open (check file_path in `tabs_data`), switch to that tab; else, create a new tab with display name = basename(path), content = file contents, and set `file_path = path`. |
| Per-tab save logic (`save_tab_to_file(tab_id, optional_path)`) | 🔴Pending | If tab has `file_path`, write content to it. If not, call Save As dialog to get path and then save and set `file_path`. Clear `dirty` flag after successful save.                                                                       |
| Ensure saving one tab doesn’t affect others                    | 🔴Pending | Always use `tab_id` to fetch content and path. Do not iterate through other tabs unless performing bulk save.                                                                                                                           |
| Add Save As flow                                               | 🔴Pending | Prompt user for destination path, update `file_path`, then save. Optionally update display name to the new basename.                                                                                                                    |
| Session persistence (optional)                                 | 🔴Pending | Save `tabs_data` metadata (names, file_paths, maybe contents) in a JSON on exit. On startup, restore tabs. Decide whether to restore unsaved content (contents in JSON) or only file associations.                                      |
| Handle file IO errors gracefully                               | 🔴Pending | Surround file reads/writes with try/except. If error, show informative message (permission denied, disk full, encoding error).                                                                                                          |

---

### 🧪 Dirty State, Autosave & Data Safety

| Feature / Task                                       | Status    | Detailed Instruction                                                                                                                                                     |
| ---------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Track `dirty` flag per tab (changes since last save) | 🔴Pending | When user edits text in editor, compare current text to stored content; if different, set `dirty=True`. Show indicator on tab label (e.g., `*`) to mark unsaved changes. |
| Hook text change detection                           | 🔴Pending | Add a small event handler to detect edits (e.g., on key press or after a short delay) and mark tab dirty. Debounce to avoid performance issues.                          |
| Per-tab autosave option (optional)                   | 🔴Pending | If enabled, on every switch or after timed interval, auto-write content to associated file. Respect user preference and only autosave when file_path exists.             |
| Crash recovery (session restore)                     | 🔴Pending | On exit, write session file containing tabs, file_paths, and unsaved contents. On next launch, prompt user to recover unsaved tabs.                                      |

---

### 🎨 Visual / UX Enhancements (practical steps)

| Feature / Task                             | Status    | Detailed Instruction                                                                                                          |
| ------------------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Highlight active tab                       | 🔴Pending | Change background/fill or underline for the active tab’s frame. Keep the change small but noticeable.                         |
| Mark unsaved tabs visually                 | 🔴Pending | Add an asterisk or different font weight for dirty tabs.                                                                      |
| Add hover effect on tabs                   | 🔴Pending | On mouse enter on a tab, slightly change background or show a tooltip with file path. On leave, revert.                       |
| Make tab close button small and accessible | 🔴Pending | Use a square hit area that’s not too small; consider confirming double closings if many tabs exist.                           |
| Tab reorder (optional, advanced)           | 🔴Pending | Optional future feature: allow dragging tabs left/right to reorder. If implemented, ensure `tabs_data` order is also tracked. |

---

### 🔧 Error Handling / Edge Cases / Defensive Steps

| Feature / Task                                         | Status    | Detailed Instruction                                                                                              |
| ------------------------------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------- |
| Prevent duplicate tab names confusing the user         | 🔴Pending | Display full file path on hover tooltip when names match. Use internal id for logic, not name.                    |
| What to do when user renames a tab to an existing name | 🔴Pending | Allow duplicates but warn on Save if it would overwrite an existing file.                                         |
| Closing last tab behavior                              | 🔴Pending | If last tab closed, create a new blank tab automatically rather than leaving editor empty.                        |
| Prevent accidental close when many unsaved tabs        | 🔴Pending | On app exit, if any tab is dirty, prompt Save All / Cancel / Don’t Save.                                          |
| File encoding problems                                 | 🔴Pending | If reading file fails due to encoding, try alternative encodings or show an error and suggest Save As with UTF-8. |

---

### 🧭 Integration With Main Application (where to place things)

| Feature / Task                                               | Status    | Detailed Instruction                                                                                                                                      |
| ------------------------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add TabSystemFrame below main menu / toolbar                 | 🔴Pending | Keep the menu intact; TabSystemFrame is the main app body below it.                                                                                       |
| Ensure resizing works across frames                          | 🔴Pending | All major frames (TabSystemFrame, TextEditorFrame) should be set to expand/shrink with window. Check text widget stretch and tab bar alignment on resize. |
| Replace older per-document editors with single shared editor | 🔴Pending | Remove separate editors and centralize editing to the single shared text area. All tab content swaps through `switch_tab`.                                |
| Keep everything class-based for clarity                      | 🔴Pending | One class for the app; consider small helper classes later for Tab objects if needed (advanced).                                                          |

---

### ✅ Testing Checklist (follow this as you implement)

| Test Item                                                                                 | Pass? |
| ----------------------------------------------------------------------------------------- | ----- |
| Create new tab — it appears and becomes active                                            | ☐     |
| Type text in a tab, switch to another tab, switch back — text persists                    | ☐     |
| Add many tabs until overflow — tab bar scrolls / remains usable                           | ☐     |
| Close a tab with unsaved changes — prompt appears                                         | ☐     |
| Open a file — new tab created and named with filename                                     | ☐     |
| Open same file twice — no duplicate tab is created; instead, app switches to existing tab | ☐     |
| Save tab with and without file_path — behaves correctly (Save / Save As)                  | ☐     |
| Rename tab — label updates; file_path unchanged unless user chooses Save As               | ☐     |
| App restart with session restore — tabs & unsaved content recovered (if implemented)      | ☐     |
| File IO error situations show friendly messages                                           | ☐     |

---

### 🛠️ Debugging Tips (simple, beginner-friendly)

* Work in tiny steps: implement one feature, test it, then move on.

* Use print/log messages to verify data: print `tabs_data` after adding a tab to ensure it contains expected keys.

* If `switch_tab` fails, log `active_tab_id` and the target `tab_id` to find mismatches.

* If UI doesn’t update, verify that the tab UI frame references are stored and not garbage collected.

* When file saves fail, check the path and permissions; try saving to Desktop to confirm.

* Use simple filenames (no unusual characters) while testing to avoid encoding/path issues.

* Back up your work: keep a copy of your workspace before large refactors.

---

### 🧾 Session/Project Organization Advice (for you as beginner)

* Implement everything inside a single class first (clear structure).

* Keep a separate small file or directory for session files (e.g., `.overnote/session.json`) rather than cluttering project root.

* Keep UI creation separate from logic functions in your file: `create_ui()` vs `create_logic()` style (conceptual separation).

* Write short comments near each major step so you can remember why you did it.

* Use version control (git) — commit early and often so you can roll back if something breaks.

---

### Suggested Sequence to Implement (the safest path for a beginner)

1. Create the basic UI frames (menu, TabSystemFrame, TabBarFrame, TextEditorFrame).

2. Add shared text widget and ensure it resizes.

3. Implement an `add_new_tab()` that only creates UI and an empty data entry - test creating tabs.

4. Implement `switch_tab()` that saves current content (in memory) and loads the new tab’s content - test switching.

5. Implement close (×) button flow safely (prompt if dirty).

6. Implement rename via double-click (simple entry overlay).

7. Add per-tab file_path and implement open-file flow with auto-naming.

8. Implement individual save / save as for active tab.

9. Add dirty flag tracking and visual unsaved indicator.

10. Add session save/restore and autosave (optional, last).

11. Polish visuals: hover, active highlight, scrollable tab bar.

---

If you want, next I can:

* Produce a **class method map** (one-line descriptions of each method and expected inputs/outputs) that you can copy into a TODO list as you code — still no runnable code, just method names and behavior.

* Or — when you’re ready — I can generate the **actual class-based Python prototype** (full code) that implements everything above (you said don’t want code right now; tell me when to produce it).

Which of those two would you like next?
