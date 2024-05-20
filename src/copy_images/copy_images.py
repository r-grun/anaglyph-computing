import os
import shutil
from tqdm import tqdm


def copy_images(src_dir, dest_dir, pbar):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Initialize a counter
    counter = 0

    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Check if the file is a .png
            if file.endswith('.jpg'):
                # Get the subdirectory name
                subdir_name = os.path.basename(root)
                # Create a new name for the file
                new_name = f"{subdir_name}_{counter}.jpg"
                # Create the full file paths
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, new_name)
                # Copy the file
                shutil.copy2(src_file_path, dest_file_path)
                # Increment the counter
                counter += 1
                # Update the progress bar
                pbar.update()


# Define the source and destination directories
src_dir = "E:\\Programming\\HAW\\Grundprojekt\\stereOBJ1M\\images_annotations"
dest_dir = "E:\\Programming\\HAW\\Grundprojekt\\anaglyph-computing\\data"

# Get the total number of .png files in the source directory
total_files = sum([len(files) for r, d, files in os.walk(src_dir) if any(f.endswith('.jpg') for f in files)])

# Copy the images with a progress bar
with tqdm(total=total_files, desc="Copying images", unit="file") as pbar:
    copy_images(src_dir, dest_dir, pbar)
