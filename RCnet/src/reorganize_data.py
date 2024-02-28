import os
import shutil

def reorganize_datasets(root_dir):
    # Paths for the new main directories
    main_dirs = ['test']

    # Ensure the new main directories exist
    for dir_name in main_dirs:
        new_dir_path = os.path.join(root_dir, dir_name)
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)

    # Iterate through each folder in the root directory
    for folder_name in os.listdir(root_dir):
        current_folder_path = os.path.join(root_dir, folder_name)
        
        # Skip if not a directory or if it's one of the new main directories
        if not os.path.isdir(current_folder_path) or folder_name in main_dirs:
            continue

        # Iterate through the subdirectories (test, train, val) of each dataset
        for sub_dir_name in main_dirs:
            sub_dir_path = os.path.join(current_folder_path, sub_dir_name)
            
            # Continue if the subdirectory does not exist
            if not os.path.exists(sub_dir_path):
                continue

            # Destination path for the current subdirectory
            dest_dir_path = os.path.join(root_dir, sub_dir_name, folder_name)
            
            # Move the subdirectory to the new location
            shutil.move(sub_dir_path, dest_dir_path)

        # Optionally remove the now-empty dataset folder
        # os.rmdir(current_folder_path)

# Example usage
root_dir = '/home/argus-vision/vision/RC_Playground/RCnet/datasets'
reorganize_datasets(root_dir)
