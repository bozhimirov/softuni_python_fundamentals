import re


text = input()

matches = re.findall(r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b", text)
print(" ".join(matches))
