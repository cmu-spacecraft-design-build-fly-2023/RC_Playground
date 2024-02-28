import os
from PIL import Image

def convert_jpg_to_png(root_dir):
    # Walk through the directory
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            # Check if the file is a JPG image
            if file.endswith('.jpg') or file.endswith('.JPG'):
                # Construct full file path
                file_path = os.path.join(subdir, file)
                # Open the image
                with Image.open(file_path) as img:
                    # Define the new filename with .png extension
                    filename_wo_extension = os.path.splitext(file)[0]
                    new_file_path = os.path.join(subdir, filename_wo_extension + '.png')
                    # Save the image in PNG format
                    img.save(new_file_path, 'PNG')
                    print(f'Converted {file_path} to {new_file_path}')

# Replace 'datasets' with your actual root directory path
root_dir = '/home/argus-vision/vision/RC_Playground/RCnet/datasets/test'
convert_jpg_to_png(root_dir)
