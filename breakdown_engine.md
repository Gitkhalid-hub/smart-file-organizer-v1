# 🧩 Breakdown Engine — Smart File Organizer

> **Technical Detective Lens:** This document dissects each module of the project, highlighting functionality, structure, edge cases, and design patterns.

---

## Module Links

- 🛠️ [FolderScanner — `core/scanner.py`](core/scanner.py)
- 🛠️ [FileClassifier — `core/classifier.py`](core/classifier.py)
- 🛠️ [FileOrganizer — `core/organizer.py`](core/organizer.py)
- 🛠️ [Orchestration — `main.py`](main.py)

---

## 1️⃣ Surface Behavior

> What does the project output at a glance?

<details>
<summary>Smart File Organizer</summary>

```python
files = scanner.scan(folder_path)

for file in files:
    category = classifier.classify(file)
    organizer.organize(file, category, folder_path)
    categories_used.add(category)
```

This system:

- Scans a folder.
- Detects files only.
- Classifies each file by extension.
- Creates category folders.
- Moves each file into its category folder.
- Handles unknown extensions using `others`.
- Prevents duplicate overwrites using filename versioning.
- Prints a final organization summary.

</details>

---

## 2️⃣ Line-by-Line Behavior

> Inspect each major module for concrete action.

<details>
<summary>FolderScanner — Detecting Files</summary>

```python
class FolderScanner:
```

Creates the scanner component.

```python
def scan(self, folder_path):
```

Defines the method that receives the target folder path.

```python
if not folder_path.exists():
    raise FileNotFoundError(
        f"Input folder does not exist: {folder_path}"
    )
```

Checks whether the folder exists. If not, the system stops safely with a clear error.

```python
files = [file for file in folder_path.iterdir() if file.is_file()]
```

Loops through the folder and keeps only files.

This ignores folders because:

```python
file.is_file()
```

only returns `True` for actual files.

```python
return files
```

Returns the list of detected files.

</details>

<details>
<summary>FileClassifier — Deciding Categories</summary>

```python
category_rules = {
    "documents": [".pdf", ".docx", ".txt"],
    "images": [".jpg", ".jpeg", ".png"],
    "code": [".py", ".js"],
}
```

Defines the classification rules.

```python
extension = file_path.suffix
```

Extracts the file extension.

Example:

```text
report.pdf → .pdf
image.png → .png
script.py → .py
```

```python
for category_name, extensions in category_rules.items():
```

Loops through each category and its supported extensions.

```python
if extension in extensions:
    return category_name
```

If the file extension matches a category rule, return that category.

```python
return "others"
```

If no rule matches, fallback safely to `others`.

</details>

<details>
<summary>FileOrganizer — Moving Files Safely</summary>

```python
source_file = file_path
```

Stores the current file being moved.

```python
target_category = destination_root / category
```

Builds the destination category folder.

Example:

```text
test_folder / documents
test_folder / images
test_folder / others
```

```python
target_category.mkdir(parents=True, exist_ok=True)
```

Creates the category folder if it does not already exist.

```python
destination = target_category / source_file.name
```

Builds the first intended destination path.

Example:

```text
documents/report.pdf
```

```python
if destination.exists():
```

Checks whether a file with the same name already exists.

```python
counter = 1
```

Starts duplicate numbering.

```python
while destination.exists():
```

Keeps generating new names until a safe unused filename is found.

```python
new_filename = f"{source_file.stem}_{counter}{source_file.suffix}"
```

Creates duplicate-safe names.

Example:

```text
report.pdf
↓
report_1.pdf
↓
report_2.pdf
```

```python
destination = target_category / new_filename
```

Updates the destination path with the new filename.

```python
counter += 1
```

Increases the counter for the next possible duplicate.

```python
source_file.rename(destination)
```

Moves the file into the final safe destination path.

```python
print(f"Moved: {source_file.name} → {category}")
```

Prints visible feedback.

```python
return destination
```

Returns the final moved path.

</details>

<details>
<summary>main.py — Workflow Orchestration</summary>

```python
scanner = FolderScanner()
organizer = FileOrganizer()
classifier = FileClassifier()
```

Creates the project components.

```python
files = scanner.scan(folder_path)
```

Gets all files from the target folder.

```python
total_files = len(files)
categories_used = set()
```

Creates summary state.

```python
for file in files:
```

Processes each file one by one.

```python
category = classifier.classify(file)
```

Classifies the current file.

```python
organizer.organize(file, category, folder_path)
```

Moves the file into the correct category folder.

```python
categories_used.add(category)
```

Tracks which categories were used.

```python
print("=== ORGANIZATION SUMMARY ===")
print(total_files)
print(categories_used)
print("Organization completed successfully")
```

Prints final workflow summary.

</details>

---

## 3️⃣ Variable Purpose

<details>
<summary>Important Variables</summary>

| Variable | Purpose |
|---|---|
| `folder_path` | Root folder being organized |
| `files` | List of files detected by `FolderScanner` |
| `file` | Current file being processed in the loop |
| `file_path` | Path object passed into classifier/organizer |
| `category_rules` | Mapping of categories to allowed extensions |
| `extension` | File suffix used for classification |
| `category` | Classification result for a file |
| `destination_root` | Root folder where category folders are created |
| `target_category` | Specific folder for one category |
| `destination` | Final file destination path |
| `counter` | Number used for duplicate filename versioning |
| `categories_used` | Set of categories encountered during execution |
| `total_files` | Number of files detected before organization |

