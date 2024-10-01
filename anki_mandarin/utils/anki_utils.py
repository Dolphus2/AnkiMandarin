import genanki



# Create a new Anki model for Mandarin flashcards
# Every unique model should have a unique model ID. Use print(random.randrange(1 << 30, 1 << 31))
# Function to create flashcards from a list of words and sentences

def create_mandarin_model():
    # Create a new Anki model for Mandarin flashcards with custom templates and CSS
    return genanki.Model(
        1297553304,
        'Advanced Model with All Refold Mandarin 1k Fields',
        fields=[
            {'name': 'Key'},
            {'name': 'Simplified'},
            {'name': 'Traditional'},
            {'name': 'Pinyin'},
            {'name': 'Meaning'},
            {'name': 'Part of speech'},
            {'name': 'Audio'},
            {'name': 'SentenceSimplified'},
            {'name': 'SentenceTraditional'},
            {'name': 'SentencePinyin'},
            {'name': 'SentenceMeaning'},
            {'name': 'SentenceAudio'},
            {'name': 'SentenceImage'},
            {'name': 'Note'},
            {'name': 'TwPronunciation'}
        ],
        templates=[
            {
                'name': 'Refold_genanki_py',
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
 margin-bottom: 10px
}

.card {
 font-family: Georgia; 
 font-size: 10px; 
 text-align: left; 
 background-color: rgb(47,47,49);
 color: #fff;
 padding: 20px;
}

.hanzi {
 font-family: Kai;  
 font-size: 78px;
 border-bottom: 3px solid rgba(0,0,0,0);
 transition: border 0.5s ease,  padding 0.5s ease;
 margin-top: 20px;
}

.hanzi.whover {
 cursor: pointer;
}

.hanzi.whover:hover {
}

.hanzi.whover::before {
 font-family: Palatino; 
 content: var(--pinyin);
 position: absolute;
 font-size: 22px;
 color: #55DD55;
 padding-left: 10px;
 padding-right: 10px;
 padding-bottom: 5px;
 border-left: 3px solid white;
 transform: translate(-10px,  -40px);
 opacity: 0;
 transition: opacity 0.5s ease;
 height: 140px;
 padding-top: 0px;
}

.hanzi.whover:hover::before {
 opacity: 1;
}

.sentence {
 font-family: Kai; 
 font-size:30px; 
 text-align:left;
 transition: padding 0.5s ease;
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
 color: #55DD55;
}

.pinyinSen {
 font-family: Palatino; 
 font-size: 20px; 
 color: #55DD55; 
 text-align:left;
}

.english {
 font-family: Didot; 
 font-size: 16px;
}

.meaningSent{
 font-family: Didot; 
 font-size: 16px;  
 text-align:left
}

.description{
 font-family: Didot; 
 font-size: 16px; 
 color: #575757;
}

.image{
	margin-top: 20px;
	border-left: 3px solid white;
	padding-left: 10px;
}
        '''
    )

# Function to create flashcards from a list of words and sentences
def create_anki_flashcards(word_sentence_list, cedict_dict, init_idx = 1, output_file='mandarin_flashcards.apkg'):
    from anki_mandarin.utils import generate_pinyin, translate_to_english, lookup_simplified_word
    # Create a new Anki model by calling the function
    my_model = create_mandarin_model()

    # Create a new Anki deck
    my_deck = genanki.Deck(
        1496240689,
        'Mandarin Flashcards')

    # Loop over the words and sentences
    key = init_idx -1
    for word, sentence in word_sentence_list:
        key += 1
        word_pinyin = generate_pinyin(word)
        sentence_pinyin = generate_pinyin(sentence)
        word_entry = lookup_simplified_word(word, cedict_dict)
        
        NO_DEFINITION_MESSAGE = f"No definition found for {word}"
        if word_entry != NO_DEFINITION_MESSAGE:
            traditional = getattr(word_entry, 'traditional', '')
            meaning = ', '.join(getattr(word_entry, 'meanings', []))
        else:
            traditional = ''
            meaning = ''

        sentence_english = translate_to_english(sentence)

        # Handle errors in any field (skip the card if data is incomplete)
        if word_pinyin is None or meaning is None or sentence_pinyin is None or sentence_english is None:
            print(f"Skipping card for '{word}' due to missing data.")
            continue

        # Create a new flashcard (with empty placeholders for optional fields)
        my_note = genanki.Note(
            model=my_model,
            fields=[
                str(key),             # 'Key' (some numeric or unique identifier)
                word,                 # 'Simplified' (simplified Chinese characters)
                traditional,          # 'Traditional' (traditional Chinese characters)
                word_pinyin,          # 'Pinyin' (pinyin with tone marks)
                meaning,              # 'Meaning' (English meaning of the word)
                '',                   # 'Part of speech' (left empty for now, to be filled manually or via another process)
                '',                   # 'Audio' (left empty for now)
                sentence,             # 'SentenceSimplified' (simplified version of the example sentence)
                '',                   # 'SentenceTraditional' (traditional version of the sentence)
                sentence_pinyin,      # 'SentencePinyin' (pinyin of the example sentence)
                sentence_english,     # 'SentenceMeaning' (English meaning of the sentence)
                '',                   # 'SentenceAudio' (left empty for now)
                '',                   # 'SentenceImage' (optional, left empty for now)
                '',                   # 'Note' (optional, left empty for now)
                ''                    # 'TwPronunciation' (optional, left empty for now)
            ])

        # Add the note to the deck
        my_deck.add_note(my_note)

    # Save the deck to a .apkg file
    genanki.Package(my_deck).write_to_file(output_file)
    print(f"Anki deck '{output_file}' created successfully!")