import os
from pypinyin import lazy_pinyin, Style
from googletrans import Translator
from cedict_utils.cedict import CedictParser
from dataclasses import dataclass
import json
import glob
from charset_normalizer import detect
import logging

# Function to generate Pinyin with error handling
def generate_pinyin(text):
    try:
        # Use Style.TONE for tone marks
        return ' '.join(lazy_pinyin(text, style=Style.TONE))
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
    
# Define the Word dataclass
@dataclass
class Word:
    simplified: str
    traditional: str
    pinyin: str
    meanings: str

    # Define a custom string representation for the Word class
    def __str__(self):
        return (f"Word: {self.simplified} (Traditional: {self.traditional})\n"
                f"Pinyin: {self.pinyin}\n"
                f"Meanings: {self.meanings}")  

# Function to lookup definitions from the CEDICT dictionary
def load_cedict_simplified_dict(cedict_file_path):
    # Load the CEDICT dictionary once for reuse
    parser = CedictParser()
    cedict_file_path = os.path.join(os.getcwd(), 'Dictionary', 'cedict_ts.u8')
    parser.read_file(cedict_file_path)
    entries = parser.parse()

    # Create a dictionary where simplified characters are keys
    cedict_dict = {}

    # Iterate over the parsed entries
    for entry in entries:
        # Create a Word dataclass instance for each entry
        word_entry = Word(
            simplified=entry.simplified,  # Simplified Chinese characters
            traditional=entry.traditional,  # Traditional Chinese characters
            pinyin=entry.pinyin,  # Pinyin with tone marks
            meanings=entry.meanings  # English definition(s)
        )
        
        # Store the Word object in the dictionary with the simplified character as the key
        cedict_dict[entry.simplified] = word_entry
    
    return cedict_dict

# Function to look up a word in the simplified dictionary
def lookup_simplified_word(word, dictionary):
    return dictionary.get(word, f"No definition found for {word}")

# Function to convert Xiandai dictionary folder into dictionary for easy lookups. 
def load_and_combine_json_files(folder_path):
    combined_dictionary = {}

    # Glob to match all JSON files in the folder
    json_files = glob.glob(f"{folder_path}/*.json")

    for file_path in json_files:
        # Detect encoding
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            encoding_info = detect(raw_data)
            encoding = encoding_info['encoding']
            logging.info(encoding)
        if "index.json" in file_path:  
            continue # Skip the index.json file
        with open(file_path, 'r', encoding=encoding) as f:
            entries = json.load(f)  # Each file is a list of entries
            for entry in entries:
                word = entry[0].strip()  # The word is the first element in each entry
                definition = entry[5][0] if entry[5] else "未找到定义"  # Extract the definition or use a fallback
                combined_dictionary[word] = definition

    return combined_dictionary