</details>

---

## 4️⃣ System Flow

<details>
<summary>Full Workflow</summary>

```text
main.py
↓
set folder_path
↓
FolderScanner.scan(folder_path)
↓
return list of files
↓
for each file
↓
FileClassifier.classify(file)
↓
return category
↓
FileOrganizer.organize(file, category, folder_path)
↓
create category folder
↓
check duplicate filename
↓
move file safely
↓
update summary state
↓
print final summary
```

</details>

<details>
<summary>Duplicate Handling Flow</summary>

```text
destination path created
↓
does destination exist?
↓
yes
↓
create counter
↓
generate filename with counter
↓
check again
↓
repeat until unused name is found
↓
move file
```

</details>

---

## 5️⃣ Edge Cases

<details>
<summary>Possible Failures</summary>

- Input folder does not exist.
- Folder contains no files.
- Folder contains only subfolders.
- File extension is not recognized.
- Destination category folder already exists.
- Destination file name already exists.
- File cannot be moved because it is open in another program.
- Permission error prevents folder creation or file movement.
- Duplicate loop must keep generating names until a safe path is found.

</details>

---

## 6️⃣ Structural Pattern

<details>
<summary>Scanner → Classifier → Organizer Pattern</summary>

The project uses a clean three-stage automation pipeline:

```text
scan
↓
classify
↓
organize
```

Each module owns one responsibility:

| Module | Responsibility |
|---|---|
| `FolderScanner` | Detect files |
| `FileClassifier` | Decide category |
| `FileOrganizer` | Move files safely |
| `main.py` | Connect the workflow |

</details>

<details>
<summary>Dictionary Rule Mapping</summary>

```python
category_rules = {
    "documents": [".pdf", ".docx", ".txt"],
    "images": [".jpg", ".jpeg", ".png"],
    "code": [".py", ".js"],
}
```

This pattern maps:

```text
extension
↓
category
```

It keeps classification rules centralized and easy to modify.

</details>

<details>
<summary>Collision Resolution Pattern</summary>

```python
while destination.exists():
    new_filename = f"{source_file.stem}_{counter}{source_file.suffix}"
    destination = target_category / new_filename
    counter += 1
```

This is a retry-generation pattern:

```text
generate candidate
↓
validate candidate
↓
retry if invalid
```

This appears in:

- file upload systems
- backup systems
- cloud storage
- synchronization tools
- caching systems

</details>

---

## 7️⃣ Reframe / Visualize

<details>
<summary>Category Table</summary>

| File Example | Extension | Category |
|---|---|---|
| `report.pdf` | `.pdf` | `documents` |
| `photo.png` | `.png` | `images` |
| `script.py` | `.py` | `code` |
| `installer.exe` | `.exe` | `others` |

</details>

<details>
<summary>Duplicate Example</summary>

| Existing File | Incoming File | Final Name |
|---|---|---|
| `report.pdf` | `report.pdf` | `report_1.pdf` |
| `report_1.pdf` | `report.pdf` | `report_2.pdf` |
| `image.png` | `image.png` | `image_1.png` |

</details>

---

## 8️⃣ Project Data Shape

<details>
<summary>Before Run</summary>

```text
test_folder/
├── report.pdf
├── image.png
├── script.py
└── installer.exe
```

</details>

<details>
<summary>After Run</summary>

```text
test_folder/
├── documents/
│   └── report.pdf
│
├── images/
│   └── image.png
│
├── code/
│   └── script.py
│
└── others/
    └── installer.exe
```

</details>

---

## 9️⃣ Insights & Recommendations

- ✅ `FolderScanner` correctly ignores folders.
- ✅ `FileClassifier` keeps rules centralized.
- ✅ `FileOrganizer` owns file movement and collision handling.
- ✅ `main.py` owns orchestration and summary state.
- ✅ V1.1 duplicate handling improves filesystem safety.
- ⚠️ Consider filtering already-organized category folders if recursive scanning is added later.
- ⚠️ Consider case-insensitive extensions later, such as `.PDF` and `.JPG`.
- ⚠️ Consider logging moved files in a future upgrade.
- ⚠️ Consider separating source folder and destination folder in future versions.

---

## ⚡ 8-Step Truth-Finding Approach

Use this when debugging or extending the project:

1. Surface Behavior
2. Line-by-Line Behavior
3. Variable Purpose
4. System Flow
5. Edge Cases
6. Structural Pattern
7. Reframe / Visualize
8. Insights & Recommendations

---

## 🧠 Final Detective Summary

Smart File Organizer is a filesystem automation pipeline.

Its core intelligence comes from:

```text
file detection
↓
extension-based classification
↓
safe destination routing
↓
duplicate collision handling
```

The most important V1.1 upgrade is duplicate-safe routing.

That means the system no longer blindly moves files into a folder. It first checks whether the destination is safe.

The key engineering idea:

```text
Automation should not only act.
Automation should act safely.
```