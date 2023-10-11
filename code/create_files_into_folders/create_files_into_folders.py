import os

# Define the main directory where you want to organize the files.
main_directory = "C:/Users/bbaliram/Dev/practice/Algorithm/code"


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
            # Create a subfolder within the language folder based on the language's extension.
            language_extension_folder = os.path.join(
                language_folder, "programming" + extension
            )

            # Create the extension folder if it doesn't exist.
            if not os.path.exists(language_extension_folder):
                os.makedirs(language_extension_folder)

            # Create an empty file with the specified extension.
            new_file_path = os.path.join(
                language_extension_folder, f"empty_file{extension}"
            )
            with open(new_file_path, "w") as file:
                pass

print("Empty files created successfully.")
