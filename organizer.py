import sys
from pathlib import Path


def main():
    if len(sys.argv) == 2:
        selected_folder = Path(sys.argv[1])

    else:
        selected_folder = Path(input("Select a folder: "))

    if (not selected_folder.is_dir()) or (not selected_folder.exists()):
        print("Folder not found")
        return

    main_logic(selected_folder)

    # Undo function
    while True:
        undo = input("undo changes? (y/n): ").lower()
        if undo in ("y", "yes", "n", "no"):
            break
    if undo == "y" or undo == "yes":
        undo_func(selected_folder)


# Extensions supported
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".tiff", ".tif", ".svg", ".ico",
        ".heic", ".heif", ".raw", ".cr2", ".nef",
        ".arw", ".dng"
    ],

    "Audio": [
        ".mp3", ".wav", ".ogg", ".flac",
        ".aac", ".m4a", ".wma", ".alac",
        ".aiff", ".ape", ".opus", ".mid",
        ".midi"
    ],

    "Video": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm", ".mpeg",
        ".mpg", ".m4v", ".3gp", ".ts"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".odt",
        ".rtf", ".txt", ".tex", ".pages"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".ods", ".csv"
    ],

    "Presentations": [
        ".ppt", ".pptx", ".odp", ".key"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2", ".xz", ".iso"
    ],

    "Code": [
        ".py", ".java", ".c", ".cpp",
        ".cs", ".js", ".ts", ".html",
        ".css", ".php", ".rb", ".go",
        ".rs", ".swift", ".kt", ".sh",
        ".sql", ".json", ".xml", ".yaml",
        ".yml"
    ],

    "Executables": [
        ".exe", ".msi", ".bat", ".cmd",
        ".apk", ".app", ".deb", ".rpm"
    ],

    "Fonts": [
        ".ttf", ".otf", ".woff",
        ".woff2", ".eot"
    ],

    "Ebooks": [
        ".epub", ".mobi", ".azw",
        ".azw3", ".fb2"
    ]
}

# LOGS
organizer_logs = {}
# CREATED FOLDERS
created_folders = []


# Helper functions
def main_logic(selected_folder):
    for item in selected_folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower()
            folder_type = extension_dir.get(extension, "Other")

            # create folder
            new_folder = selected_folder / folder_type
            if not new_folder.exists():
                created_folders.append(new_folder)
                new_folder.mkdir(parents=True, exist_ok=True)

            # move file into folder
            old_path = selected_folder / item.name
            new_path = new_folder / item.name

            move_file(item, old_path, new_path, new_folder)


def extension_map():
    extension_dictionary = {}
    for key, value in FILE_TYPES.items():
        for val in value:
            extension_dictionary[val] = key
    return extension_dictionary


def move_file(item, old_path, new_path, new_folder, move_type="move"):
    # check if there is already a file with the same name inside the folder and if so change current file name
    count = 1
    while new_path.exists():
        new_name = item.stem + f" ({count})" + item.suffix
        new_path = new_folder / new_name
        print(new_path)
        count += 1

    # move file
    old_path.rename(new_path)
    # save the move info
    if move_type == "move":
        organizer_logs[str(old_path)] = str(new_path)


def undo_func(parent_folder):
    for old_path, new_path in organizer_logs.items():
        old_path = Path(old_path)
        new_path = Path(new_path)

        # move files
        move_file(item=new_path, old_path=new_path, new_path=old_path, new_folder=parent_folder, move_type="undo")

    # delete folders
    for folder in created_folders:
        folder = Path(folder)
        if folder.is_dir() and folder.exists():
            if not any(folder.iterdir()):
                folder.rmdir()

    created_folders.clear()
    organizer_logs.clear()


# Get extension directory
extension_dir = extension_map()

if __name__ == "__main__":
    main()
