import genanki
import csv
from pypinyin import lazy_pinyin
from googletrans import Translator
import random
import csv
import os

# Function to generate Pinyin with error handling
def generate_pinyin(text):
    try:
        return ' '.join(lazy_pinyin(text))
    except Exception as e:
        print(f"Error generating pinyin for '{text}': {e}")
        return None

# Function to translate Chinese to English with error handling
def translate_to_english(text):
    translator = Translator()
    try:
        translation = translator.translate(text, src='zh-cn', dest='en')
        return translation.text
    except Exception as e:
        print(f"Error translating '{text}' to English: {e}")
        return None

# Function to create flashcards from a list of words and sentences
def create_anki_flashcards(word_sentence_list, output_file='mandarin_flashcards.apkg'):
    # Create a new Anki model for Mandarin flashcards
    my_model = genanki.Model(
        1607392319,
        'Simple Model with Pinyin',
        fields=[
            {'name': 'Mandarin'},
            {'name': 'Pinyin'},
            {'name': 'English'},
            {'name': 'Sentence'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Mandarin}}<br>{{Pinyin}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{English}}<br>{{Sentence}}',
            },
        ])

    # Create a new Anki deck
    my_deck = genanki.Deck(
        2059400110,
        'Mandarin Flashcards')

    # Loop over the words and sentences
    for word, sentence in word_sentence_list:
        word_pinyin = generate_pinyin(word)
        sentence_pinyin = generate_pinyin(sentence)
        word_english = translate_to_english(word)

        # Handle errors in any field (skip the card if data is incomplete)
        if word_pinyin is None or word_english is None:
            print(f"Skipping card for '{word}' due to missing data.")
            continue

        # Create a new flashcard
        my_note = genanki.Note(
            model=my_model,
            fields=[word, word_pinyin, word_english, sentence])

        # Add the note to the deck
        my_deck.add_note(my_note)

    # Save the deck to a .apkg file
    genanki.Package(my_deck).write_to_file(output_file)
    print(f"Anki deck '{output_file}' created successfully!")


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


# Main function to read words and generate flashcards
def main():
    input_csv = 'mandarin_words.csv'
    output_file = 'mandarin_flashcards.apkg'

    # Read the CSV file to get the list of words and sentences
    word_sentence_list = read_words_from_csv(input_csv)

    if word_sentence_list:
        # Create Anki flashcards
        create_anki_flashcards(word_sentence_list, output_file)
    else:
        print("No valid words or sentences to process.")

if __name__ == "__main__":
    main()
