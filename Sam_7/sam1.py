with open('статья.txt', encoding='utf-8') as f:
    words = f.read().split()
    word_count = len(words)
    print(f"В статье {word_count} слов.")
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
most_word = max(word_freq, key=word_freq.get)
print(f"Самое часто встречающееся слово: '{most_word}' ({word_freq[most_word]} раз)")