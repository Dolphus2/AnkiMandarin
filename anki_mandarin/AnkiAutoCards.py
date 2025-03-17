import os
import argparse
from anki_mandarin import load_cedict_simplified_dict, read_words_from_csv, create_anki_flashcards, load_and_combine_json_files

def run_model(input_csv, output_file, cedict_file_path, xiandai_folder_path, moe_folder_path):
    """
    Main function to read words from a CSV file and generate Anki flashcards.

    Args:
        input_csv (str): Path to the CSV file containing words and sentences.
        output_file (str): Path to save the generated Anki flashcards package.
        cedict_file_path (str): Path to the CEDICT dictionary file.
        xiandai_file_path (str): Path to the Xiandai dictionary folder.
    """

    # Load the CEDICT dictionary
    cedict_dict = load_cedict_simplified_dict(cedict_file_path)

    # Load the Xianndai dictionary
    xiandai_dict = load_and_combine_json_files(xiandai_folder_path)

    # Load the MoeDict dictionary
    moe_dict = load_and_combine_json_files(moe_folder_path)

    # Read the CSV file to get the list of words and sentences
    word_sentence_list = read_words_from_csv(input_csv)

    # Check if word_sentence_list has valid entries
    if word_sentence_list:
        # Create Anki flashcards
        create_anki_flashcards(word_sentence_list, cedict_dict=cedict_dict, xiandai_dict=xiandai_dict, moe_dict=moe_dict, init_idx=1, output_file=output_file)
        print(f"Anki flashcards created successfully in {output_file}.")
    else:
        print("No valid words or sentences to process.")

def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate Anki flashcards from Mandarin words and example sentences.")
    
    # Define command-line arguments
    parser.add_argument(
        '--input_csv',
        type=str,
        required=True,
        help="Path to the input CSV file containing Mandarin words and sentences."
    )
    parser.add_argument(
        '--output_file',
        type=str,
        required=True,
        help="Path to the output .apkg file where Anki flashcards will be saved."
    )
    parser.add_argument(
        '--cedict_file',
        type=str,
        required=True,
        help="Path to the CEDICT dictionary file."
    )
    parser.add_argument(
        '--xiandai_folder',
        type=str,
        required=True,
        help="Path to the Xiandai dictionary folder."
    )
    parser.add_argument(
        '--moe_folder',
        type=str,
        required=True,
        help="Path to the MoeDict dictionary folder."
    )


    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Current working directory: {os.getcwd()}")
    
    # Run the main function with parsed arguments
    run_model(args.input_csv, args.output_file, args.cedict_file, args.xiandai_folder, args.moe_folder)