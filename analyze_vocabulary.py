from math import log
from collections import Counter
from helpers import *
from matplotlib import pyplot as plt
from wordcloud import WordCloud

vocabulary = read_vocabulary('raw_results/all_text_vocabulary.json')

frequencies = Counter()
for word, count in vocabulary.items():
    frequencies[int(count)] += 1

#dump_counter_to_json(frequencies, 'frequencies')

# fig2 = plt.figure()
# number_of_occurences = []
# words_with_frequency = []
# for frequency in frequencies:
#     number_of_occurences.append(int(frequency))
#     words_with_frequency.append(frequencies[frequency])

# plt.plot(number_of_occurences, words_with_frequency)
# plt.xlim(0, 200)
# plt.ylim(0, 100)
# plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='black')
# plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
# plt.minorticks_on()
# plt.xlabel('Number of Occurences')
# plt.ylabel('Number of Words with Occurence')
# fig2.savefig('figures/figure2.png', dpi=300)

# fig3 = plt.figure()
# plt.scatter(number_of_occurences, words_with_frequency, marker='.')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='black')
# plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
# plt.minorticks_on()
# plt.xlabel('Rank')
# plt.ylabel('Frequency')
# plt.title('Zipfian Distribution')
# fig3.savefig('figures/figure3.png', dpi=300)
    
important_words = Counter()
manual_removals = [
    'objection',
    'therefore',
    'say',
    'thing',
    'reply',
    'article',
    'seem',
    'accord',
    'hence',
    'may'
]
for word in vocabulary:
    if vocabulary[word] > 200 and word not in manual_removals:
        important_words.update(Counter({word: vocabulary[word]}))
print(len(vocabulary))
print(len(important_words))

wordcloud = WordCloud(width=800, height=400, background_color='white')
wordcloud.generate_from_frequencies(important_words)
fig4 = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
fig4.savefig('figures/figure4.png', dpi=300)


top_vocab = important_words.most_common(n=20)
top_words = [pair[0] for pair in top_vocab]
top_frequencies = [pair[1] for pair in top_vocab]
fig5 = plt.figure()
plt.bar(top_words, top_frequencies, zorder=2)
plt.xticks(rotation=60)
plt.minorticks_on()
plt.grid(which='minor', axis='y', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', axis='y', linestyle='--', linewidth='0.5', color='black')
plt.subplots_adjust(bottom=0.2)
plt.xlabel('Word')
plt.ylabel('Frequency')
fig5.savefig('figures/figure5.png', dpi=300)