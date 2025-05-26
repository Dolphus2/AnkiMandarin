import os
from pathlib import Path
from anki_mandarin import extract_subtitles, convert_subtitles_to_simplified, batch_add_simplified_subs

if __name__ == "__main__":
    # Get the input and output directories from the user
    input_dir = Path(input("Enter the path to the input directory: "))
    output_dir = Path(input("Enter the path to the output directory: "))
    preferred_lang = "chi"


    # Define subdirectories
    output_dir_video = output_dir / 'video'
    output_dir_subs = output_dir / 'subs'
    output_dir_subs_trad = output_dir_subs / 'traditional'
    output_dir_subs_simp = output_dir_subs / 'simplified'

    # Create all output subdirectories
    for path in [output_dir, output_dir_video, output_dir_subs, output_dir_subs_trad, output_dir_subs_simp]:
        path.mkdir(parents=True, exist_ok=True)

    # Optional manual override
    manual_track_id = None  # Set to an integer to override, e.g. 3
    manual_output_format = None  # Set to 'srt', 'ass', 'ssa', etc.

    # Get all MKV files in the input folder
    mkv_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".mkv")]
    for file in mkv_files:
        extract_subtitles(file, output_dir_subs_trad, preferred_lang, manual_track_id, manual_output_format)
    
    # Convert all subtitle files (assume that it is srt even though the extract_subtitles knows what it is)
    subtitle_files = [os.path.join(output_dir_subs_trad, f) for f in os.listdir(output_dir_subs_trad) if f.endswith(".srt")]
    for file in subtitle_files:
        convert_subtitles_to_simplified(file, os.path.join(output_dir_subs_simp, os.path.basename(file)))
    
    batch_add_simplified_subs(input_dir, output_dir_subs_simp, output_dir_video)
    

    