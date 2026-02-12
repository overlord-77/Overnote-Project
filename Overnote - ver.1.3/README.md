## 📌 General Notes

* Version 1.3 focuses on giving the View menu and status bar and the center main widgets a functionalit

* so basically in version 1.4 it would be called the renovation - re do what i need to redo to fit the markdown syntax tag system

---

## 🖥️ Software Information

| Field Name              | Value                          |
| ----------------------- | ------------------------------ |
| Software Name           | Overnote                       |
| Software Type           | GUI (Graphical User Interface) |
| Software Purpose        | Text Editor                    |
| Software Version        | 1.3                            |
| Software Update Init    | 2025-11-17                     |
| Software Release Update | 2025-12-11                     |
| Software Made By        | Treadway                       |
| Programming Language    | Python                         |
| Code Size (approx.)     | 2452 lines - ※**Medium**※      |
| Level                   | High-Level                     |

---

## 🔄 Updates To The (View Menu & Center Main Menu Widgets & Status bar) — (Functional & Logic)

📅 Plan Update — Created on **2025-11-16**

---

| Done | Pending |
| ---- | ------- |
| 🟢D  | 🔴P     |

---

| Feature / Task                                                   | Status | Detailed Instruction / Value                                                                                                                                |
| ---------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add to Functionality → Zoom                                      | 🟢D    | Zoom in - Zoom Out - Restore default zoom                                                                                                                   |
| Add to Functionality → Status Bar                                | 🟢D    | The bottom Bar line, column count, etc. - (🟢D - in v 0.7)                                                                                                  |
| Add to Functionality → Word Wrap                                 | 🟢D    | On = automatically wrap to next line when reaches the edge. - Off = continue on the same line                                                               |
| Add to Functionality → Markdown                                  | 🟢D    | On = when file ext is .md - allow to write markdown syntax and turn it to formatted - (Functional 70%)                                                      |
| Add to Functionality → H1                                        | 🟢D    | different type of font size such as headings and subheadings                                                                                                |
| Add to Functionality → List Type                                 | 🟢D    | bulleted list and numbered list                                                                                                                             |
| Add to Functionality → Bold                                      | 🟢D    | set text to bold                                                                                                                                            |
| Add to Functionality → Italicc                                   | 🟢D    | set text to italic                                                                                                                                          |
| Add to Functionality → Link                                      | 🔴P    | allow you to add a link as it is or set a name for the link and add it - (Unfinished)                                                                       |
| Add to Functionality → Clear Formatting                          | 🔴P    | clear all type of formatting such as font size or font family or even link and so on - (Unfinished)                                                         |
| Add to Functionality → Ln/Col/Characters                         | 🟢D    | the count for lines, column and character from the text widget (🟢D - in v 0.7)                                                                             |
| Add to Functionality → Characters                                | 🔴P    | When highlight it read the number of characters that are selected for example 65 out 121 characters - (Unfinished)                                          |
| Add to Functionality → Formatted / Markdown syntax in status bar | 🔴P    | Formatted mean .txt \| Markdown syntax mean .md - the file type and features - (Unfinished)                                                                 |
| Add to Functionality → Zoom Percentage                           | 🟢D    | Zoom normal = 100% - 14pt \| Zoom in max = 500% - 70pt \| Zoom out max = 14% - 2pt                                                                          |
| Add to Functionality → Windows (CRLF)                            | 🔴P    | Windows (CRLF) refers to the line ending style used by Windows operating systems. It tells how a new line is represented inside a text file. - (Unfinished) |
| Add to Functionality → UTF-8                                     | 🔴P    | **UTF-8** refers to the **text encoding** used to save the file. - (Unfinished)                                                                             |

Notes:

> > > > > > > > > > > --------------------------------------------------------<<<<<<<<<<<<<<<<<

> > > > > > > > > > > --------------------------------------------------------<<<<<<<<<<<<<<<<<

> > > > > > > > > > > --------------------------------------------------------<<<<<<<<<<<<<<<<<

-—- what i need to fix is that

-> when i open the software (by defualt): all the text inside of the text area widget will be as plain text or markdown syntax

- that file type will change from plain text or markdown syntax to formmated when ever i add fromatting to the text in the text widget like chaning the font

-> when i open a file that is (file.md) the software will open with text widget converted to forrmatted and you will be able to toggle to markdown Syntax

-> when i open a file that is (file.txt) the software will open with text widget as plain text, it won’t have the mark down sytnax to formatted toggle enabled

- but if i add any kind of formatting to the text widget of a file.txt then it will be converted to formatted therefore you can switch from formatting to markdown syntax

[youtube.com](# "ttest")

what i need to change is that

when i add a bold text  it acutally get added as  **bold text**

when i add an italix text  it acutally get added as *italic text*

this is a bulleted list = * sdfdsfsdf

this is a numbered list = 1. sdfsdf

or when i add alink it acutally get added as [Youtube][https://www.youtube.com/](https://www.youtube.com/ "https://www.youtube.com/"))

therefore it actually change the markdown syntax to formatted automatic when ever i open a file or click the toggle formated to makrdown or vice versa

----->>>> so for example: if i open my software and then i decied to type a senected and then decided to use the bold function, what happen is that the word that i select

using the mouse is that when i click the bold function it actuall at ** at the beginning and end of that world or select text then imdeadtyl my software detect taht

there is some markdown syntax therefore it turn it to a formatted document which then the word that is bold turn from this **bold text** to this bold text as bolded

> > > > > > > > > > > --------------------------------------------------------<<<<<<<<<<<<<<<<<

> > > > > > > > > > > --------------------------------------------------------<<<<<<<<<<<<<<<<<

> > > > > > > > > > > --------------------------------------------------------<<<<<<<<<<<<<<<<<

* - the main center widget will disappear when markdown is enable

the formatted / markdown syntax in the status bar will also change between too when applicable

the markdown button in the menu will be gray and unclickable until the file is an actual .md

the percentage of zoom in the status bar will also change when zooming in or out using the menu

Note For Problems:

- you must think of all outcomes like the fact that the logic of the link will disappear after switching tabs or saving it will not save the funcstion

- the main center widget will disappear when markdown is enable

the formatted / markdown syntax in the status bar will also change between too when applicable

the markdown button in the menu will be gray and unclickable until the file is an actual .md

the percentage of zoom in the status bar will also change when zooming in or out using the menu

Note For Problems:

- you must think of all outcomes like the fact that the logic of the link will disappear after switching tabs or saving it will not save the funcstion
