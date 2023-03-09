import os

folder_path = "folder path" # Replace with your folder path

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Sort the list of files alphabetically
files.sort()

# Initialize a counter variable
count = 1

# Loop through the files and rename them with a numbered prefix
for file in files:
    # Generate the new file name with the numbered prefix
    new_name = f"{count:01d}.{file}"
    
    # Create the full path to the file
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)
    
    # Increment the counter variable
    count += 1
