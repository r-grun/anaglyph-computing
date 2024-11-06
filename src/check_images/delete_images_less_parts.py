import os
from tqdm import tqdm

TARGET_DIRECTORY = 'E:/Programming/HAW/Grundprojekt/anaglyph-computing/data/data/anaglyph'
INPUT_FILE = 'images_with_less_than_7_copies.txt'

def delete_images_from_file(directory, input_file):
    with open(input_file, 'r') as file:
        images_to_delete = file.readlines()

    with tqdm(total=len(images_to_delete), desc="Deleting images", unit="file") as pbar:
        for image in images_to_delete:
            image = image.strip()
            image_path = os.path.join(directory, image)
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Deleted: {image_path}")
            else:
                print(f"File not found: {image_path}")
            pbar.update(1)

if __name__ == "__main__":
    delete_images_from_file(TARGET_DIRECTORY, INPUT_FILE)