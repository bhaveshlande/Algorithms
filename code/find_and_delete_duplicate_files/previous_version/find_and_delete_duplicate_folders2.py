import os


def find_and_delete_duplicate_folders(root_dir):
    for dirpath, dirnames, _ in os.walk(root_dir, topdown=False):
        for subdir in dirnames:
            subdir_path = os.path.join(dirpath, subdir)
            if not any(subdir in d for d in dirnames):
                try:
                    # Attempt to remove the folder even if it's non-empty
                    for root, dirs, files in os.walk(subdir_path, topdown=False):
                        for file in files:
                            file_path = os.path.join(root, file)
                            os.remove(file_path)
                        for folder in dirs:
                            folder_path = os.path.join(root, folder)
                            os.rmdir(folder_path)
                    os.rmdir(subdir_path)
                    print(f"Deleted folder: {subdir_path}")
                except FileNotFoundError as e:
                    print(f"FileNotFoundError: {e}")
                except PermissionError as e:
                    print(f"PermissionError: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")


if __name__ == "__main":
    root_directory = r"C:\Users\bbaliram\Dev\practice\Algorithm\code"
    find_and_delete_duplicate_folders(root_directory)
