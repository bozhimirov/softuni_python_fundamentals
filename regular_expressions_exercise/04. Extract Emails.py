import re

text = input()
# pattern = r'\b[a-zA-Z0-9]+(\-|\_|\.)*([a-zA-Z0-9]*)@[a-zA-Z]+\-*[a-zA-Z]+\.*[a-zA-Z]+(\.[a-zA-Z]+)\b'
pattern = r'(^|(?<=\s))[a-zA-Z0-9]+[\-_.]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+'
# user_pattern = r'\b[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*'
# host_pattern = r'[a-zA-Z]+\-*[a-zA-Z]+\.*[a-zA-Z]+(\.[a-zA-Z]+)\b'

# pattern = rf'{user_pattern}@{host_pattern}'

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])



