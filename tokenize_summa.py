from collections import Counter
import re
import json
import nltk
import nltk.tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import enchant

from helpers import *

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

def generate_vocabulary(text_filepath):

    with open(text_filepath, 'r') as f:
        text = f.read()
    text = text.lower()

    tokens = nltk.tokenize.word_tokenize(text, language='english')
    punctuation_re = re.compile(r'[^a-zA-Z\s]+$')
    tokens = [
        token.replace("\\", "").replace("'", "").strip("-")
        for token in tokens
        if not punctuation_re.match(token)
    ]

    lemmatizer = WordNetLemmatizer()
    pos_tags = nltk.pos_tag(tokens)
    tokens = []
    for token, pos in pos_tags:
        lemma = lemmatizer.lemmatize(token, pos=pos[0].lower()) if pos[0].lower() in ['a', 'n', 'v'] else lemmatizer.lemmatize(token)
        tokens.append(lemma)

    vocabulary = Counter()
    vocabulary.update(tokens)
    for word in list(vocabulary):
        if (word in stopwords.words('english') or
            not wordnet.synsets(word, lang='eng')):
            
            del vocabulary[word]

    output_filepath = 'raw_results/' + text_filepath.split('/')[-1][:-4] + '_vocabulary.json'
    with open(output_filepath, 'w') as file:
        json.dump(dict(vocabulary.most_common()), file)

    return vocabulary



# generate_vocabulary('raw_results/all_text.txt')
vocabulary = read_vocabulary('raw_results/all_text_vocabulary.json')
print(len(vocabulary))

#print(vocabulary.most_common(n=10))
#print(len([word for word in vocabulary if vocabulary[word] >= 1000])


# # Testing for different word validity methods

# non_eng_words = Counter()
# spell_check_words = Counter()
# special_words = Counter()
# d = enchant.Dict("en_US")
# for word in vocabulary:
#     if not wordnet.synsets(word, lang='eng'):
#         non_eng_words.update(Counter({word: vocabulary[word]}))
#     if not d.check(word):
#         spell_check_words.update(Counter({word: vocabulary[word]}))
#     if not wordnet.synsets(word, lang='eng') and not d.check(word):
#         special_words.update(Counter({word: vocabulary[word]}))

# print(len(non_eng_words))
# print(len(spell_check_words))
# print(len(special_words))

# dump_counter_to_json(non_eng_words, 'synsets_words')
# dump_counter_to_json(spell_check_words, 'spell_check_words')
# dump_counter_to_json(special_words, 'special_words')