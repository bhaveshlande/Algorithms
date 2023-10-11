import os
import shutil

# Define the main directory where you want to organize the files.
main_directory = "C:/Users/bbaliram/Dev/practice/Algorithm/code"

# Get a list of all files in the main directory and its subfolders.
for foldername, subfolders, filenames in os.walk(main_directory):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        file_name, file_extension = os.path.splitext(filename)

        # Define a dictionary that maps file extensions to programming languages.
        language_mapping = {
            ".py": "Python",
            ".java": "Java",
            ".cpp": "C++",
            ".cs": "C#",
            ".php": "PHP",
            ".js": "JavaScript",
        }

        # Check if the file extension is in the mapping.
        if file_extension in language_mapping:
            language = language_mapping[file_extension]

            # Create a directory for the programming language if it doesn't exist.
            language_directory = os.path.join(main_directory, language)
            if not os.path.exists(language_directory):
                os.makedirs(language_directory)

            # Move the file to the corresponding language directory.
            new_file_path = os.path.join(language_directory, filename)
            shutil.move(file_path, new_file_path)

            print(f"Moved '{filename}' to '{language}' folder.")
