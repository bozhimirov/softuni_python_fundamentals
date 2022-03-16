import re

text = input()
while text != "":

    pattern = r'www\.[a-zA-Z0-9\-]+(\.[a-z]+)+'

    domains = re.finditer(pattern, text)

    for domain in domains:
        print(domain[0])

    text = input()
