sentence = input("Введите предложение на английском: ")

print("Длина предложения:", len(sentence))

lower_sentence = sentence.lower()
print("Предложение в нижнем регистре:", lower_sentence)

vowels = "aeiou"
count_vowels = 0
for letter in lower_sentence:
    if letter in vowels:
        count_vowels += 1
print("Количество гласных в предложении:", count_vowels)

new_sentence = lower_sentence.replace("ugly", "beauty")
print("Предложение с заменой слова 'ugly' на 'beauty':", new_sentence)

if lower_sentence.startswith("the") and lower_sentence.endswith("end"):
    print("Предложение начинается с 'The' и заканчивается на 'end'")
else:
    print("Предложение не соответствует условиям")