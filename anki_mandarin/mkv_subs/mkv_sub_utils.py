import os
from pathlib import Path
import subprocess
import json

# Note: The mkvtoolnix package is required for this code to work. It can be installed using your system's package manager.

# --- Helper: Load track info ---
def load_mkv_track_info(mkv_file: Path):
    result = subprocess.run(
        ["mkvmerge", "-J", mkv_file],
        capture_output=True,
        text=True,
        encoding="utf-8",  # <-- force UTF-8!
        check=True
    )
    return json.loads(result.stdout)

def get_existing_subtitle_tracks(mkv_file: Path) -> list:
    """Return a list of subtitle track IDs in the MKV file using mkvmerge JSON output."""
    info = load_mkv_track_info(mkv_file)
    return [t for t in info.get("tracks", []) if t.get("type") == "subtitles"]


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

def add_simplified_sub_to_mkv(
    input_mkv: Path,
    subtitle_file: Path,
    output_mkv: Path,
    language: str = "chi",
    track_name: str = "Chinese (Simplified)"
):
    if not input_mkv.exists() or not subtitle_file.exists():
        print(f"Missing: {input_mkv} or {subtitle_file}")
        return

    # Build command: copy all existing tracks from mkv + add new subtitle
    command = [
        "mkvmerge", "-o", str(output_mkv),
        str(input_mkv),
        "--language", "0:" + language,
        "--track-name", f"0:{track_name}",
        str(subtitle_file)
    ]

    subprocess.run(command, check=True)
    print(f"Added simplified subs to: {output_mkv.name}")

def batch_add_simplified_subs(mkv_dir: Path, srt_dir: Path, output_dir: Path):
    mkv_dir = Path(mkv_dir)
    srt_dir = Path(srt_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for mkv_file in mkv_dir.glob("*.mkv"):
        # Find any .srt file in srt_dir that starts with the mkv_file's stem
        matching_srts = list(srt_dir.glob(f"{mkv_file.stem}*.srt"))

        if not matching_srts:
            print(f"No .srt file found for {mkv_file.name}")
            continue

        # Use the first matching subtitle
        srt_file = matching_srts[0]
        output_file = output_dir / mkv_file.name

        add_simplified_sub_to_mkv(
            input_mkv=mkv_file,
            subtitle_file=srt_file,
            output_mkv=output_file
        )

if __name__ == "__main__":
    
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
