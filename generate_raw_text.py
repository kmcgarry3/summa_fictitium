import os
import json

filepath = 'summa.json//json//ALL.json'
with open(filepath) as f:
    data = json.load(f)

# Need something recursive to get all the text
all_text = []
for key, value in data.items():
    print(key)
    if key == 'title' or key == 'text':
        all_text.append(value + '\n')

print(all_text[0:10])