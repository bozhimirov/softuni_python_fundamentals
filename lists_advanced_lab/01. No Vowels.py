vowels = ['a', 'u', 'o', 'e', 'i', 'A', 'U', 'O', 'I']
text = input()
# no_vowels_text = list()
#
# for ch in text:
#     if ch not in vowels:
#         no_vowels_text.append(ch)

no_vowels_text = [ch for ch in text if ch not in vowels]
print("".join(no_vowels_text))
