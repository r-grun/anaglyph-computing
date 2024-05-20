import cv2 as cv
import os
from tqdm import tqdm

SOURCE_DIR = 'E:\\Programming\\HAW\\Grundprojekt\\anaglyph-computing\\data\\holopix50k'
TARGET_DIR = 'E:\\Programming\\HAW\\Grundprojekt\\anaglyph-computing\\data\\holopix50k\\anaglyphs'


def split_image(image):
    # Get the image shape
    height, width, _ = image.shape

    # Calculate the middle of the image
    middle = width // 2

    # Split the image into left and right halves
    left_img = image[:, :middle]
    right_img = image[:, middle:]

    return left_img, right_img


def merge_channels(img_left, img_right):
    # Split the images into B,G,R channels
    B_left, G_left, R_left = cv.split(img_left)
    B_right, G_right, R_right = cv.split(img_right)

    # Create a new image with the red channel from 'img_left' and the blue + green channel from 'img_right'
    merged_img = cv.merge((B_right, G_right, R_left))

    return merged_img


def process_image(img_input):
    img_left, img_right = split_image(img_input)
    img_anaglyph = merge_channels(img_left, img_right)
    return img_anaglyph


def process_all_images(source_path, target_path, pbar):
    files = os.listdir(source_path)

    # Filter the list to include only .jpg files
    images = [file for file in files if file.endswith('.jpg')]

    # Apply to all images
    for image in images:
        # Construct the full image path
        image_path = os.path.join(source_path, image)

        # Load the image
        img = cv.imread(image_path)

        # Process the image
        processed_img = process_image(img)

        # Save the processed image
        base_name, ext = os.path.splitext(image)
        processed_image_path = os.path.join(target_path, base_name + '_anaglyph' + ext)
        cv.imwrite(processed_image_path, processed_img)

        # Update the progress bar
        pbar.update()


if __name__ == '__main__':
    total_files = sum([len(files) for r, d, files in os.walk(SOURCE_DIR) if any(f.endswith('.jpg') for f in files)])

    with tqdm(total=total_files, desc="Copying images", unit="file") as pbar:
        process_all_images(SOURCE_DIR, TARGET_DIR, pbar)
