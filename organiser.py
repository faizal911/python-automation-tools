import os
import shutil

# ─────────────────────────────────────────
# FILE ORGANISER — by Faizal Khan
# Automatically sorts files in a folder
# into subfolders by their file type.
# ─────────────────────────────────────────

# Dictionary: file extension → folder name
FILE_TYPES = {
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images',
    '.gif': 'Images', '.bmp': 'Images', '.svg': 'Images',
    # Documents
    '.pdf': 'Documents', '.docx': 'Documents', '.doc': 'Documents',
    '.txt': 'Documents', '.pptx': 'Documents', '.xlsx': 'Documents',
    # Videos
    '.mp4': 'Videos', '.mkv': 'Videos', '.avi': 'Videos', '.mov': 'Videos',
    # Audio
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
    # Code
    '.py': 'Code', '.js': 'Code', '.html': 'Code', '.css': 'Code',
    '.java': 'Code', '.cpp': 'Code', '.c': 'Code',
    # Archives
    '.zip': 'Archives', '.rar': 'Archives', '.tar': 'Archives', '.gz': 'Archives',
}


def organise_folder(folder_path):
    """
    Organises all files in the given folder
    into subfolders based on file type.
    """

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"❌ Error: Folder '{folder_path}' does not exist.")
        return

    files_moved = 0
    files_skipped = 0

    # Loop through every item in the folder
    for filename in os.listdir(folder_path):

        # Build the full path of the file
        file_path = os.path.join(folder_path, filename)

        # Skip folders — only process files
        if os.path.isdir(file_path):
            continue

        # Get the file extension (e.g. '.pdf', '.jpg')
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Find which folder this extension belongs to
        folder_name = FILE_TYPES.get(extension, 'Others')

        # Build the destination folder path
        destination_folder = os.path.join(folder_path, folder_name)

        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file to the destination folder
        destination_path = os.path.join(destination_folder, filename)

        # Handle duplicate filenames
        if os.path.exists(destination_path):
            base, ext = os.path.splitext(filename)
            destination_path = os.path.join(destination_folder, f"{base}_copy{ext}")

        shutil.move(file_path, destination_path)
        print(f"✅ Moved: {filename} → {folder_name}/")
        files_moved += 1

    print(f"\n📁 Done! {files_moved} files organised, {files_skipped} skipped.")


# ─── MAIN PROGRAM ───
if __name__ == "__main__":
    print("=" * 45)
    print("       🗂️  Python File Organiser")
    print("=" * 45)

    folder = input("\nEnter the full path of the folder to organise:\n> ").strip()
    organise_folder(folder)
