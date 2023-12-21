import collections
import re
import json
import nltk
import nltk.tokenize
from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
# nltk.download('wordnet', quiet=True)

def generate_vocabulary(text_filepath):

    with open(text_filepath, 'r') as f:
        text = f.read()
    text = text.lower()

    tokens = nltk.tokenize.word_tokenize(text, language='english')
    punctuation_re = re.compile(r'[^a-zA-Z\s]+$')
    tokens = [token for token in tokens if not punctuation_re.match(token)]

    # lemmatizer = WordNetLemmatizer()
    # tokens = [lemmatizer.lemmatize(token) for token in tokens]

    vocabulary = collections.Counter()
    vocabulary.update(tokens)
    for word in list(vocabulary):
        if word in stopwords.words('english'):
            del vocabulary[word]
    # print(vocabulary.most_common(n=10))
    # print(len([word for word in vocabulary if vocabulary[word] >= 1000]))

    output_filepath = 'raw_results/' + text_filepath.split('/')[-1][:-4] + '_vocabulary.txt'
    with open(output_filepath, 'w') as file:
        json.dump(dict(vocabulary), file)

    return vocabulary

def read_vocabulary(text_filepath):
    with open(text_filepath, 'r') as file:
        vocabulary = file.read()
    return vocabulary



generate_vocabulary('raw_results/all_text.txt')
new_vocabulary = read_vocabulary('raw_results/all_text_vocabulary.txt')