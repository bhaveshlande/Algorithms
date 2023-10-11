import os
from collections import defaultdict


def find_and_delete_duplicate_folders(root_dir):
    folder_dict = defaultdict(list)

    for foldername, _, _ in os.walk(root_dir):
        # Extract the folder name without the full path
        folder_name = os.path.basename(foldername)
        # Store the folder's path in the dictionary under its name
        folder_dict[folder_name].append(foldername)

    for folder_name, folder_paths in folder_dict.items():
        # If there is more than one folder with the same name, delete all but one
        if len(folder_paths) > 1:
            print(f"Duplicate folders found for '{folder_name}':")
            for folder_path in folder_paths[1:]:
                print(f"Deleting folder: {folder_path}")
                try:
                    os.rmdir(folder_path)
                except Exception as e:
                    print(f"Error deleting folder: {e}")


if __name__ == "__main__":
    root_directory = r"C:\Users\bbaliram\Dev\practice\Algorithm\code"
    find_and_delete_duplicate_folders(root_directory)
