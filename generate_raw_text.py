import os
import json
import pandas as pd

filepath = 'summa.json//json//ALL.json'
with open(filepath) as f:
    data = json.load(f)

df = pd.json_normalize(data, sep='_')
flat_dict = df.to_dict()

# Write all titles and text to a text file
with open('all_text.txt', 'w') as f:
    for key, value in flat_dict.items():
        if ('title' in key or 'text' in key
             or 'counter' in key or 'body' in key
        ):
            if str(value[0])[0] is '[':
                line = str(value[0])[2:-2]
            else:
                line = str(value[0])
            f.write(line + '\n')