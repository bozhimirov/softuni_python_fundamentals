banned = input().split(", ")

text = input()

for words in banned:
    while words in text:
        text = text.replace(words, "*" * len(words))

print(text)
