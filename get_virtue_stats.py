import json
import pandas as pd
import matplotlib.pyplot as plt

filepath = 'summa.json//json//ALL.json'
with open(filepath) as f:
    data = json.load(f)

df = pd.json_normalize(data, sep='_')
flat_dict = df.to_dict()

# Count the number of times the word "prudence" shows up in the summa

fields = ['title', 'text', 'counter', 'body']
prudence_count = 0
justice_count = 0
fortitude_count = 0
temperance_count = 0

for key, value in flat_dict.items():
    if any(field in key for field in fields):
        if str(value[0])[0] == '[':
            line = str(value[0])[2:-2]
        else:
            line = str(value[0])
    
        if "prudence" in line.lower():
            prudence_count += 1
        elif "justice" in line.lower():
            justice_count += 1
        elif "fortitude" in line.lower():
            fortitude_count += 1
        elif "temperance" in line.lower():
            temperance_count += 1

print("The word \'prudence\' occurs {} times in the summa.".format(prudence_count))
print("The word \'justice\' occurs {} times in the summa.".format(justice_count))
print("The word \'fortitude\' occurs {} times in the summa.".format(fortitude_count))
print("The word \'temperance\' occurs {} times in the summa.".format(temperance_count))

virtues = [
    'prudence',
    'justice',
    'fortitude',
    'temperance'
]
counts = [
    prudence_count,
    justice_count,
    fortitude_count,
    temperance_count
]
fig1 = plt.figure()
plt.minorticks_on()
plt.grid(which='minor', axis='y', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', axis='y', linestyle='--', linewidth='0.5', color='black')
plt.bar(virtues, counts, zorder=2)
plt.xlabel('Virtue')
plt.ylabel('Number of Occurences')
fig1.savefig('figures/figure1.png', dpi=300)
