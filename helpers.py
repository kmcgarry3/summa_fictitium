from collections import Counter
import json

def read_vocabulary(json_filepath):
    with open(json_filepath, 'r') as file:
        vocabulary = Counter(json.load(file))
    return vocabulary

def dump_counter_to_json(counter, name):
    with open(name + '.json', 'w') as file:
     json.dump(dict(counter.most_common()), file)