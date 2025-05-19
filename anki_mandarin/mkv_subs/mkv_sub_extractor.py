import os
from pathlib import Path
import subprocess
import json

# Note: The mkvtoolnix package is required for this code to work. It can be installed using your system's package manager.

# --- Helper: Load track info ---
def load_mkv_track_info(mkv_file):
    result = subprocess.run(
        ["mkvmerge", "-J", mkv_file],
        capture_output=True,
        text=True,
        check=True
    )
    return json.loads(result.stdout)


# --- Helper: Select subtitle track automatically ---
def select_subtitle_track(info, preferred_lang="eng"):
    subtitle_tracks = [t for t in info["tracks"] if t["type"] == "subtitles"]

    for track in subtitle_tracks:
        if track.get("properties", {}).get("language") == preferred_lang:
            return track

    return subtitle_tracks[0] if subtitle_tracks else None

def extract_subtitles(mkv_file, output_dir, preferred_lang = "chi", manual_track_id = None, manual_output_format = None):
    info = load_mkv_track_info(mkv_file)

    if manual_track_id is not None:
        # Manual override: use specified track ID
        selected_track = next(
            (t for t in info["tracks"] if t["id"] == manual_track_id and t["type"] == "subtitles"), None
        )
        if not selected_track:
            raise Exception(f"Track ID {manual_track_id} not found or not a subtitle track.")
        output_ext = manual_output_format or "srt"
    else:
        # Auto-select subtitle track by language
        selected_track = select_subtitle_track(info, preferred_lang)
        if not selected_track:
            raise Exception("No subtitle track found.")
        codec = selected_track["codec"]
        ext_map = {
            "S_TEXT/UTF8": "srt",
            "S_TEXT/ASS": "ass",
            "S_TEXT/SSA": "ssa"
        }
        output_ext = ext_map.get(codec, "srt")

    track_id = selected_track["id"]
    track_codec = selected_track["codec"]
    print(f"Selected track ID: {track_id} ({track_codec})")

    # --- Construct output path ---
    base_name = os.path.splitext(os.path.basename(mkv_file))[0]
    output_file = os.path.join(output_dir, f"{base_name}_track{track_id}.{output_ext}")

    # --- Run mkvextract ---
    subprocess.run(
        ["mkvextract", mkv_file, "tracks", f"{track_id}:{output_file}"],
        check=True
    )

    print(f"Extracted subtitle track {track_id} to {output_file}")


if __name__ == "__main__":
    # --- Configuration ---
    input_dir = Path(r"C:\Users\Gabriel\MyFiles\Lokale Filer\Kina\MyChinese\Anki\AnkiMandarin\data\TraditionalSubtitles\Test1")
    output_dir = Path(r"C:\Users\Gabriel\MyFiles\Lokale Filer\Kina\MyChinese\Anki\AnkiMandarin\data\TraditionalSubtitles\Test2")
    preferred_lang = "chi"

    # Optional manual override
    manual_track_id = None  # Set to an integer to override, e.g. 3
    manual_output_format = None  # Set to 'srt', 'ass', 'ssa', etc.

    # Get all MKV files in the input folder
    mkv_files = [input_dir / f for f in os.listdir(input_dir) if f.endswith(".mkv")]
    for file in mkv_files:
        extract_subtitles(file, output_dir, preferred_lang, manual_track_id, manual_output_format)
