import genanki



# Create a new Anki model for Mandarin flashcards
# Every unique model should have a unique model ID. Use print(random.randrange(1 << 30, 1 << 31))
# Function to create flashcards from a list of words and sentences

def create_mandarin_model():
    # Create a new Anki model for Mandarin flashcards with custom templates and CSS
    return genanki.Model(
        1411383865,
        'RefoldStyleMandarinPython', # Note type # Advanced Model with All Refold Mandarin 1k Fields and more#
        fields=[
            {'name': 'Key'},
            {'name': 'Simplified'},
            {'name': 'Traditional'},
            {'name': 'Pinyin'},
            {'name': 'TwPronunciation'},
            {'name': 'Meaning'},
            {'name': 'MeaningZH'},
            {'name': 'Part of speech'},
            {'name': 'Audio'},
            {'name': 'SentenceSimplified'},
            {'name': 'SentenceTraditional'},
            {'name': 'SentencePreWord'},
            {'name': 'SentenceWord'},
            {'name': 'SentencePostWord'},
            {'name': 'SentencePinyin'},
            {'name': 'SentenceMeaning'},
            {'name': 'SentenceAudio'},
            {'name': 'SentenceImage'},
            {'name': 'Source'},
            {'name': 'Note'},
            
        ],
        templates=[
            {
                'name': 'WordFirst',
                'qfmt': '''
<div lang="zh-Hans" class="hanzi whover" style="--pinyin: '{{Pinyin}}{{#TwPronunciation}}, Taiwanese Pronunciation: {{TwPronunciation}}{{/TwPronunciation}}'">{{Simplified}}</div>
<div class="pinyin"><br></div>
<div class="english"><br></div>
<div class="description"><br></div>
<hr>
<div lang="zh-Hans" class="sentence" style="--pinyin: {{SentencePinyin}}">{{SentenceSimplified}}</div>
<div class="pinyinSen whover">{{SentencePinyin}}</div>
                ''',
                'afmt': '''
<div lang="zh-Hans" class="hanzi">{{Simplified}}</div>
<div class="pinyin">{{Pinyin}}{{#TwPronunciation}}, Taiwanese Pronunciation: {{TwPronunciation}}{{/TwPronunciation}}</div>
<div class="english">{{Meaning}}</div>
<div class="description">{{Part of speech}}</div>
<hr>
<div lang="zh-Hans" class="sentence">{{SentenceSimplified}}</div>
<div class="pinyinSen">{{SentencePinyin}}</div>
<div class="meaningSent">{{SentenceMeaning}}</div>
{{Audio}} {{SentenceAudio}}
<br>
{{#Source}}Source: {{Source}}{{/Source}}
<br>
{{#Note}}Note: {{Note}}{{/Note}}
<br>
<div class="image">{{SentenceImage}}</div>
                '''
            },
        ],
        css='''
hr {
    height: 3px;
    background: white;
    border: none;
    margin-top: 20px;
    margin-bottom: 20px;
}

div {
    margin-bottom: 10px;
}

.card {
    font-family: Georgia; 
    font-size: 10px; 
    text-align: left; 
    background-color: rgb(47,47,49);
    color: #fff;
    padding: 20px;
    height: 87vh; 
}

.nightMode.card {
    color: white;
    background-color: #121212;
}

.hanzi {
    font-family: Kai;  
    font-size: 78px;
    border-bottom: 3px solid rgba(0,0,0,0);
    transition: border 0.5s ease, padding 0.5s ease;
    margin-top: 20px;
}

.hanzi.whover {
    cursor: pointer;
}

.hanzi.whover::before,
.sentence.whover::before {
    font-family: Palatino;
    content: var(--pinyin);
    position: absolute;
    font-size: 22px;
    color: #1f81b7;
    padding-left: 10px;
    padding-right: 10px;
    padding-bottom: 5px;
    border-left: 3px solid white;
    transform: translate(-10px, -40px);
    opacity: 0;
    transition: opacity 0.5s ease;
    height: 140px;
    padding-top: 0px;
}

.hanzi.whover:hover::before,
.sentence.whover:hover::before {
    opacity: 1;
}
.sentence {
    font-family: Kai; 
    font-size: 30px; 
    text-align: left;
    transition: padding 0.5s ease;
}

.sentenceFront {
    font-size: 40px;
}

.sentenceBack {
    font-size: 35px;
}

.pinyinSen.whover {
    cursor: pointer;
    opacity: 1;
    border-left: 3px solid white;
    padding-left: 10px;
    height: 25px;
    max-height: 80px;
    display: flex;
    padding-top: 55px;
    transform: translate(-10px, -50px);
    opacity: 0;
    transition: opacity 0.5s ease;
    white-space: nowrap;
}

.pinyinSen.whover:hover {
    opacity: 1;
}

.pinyin {
    font-family: Palatino; 
    font-size: 22px; 
    color: #1f81b7;
}

.pinyinSen {
    font-family: Palatino; 
    font-size: 20px; 
    color: #1f81b7; 
    text-align: left;
}

.wordFront {
    color: #a11010;
    font-size: 40px;
}

.nightMode .wordFront {
    color: lightpink;
}

/* Word in the back of the card */
.wordBack {
    font-size: 35px;
    padding-bottom: 20px;
    color: #a11010;
}

.nightMode .wordBack {
    color: lightpink;
}

/* English and Meaning Display */
.english {
    font-family: Didot;
    font-size: 16px;
}

details summary {
  font-family: Didot;
  font-size: 16px;
  cursor: pointer; 
  margin-top: 10px; /* Optional: spacing above */
}

.meaningSent {
    font-family: Didot;
    font-size: 16px;
    text-align: left;
}

.meaning {
    padding-bottom: 20px;
    font-size: 20px;
}

/* Part of Speech (Optional) */
.description {
    font-family: Didot; 
    font-size: 16px; 
    color: #575757;
}

/* Fade-in Animation */
.fadeIn {
    animation: fadeIn 3s;
}

@keyframes fadeIn {
    0% { opacity: 0; }
    70% { opacity: 0; }
    100% { opacity: 1; }
}

/* Flex Container for Centering */
.container {
    max-width: 500px;
    margin: 0 auto;
}

.flexCenter {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* Image Container */
.image {
    margin-top: 20px;
    border-left: 3px solid white;
    padding-left: 10px;
}
        '''
    )

