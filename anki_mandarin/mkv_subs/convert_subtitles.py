from pathlib import Path
import opencc

def convert_subtitles_to_simplified(input_file: Path, output_file: Path):
    """
    Convert a subtitle file from Traditional to Simplified Chinese using OpenCC.
    
    Parameters:
        input_file (str or Path): Path to the input subtitle file.
        output_file (str or Path): Path to save the converted subtitle file.
    """
    converter = opencc.OpenCC('tw2s.json')

    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    # Read, convert, and write
    with input_path.open("r", encoding="utf-8") as fin:
        content = fin.read()
    
    converted = converter.convert(content)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fout:
        fout.write(converted)

    print(f"Converted {input_path.name} → {output_path.name} (Traditional → Simplified)")

if __name__ == "__main__":
    input_file=Path(r"C:\Users\Gabriel\MyFiles\Lokale Filer\Kina\MyChinese\Anki\AnkiMandarin\data\TraditionalSubtitles\Test2\21_track5.srt")
    output_file=Path(r"C:\Users\Gabriel\MyFiles\Lokale Filer\Kina\MyChinese\Anki\AnkiMandarin\data\TraditionalSubtitles\Test2\21_track5simp.srt")

    convert_subtitles_to_simplified(input_file, output_file)