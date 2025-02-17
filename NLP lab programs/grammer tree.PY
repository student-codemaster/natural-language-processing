import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk import word_tokenize, pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = 'the brown for step over the lazy dog'

tokens = word_tokenize(sentence)
pos_tags=pos_tag(tokens)
print('POS tags:',pos_tags)

grammar ="""
NP:{<DT>?<JJ>*<NN>}
VP:{<VB.*><NP|PP>}
PP:{<IN><NP>}
"""

chunk_parser = RegexpParser(grammar)

chunk_tree = chunk_parser.parse(pos_tags)


chunk_tree.pretty_print()