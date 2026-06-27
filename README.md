# File organizer

A python application that automatically organizes files into folders based on their file type. The project includes both a command line interface (CLI) abd a graphical user interface (GUI) built with PyQt5.

## Features
- Organizes files into categories based on their extensions.
- Automatically creates folders for each category
- Preventing overwriting existing files by automatically renaming duplicates
- An undo feature that restores moved files to their original locations during the current session
- Command line interface and a GUI

## Supported Categories
- Images
- Audio
- Video
- Documents
- Spreadsheets
- Presentations
- Archives
- Code
- Executables
- Fonts
- Ebooks

Files with unsupported extensions are placed in an Other folder.

## Project Structure
```
. 
├── organizer.py # Core organizing logic and CLI application 
├── gui.py # PyQt5 graphical interface 
├── gui.ui # Qt Designer UI file 
└── README.md
```

## Technologies used
- Python 3
- PyQt5

## Usage
### Command Line Interface
Run :
```bash
python organizer.py
```
You can also provide the folder path as a command-line argument:

```bash
python organizer.py "C:\Users\Username\Downloads"
```
### Graphical User Interface

Run:

```bash
pip inn
python gui.py
```

Then:

1. Click **Browse** to select a folder (or type the folder path manually).
2. Click **Organize** to sort the files.
3. Click **Undo** if you want to restore the changes made during the current session.

## What I learned
This project helped me practice,
* Working with the file system using `pathlib`
* Building reusable functions that can be shared between multiple interfaces
* Creating desktop applications with PyQt5
* Handling duplicate filenames

## Future Improvements
- Support for organizing files recursively through subfolders
- Allow users to customize file categories and extensions
- Package the application as a 