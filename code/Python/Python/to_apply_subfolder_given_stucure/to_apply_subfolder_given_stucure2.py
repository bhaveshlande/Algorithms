import os
import shutil

# Define the main directory where you want to organize the files.
main_directory = "C:/Users/bbaliram/Dev/practice/Algorithm/code"


# Create a dictionary to map extensions to programming languages.
extension_to_language = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".cs": "C#",
    ".php": "PHP",
    ".js": "JavaScript",
    # Add more extensions and language names as needed.
}

# Traverse the main directory and its subfolders.
for foldername, subfolders, filenames in os.walk(main_directory):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        file_name, file_extension = os.path.splitext(filename)

        # Check if the file extension is in the mapping.
        if file_extension in extension_to_language:
            language = extension_to_language[file_extension]

            # Create a directory structure to match the original path within the language folder.
            language_folder = os.path.join(main_directory, language)
            new_folder_path = os.path.join(
                language_folder, foldername[len(main_directory) + 1 :]
            )

            # Create the subfolder in the language folder if it doesn't exist.
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            # Copy the file to the subfolder within the language folder.
            new_file_path = os.path.join(new_folder_path, filename)
            shutil.copy2(file_path, new_file_path)

            print(
                f"Stored '{filename}' in '{language}/{foldername[len(main_directory) + 1:]}' folder."
            )
