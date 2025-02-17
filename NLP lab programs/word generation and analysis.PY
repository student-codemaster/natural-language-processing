import spacy
from nltk.corpus import wordnet as wn

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_word(word):
    token = nlp(word)[0]
    pos = token.pos_
    lemma = token.lemma_

    synsets = wn.synsets(lemma)
    meanings = [synset.definition() for synset in synsets]

    return {
        'word': word,
        'lemma': lemma,
        'pos': pos,
        'meanings': meanings,
    }

def generate_words(base_word, affixes):
    generated_words = []
    for affix in affixes:
        generated_words.append(base_word + affix)
    return generated_words

# Example usage
word = 'unhappiness'

# Analyze the word
analysis = analyze_word(word)
print('Word analysis:')
print(f"Original word: {analysis['word']}")
print(f"Lemma: {analysis['lemma']}")
print(f"Part of speech: {analysis['pos']}")
print(f"Meanings: {analysis['meanings']}\n")

# Generate new words
base_word = 'play'
affixes = ['-ful', '-less', '-ing', '-ed']

new_words = generate_words(base_word, affixes)
print(new_words)
