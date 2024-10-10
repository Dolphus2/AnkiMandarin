import csv
import os

# Function to read data from CSV and return a list of dictionaries
def read_words_from_csv(file_path):
    word_sentence_list = []
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return word_sentence_list

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Append the whole row as a dictionary for flexibility in terms of columns.
                word_sentence_list.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return word_sentence_list