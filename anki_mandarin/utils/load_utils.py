import csv
import os

# Function to read data from CSV and return a list of word-sentence pairs
def read_words_from_csv(file_path):
    word_sentence_list = []
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return word_sentence_list

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                word_sentence_list.append((row['word'], row['sentence']))
    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return word_sentence_list