# Function to create flashcards from a list of words and sentences
def create_anki_flashcards(word_sentence_list, cedict_dict, xiandai_dict, init_idx = 1, output_file='mandarin_flashcards.apkg'):
    from anki_mandarin.utils import generate_pinyin, translate_to_english, lookup_simplified_word
    # Create a new Anki model by calling the function
    my_model = create_mandarin_model()

    # Create a new Anki deck
    my_deck = genanki.Deck(
        1975033564,
        'Python_output')

    # Loop over the words and sentences
    for row in word_sentence_list:
        word, sentence, sentence_translation, part_of_speech = \
            (row['word'], row['sentence'], row['sentence_translation'], row['part_of_speech'])

        key = word
        word_pinyin = generate_pinyin(word)
        sentence_pinyin = generate_pinyin(sentence)

        NO_DEFINITION_MESSAGE = f"No definition found for {word}"
        word_entry = cedict_dict.get(word, NO_DEFINITION_MESSAGE)
        word_entryZH = xiandai_dict.get(word, "未找到定义")
        
        if word_entry != NO_DEFINITION_MESSAGE:
            traditional = getattr(word_entry, 'traditional', '')
            meaning = ', '.join(getattr(word_entry, 'meanings', []))
        else:
            traditional = ''
            meaning = ''
        
        sentence_english = sentence_translation if sentence_translation is not None else translate_to_english(sentence)
        part_of_speech = '' if part_of_speech is None else part_of_speech

        # Handle errors in any field (skip the card if data is incomplete)
        if word_pinyin is None or meaning is None or sentence_pinyin is None or sentence_english is None:
            print(f"Skipping card for '{word}' due to missing data.")
            continue

        # Create a new flashcard (with empty placeholders for optional fields)
        my_note = genanki.Note(
            model=my_model,
                fields=[
                    key,                  # 'Key' (Unique identifier, in this case the word)
                    word,                 # 'Simplified' (simplified Chinese characters)
                    traditional,          # 'Traditional' (traditional Chinese characters)
                    word_pinyin,          # 'Pinyin' (pinyin with tone marks)
                    '',                   # 'TwPronunciation' (optional, left empty for now)
                    meaning,              # 'Meaning' (English meaning of the word)
                    word_entryZH,         # 'MeaningZH' (Chinese meaning of the word)
                    part_of_speech,       # 'Part of speech' (What word class ie. Noun, adjective, etc.)
                    '',                   # 'Audio' (left empty for now)
                    sentence,             # 'SentenceSimplified' (simplified version of the example sentence)
                    '',                   # 'SentenceTraditional' (traditional version of the sentence)
                    '',                   # 'SentencePreWord' (the part of the sentence before the word)
                    '',                   # 'SentenceWord' (the target word in the sentence)
                    '',                   # 'SentencePostWord' (the part of the sentence after the word)
                    sentence_pinyin,      # 'SentencePinyin' (pinyin of the example sentence)
                    sentence_english,     # 'SentenceMeaning' (English meaning of the sentence)
                    '',                   # 'SentenceAudio' (left empty for now)
                    '',                   # 'SentenceImage' (optional, left empty for now)
                    '',                   # 'Source' (optional, left empty for now)
                    '',                   # 'Note' (optional, left empty for now)
            ])

        # Add the note to the deck
        my_deck.add_note(my_note)

    # Save the deck to a .apkg file
    genanki.Package(my_deck).write_to_file(output_file)
    print(f"Anki deck '{output_file}' created successfully!")