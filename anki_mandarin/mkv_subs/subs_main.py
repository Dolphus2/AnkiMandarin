import os
from anki_mandarin import extract_subtitles, convert_subtitles_to_simplified

if __name__ == "__main__":
    # Get the input and output directories from the user
    input_dir = input("Enter the path to the input directory: ")
    output_dir = input("Enter the path to the output directory: ")
    preferred_lang = "chi"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Optional manual override
    manual_track_id = None  # Set to an integer to override, e.g. 3
    manual_output_format = None  # Set to 'srt', 'ass', 'ssa', etc.

    # Get all MKV files in the input folder
    mkv_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".mkv")]
    for file in mkv_files:
        extract_subtitles(file, output_dir, preferred_lang, manual_track_id, manual_output_format)
    
    # Convert all subtitle files (assume that it is srt even though the extract_subtitles knows what it is)
    subtitle_files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".srt")]
    for file in subtitle_files:
        convert_subtitles_to_simplified(file, os.path.join(output_dir, "simp_" + os.path.basename(file)))
    