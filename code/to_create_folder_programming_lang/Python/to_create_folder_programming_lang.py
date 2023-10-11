import os

# Define the path where you want to create subfolders.
main_directory = "C:/Users/bbaliram/Dev/practice/Algorithm/code"

# Define a list of programming languages for which you want to create folders.
programming_languages = [
    "Python",
    "Java",
    "C++",
    "C#",
    "PHP",
    "JavaScript",
    # Add more languages as needed.
]

# Traverse the main directory and its subfolders.
for foldername, subfolders, filenames in os.walk(main_directory):
    for language in programming_languages:
        # Create a subfolder with the language name in each folder.
        language_folder = os.path.join(foldername, language)
        if not os.path.exists(language_folder):
            os.makedirs(language_folder)
            print(
                f"Created '{language}' folder in '{foldername[len(main_directory) + 1:]}'"
            )

print("Folders created successfully.")
