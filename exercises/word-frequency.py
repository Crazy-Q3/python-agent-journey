words = ["python", "java", "python", "c", "java", "python", "agent", "c"]
word_freq = {}
print("Word Frequency Count:",len(words))
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print(word_freq)
print("不同词数:", len(word_freq))

for word, count in word_freq.items():
    print(word, count)

most_word = max(word_freq, key=word_freq.get)
print("出现最多的是:", most_word, word_freq[most_word])
