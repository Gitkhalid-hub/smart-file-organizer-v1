# THE FILE ORGANIZER.
# Responsible for moving files into category folders.

from pathlib import Path


class FileOrganizer:

    def organize(self, file_path, category, destination_root):

        # 1. Define source file
        source_file = file_path

        # 2. Create target category folder
        target_category = destination_root / category
        target_category.mkdir(parents=True, exist_ok=True)

        # 3. Build destination path
        destination = target_category / source_file.name
        
        # check duplicates
        if destination.exists():
            counter = 1
            
            while destination.exists():
                # adjusting file name
                new_filename = f"{source_file.stem}_{counter}{source_file.suffix}"
                destination = target_category / new_filename
                counter += 1

        # 4. Move the file
        source_file.rename(destination)

        # 5. Print summary
        print(f"Moved: {source_file.name} → {category}")
        return destination