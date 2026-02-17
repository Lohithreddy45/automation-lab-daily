import os
import shutil
import argparse
from datetime import datetime

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Others": []
}

def log(message):
    with open("organizer.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")


def organize(folder):
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            moved = False

            for category, extensions in FILE_TYPES.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    target = os.path.join(folder, category)
                    os.makedirs(target, exist_ok=True)
                    shutil.move(file_path, os.path.join(target, file))
                    log(f"Moved {file} -> {category}")
                    moved = True
                    break

            if not moved:
                target = os.path.join(folder, "Others")
                os.makedirs(target, exist_ok=True)
                shutil.move(file_path, os.path.join(target, file))
                log(f"Moved {file} → Others")

    print("Organization complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Organizer Tool")
    parser.add_argument("path", help="Folder path to organize")

    args = parser.parse_args()
    organize(args.path)
