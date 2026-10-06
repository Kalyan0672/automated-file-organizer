import os
import shutil

SOURCE_FOLDER = "input"
OUTPUT_FOLDER = "output"

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Presentations": [".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"]
}


def organize_files():

    if not os.path.exists(SOURCE_FOLDER):
        print("Input folder does not exist.")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(SOURCE_FOLDER):

        file_path = os.path.join(SOURCE_FOLDER, filename)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        # Default category
        category = "Others"

        # Find the correct category
        for folder, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                category = folder
                break

        # Create category folder
        category_path = os.path.join(OUTPUT_FOLDER, category)

        os.makedirs(category_path, exist_ok=True)

        # Destination path
        destination = os.path.join(category_path, filename)

        # Move the file
        shutil.move(file_path, destination)

        print(f"Successfully moved: {filename} → {category}")


if __name__ == "__main__":
    organize_files()