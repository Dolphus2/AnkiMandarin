# AnkiMandarin
Automating the boring stuff for my Mandarin Anki cards. Also contains a module to convert MKV video file subtitles from traditional to simplified characters.

AnkiMandarin automates the creation of Mandarin Anki flashcards from words and example sentences.
This is a simple Python package that takes a data `.csv` file with Chinese words and sentence examples as input, and outputs a nicely formatted Anki deck with pinyin, a dictionary lookup for the main word, and a rough translation using a Google Translate API. Sentence translation and word classes can also optionally be provided in the `.csv` file.

I made this to help review and prepare new words from the reading material in my Chinese classes. A typical use case would involve writing up a word list, then either using your own sentence examples or having an LLM (豆包, ChatGPT) generate them for you. Optionally, you can also use the LLM to generate full sentence translations, as these are likely to be more accurate and idiomatic.

If you are comfortable with Anki, the flashcards can be migrated to a new note type, allowing you to change the style or decide not to show translations or pinyin. A tool like HyperTTS can be used to add Text To Speech audio to the cards, as is done below.

### Input `.csv` file examples

![Input](https://github.com/user-attachments/assets/4dd4370a-03cc-4a35-9b9e-24f875957075)
![Input2](https://github.com/user-attachments/assets/610e5e0e-41cd-4a98-b149-fc438f13d7df)

### Anki Card Template

| ![AnkiDemo1](https://github.com/user-attachments/assets/c5493d20-b556-4247-9943-a94e959e3e21) | ![AnkiDemo2](https://github.com/user-attachments/assets/b75f8436-1b04-4844-aed6-caf1bf666f8f) |
|:---:|:---:|
| **Anki Card Front** | **Anki Card Back** |


# Installation Guide

## Prerequisites

You will need Git to clone the repository and a Python installation to run the program.

If you don't have GIt, download from [git-scm.com](https://git-scm.com/) and follow the installation instructions.
If you don't have Python setup, I recommend downloading Miniconda [miniconda official site](https://docs.conda.io/en/latest/miniconda.html) and following the installation instructions.

## Installation

### 1. Clone the Repository

First clone the AnkiMandarin project from github and enter the AnkiMandarin directory:

```bash
git clone https://github.com/Dolphus2/AnkiMandarin
cd AnkiMandarin
```

### 2. Install the Local Module

After cloning the repository, install the `anki_mandarin` package locally using `pip`:

```bash
pip install -e .
```

## Running the Script

Place your `MyWords.csv` with Chinese words in the data folder. 

To generate Anki flashcards, run the main Python script `local_run.py`:

```bash
python .\anki_mandarin\local_run.py
```

This will prompt you to "Enter the name of the `.csv` file (e.g., Chap4.csv):". Simply write the name of the `MyWords.csv` file, and the MyWords.apkg Anki deck should appear in the Output folder. 

Import into Anki and profit!
