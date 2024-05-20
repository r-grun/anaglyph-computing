import cv2 as cv
import os
from tqdm import tqdm
import numpy as np

SOURCE_DIR_LEFT = 'E:\\Programming\\HAW\\Grundprojekt\\anaglyph-computing\\data\\holopix50k\\left'
SOURCE_DIR_RIGHT = 'E:\\Programming\\HAW\\Grundprojekt\\anaglyph-computing\\data\\holopix50k\\right'
TARGET_DIR = 'E:\\Programming\\HAW\\Grundprojekt\\anaglyph-computing\\data\\holopix50k'


def process_all_images(left_folder, right_folder, output_folder, pbar):
    # Get the list of image files in the left and right folders
    left_images = os.listdir(left_folder)
    right_images = os.listdir(right_folder)

    for image in left_images:
        # Check if the corresponding image exists in the right folder
        right_image = image.replace('_left', '_right')
        if right_image in right_images:
            # Construct the full path to the left and right images
            left_image_path = os.path.join(left_folder, image)
            right_image_path = os.path.join(right_folder, right_image)

            # Read the images
            img1 = cv.imread(left_image_path)
            img2 = cv.imread(right_image_path)

            # Check if the images were loaded successfully
            if img1 is None:
                print(f"Image at {left_image_path} not found")
                continue
            if img2 is None:
                print(f"Image at {right_image_path} not found")
                continue

            # Concatenate the images along the x-axis
            img_concatenated = np.concatenate((img1, img2), axis=1)

            # Remove the '_left' suffix from the image filename
            output_name = image.replace('_left', '')

            # Create the output path
            output_path = os.path.join(output_folder, output_name)

            # Save the concatenated image
            cv.imwrite(output_path, img_concatenated)

            # increment progress bar
            pbar.update()


if __name__ == '__main__':
    total_files = sum(
        [len(files) for r, d, files in os.walk(SOURCE_DIR_LEFT) if any(f.endswith('.jpg') for f in files)])

    with tqdm(total=total_files, desc="Copying images", unit="file") as pbar:
        process_all_images(SOURCE_DIR_LEFT, SOURCE_DIR_RIGHT, TARGET_DIR, pbar)
