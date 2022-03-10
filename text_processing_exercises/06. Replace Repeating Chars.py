text = input()
result = ""
for i in range(len(text)):
    current_letter = text[i]
    if i == 0:
        result += "".join(current_letter)
    else:
        if text[i] != text[i - 1]:
            result += ''.join(text[i])

print(result)
