with open('inpput.txt') as forbidden_words, open('text.txt') as to_change:
	pattern, text = forbidden_words.read().split(), to_change.read()
text_lower = text.lower()
for word in pattern:
	text_lower = text_lower.replace(word, '*' * len(word))
result = ''.join((y, x)[x == '*'] for x, y in zip(text_lower, text))
print(result)