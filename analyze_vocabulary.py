from math import log
from collections import Counter
from helpers import *
from matplotlib import pyplot as plt

vocabulary = read_vocabulary('raw_results/all_text_vocabulary.json')

frequencies = Counter()
for word, count in vocabulary.items():
    frequencies[int(count)] += 1

dump_counter_to_json(frequencies, 'frequencies')

fig2 = plt.figure()
number_of_occurences = []
words_with_frequency = []
for frequency in frequencies:
    number_of_occurences.append(int(frequency))
    words_with_frequency.append(frequencies[frequency])

plt.plot(number_of_occurences, words_with_frequency)
plt.xlim(0, 200)
plt.ylim(0, 100)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='black')
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
plt.minorticks_on()
plt.xlabel('Number of Occurences')
plt.ylabel('Number of Words with Occurence')
fig2.savefig('figures/figure2.png', dpi=300)

fig3 = plt.figure()
plt.scatter(number_of_occurences, words_with_frequency, marker='.')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='black')
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
plt.minorticks_on()
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Zipfian Distribution')
fig3.savefig('figures/figure3.png', dpi=300)