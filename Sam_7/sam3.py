with open('input.txt', 'r') as file:
    text = file.read()
letters = sum(c.isalpha() for c in text)
words = len(text.split())
lines = text.count('\n') + 1

print(f"Input file contains: {letters} letters, {words} words, {lines} lines")