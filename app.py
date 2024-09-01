import os
import shutil

# Define the target directory
directory = os.path.join(os.path.expanduser("~"), "C:\\Users\\Hp")

# Create a dictionary mapping file extensions to their corresponding folder names
extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".pptx": "MSPowerPoints",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".docx": "Documents",
    ".apk": "Applications",
    ".csv": "DataSheets",
    ".xlsx": "MSDocs",
    ".exe": "Executibles",
    ".zip": "Zips",
    ".pdf": "Documents",
    ".srt": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".wav": "Music"
}

# Iterate through each file in the target directory
for filename in os.listdir(directory):
    # Get the full path of the file
    file_path = os.path.join(directory, filename)

    # Check if the item is a file (not a directory)
    if os.path.isfile(file_path):
        # Get the file extension in lowercase
        extension = os.path.splitext(filename)[1].lower()

        # Check if the extension is supported
        if extension in extensions:
            # Get the corresponding folder name
            folder_name = extensions[extension]

            # Create the folder if it doesn't exist
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # Move the file to the appropriate folder
            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            # Print a success message
            print(f"Moved {filename} to {folder_name} folder.")
        else:
            # Print a message for unsupported file extensions
            print(f"Skipped {filename}. Unknown File Extension.")
    else:
        # Print a message for directories
        print(f"Skipped {filename}. It is a Directory.")

# Print a completion message
print("File Organization Completed.")
