import sys
from pathlib import Path


def main():
    if len(sys.argv) == 2:
        selected_folder = Path(sys.argv[1])

    else:
        # Should open a GUI here. Added an error message for now
        print("No folder selected")
        return

    if (not selected_folder.is_dir()) or (not selected_folder.exists()):
        print("Folder not found")
        return

    # Get extension directory
    extension_dir = get_dictionary()

    for item in selected_folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower()
            folder_type = extension_dir.get(extension, "Other")

            # create folder
            new_folder = selected_folder / folder_type
            new_folder.mkdir(parents=True, exist_ok=True)

            # move file into folder
            old_path = selected_folder / item.name
            new_path = new_folder / item.name


            # check if there is already a file with the same name inside the folder and if so change current file name
            # TODO
            count=1
            while new_path.exists():
                new_name = item.stem + f" ({count})" + item.suffix
                new_path = new_folder / new_name
                print(new_path)
                count += 1

            old_path.rename(new_path)


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


# Helper functions
def get_dictionary():
    extension_dictionary = {}
    for key, value in FILE_TYPES.items():
        for val in value:
            extension_dictionary[val] = key
    return extension_dictionary


if __name__ == "__main__":
    main()
