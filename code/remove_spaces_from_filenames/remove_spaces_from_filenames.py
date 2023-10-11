import os


def remove_spaces_from_filenames(root_dir):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if " " in filename:
                new_filename = filename.replace(
                    " ", "_"
                )  # Replace spaces with underscores (you can change this to your preference)
                src = os.path.join(foldername, filename)
                dst = os.path.join(foldername, new_filename)
                os.rename(src, dst)
                print(f"Renamed: {src} -> {dst}")


if __name__ == "__main__":
    root_directory = input("Enter the root directory path: ")
    if os.path.exists(root_directory):
        remove_spaces_from_filenames(root_directory)
        print("Spaces removed from filenames in all subfolders.")
    else:
        print("The specified directory does not exist.")
