import re

patternt = r'\d+'

while True:
    text = input()

    if not text:
        break

    result = re.findall(patternt, text)

    if len(result) > 0:
        print(" ".join(result), end=' ')
