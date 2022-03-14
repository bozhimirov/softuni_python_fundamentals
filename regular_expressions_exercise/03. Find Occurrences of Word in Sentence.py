import re
text = input()
word = input()

pattern = rf'\b{word}\b'

result = re.findall(pattern, text, re.I)
print(len(result))
