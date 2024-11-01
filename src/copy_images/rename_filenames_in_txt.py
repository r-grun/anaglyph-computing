from tqdm import tqdm

txt_path = '../../data/xx.txt'
new_txt_path = '../../data/xx_indexed.txt'

# Open the file and read lines
with open(txt_path, 'r') as file:
    lines = file.readlines()

# Write new lines directly to the new file with tqdm progress bar
with open(new_txt_path, 'w') as new_file:
    for line in tqdm(lines, desc="Processing"):
        line = line.strip()  # Remove any extra spaces
        for i in range(8):
            new_line = f"{line.split('.')[0]}_{i}.jpg"
            new_file.write(new_line + '\n')


print(f"Processing complete. Check {new_txt_path} for results.")