import os
from collections import defaultdict
from tqdm import tqdm

TARGET_DIRECTORY = 'E:/Programming/HAW/Grundprojekt/anaglyph-computing/data/data/anaglyph'
OUTPUT_FILE = 'images_with_less_than_7_copies.txt'

def get_image_prefix(filename):
    base_name = filename.split('.')[0]
    prefix = base_name.split('_')[0]
    return prefix

def count_image_copies(directory):
    prefix_count = defaultdict(int)
    files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    with tqdm(total=len(files), desc="Scanning images", unit="file") as pbar:
        for filename in files:
            prefix = get_image_prefix(filename)
            prefix_count[prefix] += 1
            pbar.update(1)
    return prefix_count, files

def write_images_with_less_than_7_copies(prefix_count, files, output_file):
    with open(output_file, 'w') as file:
        for filename in files:
            prefix = get_image_prefix(filename)
            if prefix_count[prefix] < 7:
                file.write(f"{filename}\n")

if __name__ == "__main__":
    prefix_count, files = count_image_copies(TARGET_DIRECTORY)
    write_images_with_less_than_7_copies(prefix_count, files, OUTPUT_FILE)
    print(f"Images with less than 7 copies have been written to {OUTPUT_FILE}")

    # Print the number of copies for each prefix with less than 7 copies
    for prefix, count in prefix_count.items():
        if count < 7:
            print(f"Prefix: {prefix}, Copies: {count}")