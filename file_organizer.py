import os
import shutil

# Change this path to the folder you want to organize
SOURCE_FOLDER = os.getcwd()

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Others": []
}

for file in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, file)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                target_folder = os.path.join(SOURCE_FOLDER, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file))
                moved = True
                break

        if not moved:
            target_folder = os.path.join(SOURCE_FOLDER, "Others")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))

print("Files organized successfully!")
