import os
import shutil

# Define the main directory where you want to organize the files.
main_directory = "C:/Users/bbaliram/Dev/practice/Algorithm/code"

# Create a dictionary to map extensions to folder names.
extension_to_folder = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".cs": "C#",
    ".php": "PHP",
    ".js": "JavaScript",
    # Add more extensions and folder names as needed.
}

# Get a list of all files in the main directory and its subfolders.
for foldername, subfolders, filenames in os.walk(main_directory):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        file_name, file_extension = os.path.splitext(filename)

        # Check if the file extension is in the mapping.
        if file_extension in extension_to_folder:
            language_folder = extension_to_folder[file_extension]
            language_directory = os.path.join(main_directory, language_folder)

            # Create the language-specific folder if it doesn't exist.
            if not os.path.exists(language_directory):
                os.makedirs(language_directory)

            # Create a copy of the file with the same name in the language folder
            new_file_path = os.path.join(language_directory, filename)

            # Check if the file already exists in the destination folder
            if not os.path.exists(new_file_path):
                shutil.copy2(file_path, new_file_path)
                print(f"Stored '{filename}' in '{language_folder}' folder.")
            else:
                print(f"'{filename}' already exists in '{language_folder}' folder.")
