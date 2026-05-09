# FOLDER SCANNER LOGIC: Responsible for finding files.

class FolderScanner:

    def scan(self, folder_path):

        # checking if the folder exists
        if not folder_path.exists():
            raise FileNotFoundError(
                f"Input folder does not exist: {folder_path}")

        # getting all files inside the folder
        files = [file for file in folder_path.iterdir() if file.is_file()]
        return files