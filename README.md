# SMART FILE ORGANIZER V1

A Python-based automation tool that scans a folder, classifies files by extension, and automatically organizes them into category folders.

---

# Features

- Scans folders for files
- Classifies files using extensions
- Automatically creates category folders
- Moves files into matching folders
- Handles unknown file types safely
- Prints organization summary after execution

---

# Project Structure

```text
SMART_FILE_ORGANIZER_V1/
│
├── core/
│   ├── __init__.py
│   ├── scanner.py
│   ├── classifier.py
│   └── organizer.py
│
├── test_folder/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── pseudocode.txt
```

---

# Architecture Overview

## FolderScanner

Responsible for:
- scanning folders
- returning files only

---

## FileClassifier

Responsible for:
- extracting file extensions
- deciding file categories

---

## FileOrganizer

Responsible for:
- creating category folders
- moving files into destination folders

---

## main.py

Responsible for:
- coordinating the full workflow
- summary reporting

---

# Categories

Current supported categories:

- documents → .pdf, .docx, .txt
- images → .jpg, .jpeg, .png
- code → .py, .js
- others → unknown extensions

---

# Example Output

```text
Moved: report.pdf → documents
Moved: image.png → images

=== ORGANIZATION SUMMARY ===
20
{'documents', 'images', 'others'}

Organization completed successfully
```

---

# Technologies Used

- Python
- pathlib
- Object-Oriented Programming (OOP)
- File System Automation

---

# Future Improvements

Potential future upgrades:

- duplicate file handling
- recursive folder scanning
- logging system
- smart renaming
- real-time watch mode
- configuration support

---

# Learning Focus

This project was built to practice:

- system design thinking
- responsibility separation
- filesystem automation
- modular architecture
- Python OOP principles

---

# Author

Khalid Ishola Abdulkadir