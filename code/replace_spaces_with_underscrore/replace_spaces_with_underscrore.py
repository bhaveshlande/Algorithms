import os


def replace_spaces_with_underscores(root_dir):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if " " in filename:
                new_filename = filename.replace(" ", "_")
                src = os.path.join(foldername, filename)
                dst = os.path.join(foldername, new_filename)
                os.rename(src, dst)
                print(f"Renamed: {src} -> {dst}")


if __name__ == "__main__":
    root_directory = input("Enter the root directory path: ")
    if os.path.exists(root_directory):
        replace_spaces_with_underscores(root_directory)
        print(
            "Spaces replaced with underscores in filenames for all subfolders and files."
        )
    else:
        print("The specified directory does not exist.")
