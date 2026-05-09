# THE MAIN FLOW

from pathlib import Path # or just use the OS module: import os
from core.scanner import FolderScanner
from core.organizer import FileOrganizer
from core.classifier import FileClassifier

folder_path = Path("C:\\Users\\KHIDDAFA\\PycharmProjects\\SMART_FILE_ORGANIZER_V1\\test_folder")

scanner = FolderScanner()
organizer = FileOrganizer()
classifier = FileClassifier()

files = scanner.scan(folder_path)

total_files = len(files)
categories_used = set()

for file in files:
	category = classifier.classify(file)
	organizer.organize(file, category, folder_path)
	categories_used.add(category)
	
print("=== ORGANIZATION SUMMARY ===")
print(total_files)
print(categories_used)
print("Organization completed successfully")