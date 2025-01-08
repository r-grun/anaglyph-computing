import csv

def filter_csv(input_csv, output_txt, target_label):
    """
    Filters rows from a CSV file based on a target label and writes the 'Path' column values to a text file.

    :param input_csv: Path to the input CSV file.
    :param output_txt: Path to the output text file.
    :param target_label: The label to filter rows by.
    """
    try:
        with open(input_csv, mode='r', newline='', encoding='utf-8') as csv_file, open(output_txt, mode='w', encoding='utf-8') as txt_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                if row['Label'] == target_label:
                    txt_file.write(row['Path'] + '\n')

        print(f"Filtered rows with label '{target_label}' written to {output_txt}")
    except FileNotFoundError:
        print(f"Error: The file {input_csv} was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Paths and target labels
input_csv = '/workspace/data/train.csv'
anaglyph_output = '/workspace/data/train_anaglyphs.txt'
reversed_output = '/workspace/data/train_reversed.txt'

# Filter rows and create the output files
filter_csv(input_csv, anaglyph_output, 'anaglyph')
filter_csv(input_csv, reversed_output, 'anaglyph_reversed')
