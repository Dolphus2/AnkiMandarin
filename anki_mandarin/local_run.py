import os
from anki_mandarin import run_model

import os

def find_csv_in_subdirectories(base_dir, csv_name):
    for root, dirs, files in os.walk(base_dir):
        if csv_name in files:
            return os.path.join(root, csv_name)
    return None

if __name__ == "__main__":
    # Prompt user for CSV file name
    csv_name = input("Enter the name of the .csv file (e.g., Chap4.csv): ")

    # Define base directory and search for the CSV file in the 'data' subdirectories
    base_dir = os.getcwd()
    input_csv = find_csv_in_subdirectories(os.path.join(base_dir, 'data'), csv_name)

    if input_csv:
        print(f"CSV file found: {input_csv}")
        # Define output and dictionary paths
        output_file = os.path.join(base_dir, 'Output', f'PythonMandarin_{csv_name}.apkg')
        cedict_file_path = os.path.join(base_dir, 'Dictionary', 'cedict_ts.u8')

        # Run the main function with parsed arguments
        run_model(input_csv, output_file, cedict_file_path)
    else:
        print(f"CSV file '{csv_name}' not found in the 'data' subdirectories.")