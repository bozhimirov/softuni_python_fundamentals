import re

data = input()
pattern = r'\b_[a-zA-Z0-9]+\b'

result = re.findall(pattern, data)

word_list = []

for word in result:
    word_list.append(word[1:])

print(','.join(word_list))
