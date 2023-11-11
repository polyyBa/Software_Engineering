def count_vowels_consonants(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    consonants_count = 0

    for letter in word:
        if letter.lower() in vowels:
            vowels_count += 1
        elif letter.isalpha():
            consonants_count += 1

    return (vowels_count, consonants_count)


word1 = "hello"
word2 = "world"
word3 = "gffgfdfhjskazrfhncdrhyujc"

print(count_vowels_consonants(word1))
print(count_vowels_consonants(word2))
print(count_vowels_consonants(word3))
