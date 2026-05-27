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
- Prevents duplicate file overwrites using automatic filename versioning

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
├── pseudocode.txt
├── breakdown_engine.md
├── requirements.txt
└── .gitignore
```

---

# 🧠 Architecture

The system is built with clear separation of concerns and layered filesystem automation design.

### Architecture Layers

| Layer | Responsibility |
|---|---|
| `scanner.py` | Detects files from the target folder |
| `classifier.py` | Classifies files using extension rules |
| `organizer.py` | Moves files safely into category folders |
| `main.py` | Orchestrates the workflow and summary reporting |
| `pseudocode.txt` | Planning and workflow reasoning |
| `breakdown_engine.md` | Deep engineering dissection, debugging cognition, and structural analysis |

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

# Breakdown Engine

The project includes a dedicated engineering investigation document:

```text
breakdown_engine.md
```

This file dissects the system using a technical detective approach.

It analyzes:

- surface behavior
- line-by-line execution
- variable purpose
- system flow
- edge cases
- structural patterns
- duplicate handling logic
- filesystem safety design

This improves:

- debugging cognition
- architectural understanding
- reasoning transparency
- system extensibility

---


## V1.1 Upgrade — Duplicate File Handling

The organizer now safely handles duplicate filenames.

If a file with the same name already exists inside a category folder, the system automatically generates a new safe filename instead of overwriting the existing file.

Example:

```text
report.pdf
↓
report_1.pdf
↓
report_2.pdf
```

This improves:
- filesystem safety
- collision handling
- automation reliability

---

## Project Status

V1 — Core file organization system  
V1.1 — Added duplicate file handling for safer file routing

---

# Author

Khalid Ishola Abdulkadir