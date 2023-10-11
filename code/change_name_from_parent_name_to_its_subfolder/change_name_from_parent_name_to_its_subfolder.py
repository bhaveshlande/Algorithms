import os

# Define the main directory where you want to organize the files.
main_directory = "path/to/your/main/directory"

# Create a dictionary to map programming languages to their corresponding extensions.
language_to_extension = {
    "Python": ".py",
    "Java": ".java",
    "C++": ".cpp",
    "C#": ".cs",
    "PHP": ".php",
    "JavaScript": ".js",
    # Add more languages and extensions as needed.
}

# Traverse the main directory and its subfolders.
for foldername, subfolders, filenames in os.walk(main_directory):
    for language, extension in language_to_extension.items():
        language_folder = os.path.join(foldername, language)

        # Check if the language folder exists within the current directory.
        if os.path.exists(language_folder):
            # Rename the language folder to match the folder you're traversing.
            new_language_folder = os.path.join(
                foldername, f"{os.path.basename(foldername)}{extension}"
            )

            if not os.path.exists(new_language_folder):
                os.rename(language_folder, new_language_folder)
                print(f"Renamed '{language_folder}' to '{new_language_folder}'")

            # Create an empty file with the specified extension.
            new_file_path = os.path.join(
                new_language_folder, f"{os.path.basename(foldername)}{extension}"
            )
            with open(new_file_path, "w") as file:
                pass

print("Folders and files organized successfully.")
