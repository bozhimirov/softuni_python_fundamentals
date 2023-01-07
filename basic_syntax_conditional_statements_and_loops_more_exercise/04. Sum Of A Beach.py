letters = input()

output = 0

string_names = ["water", "sun", "fish", "sand"]
lower_letters = letters.lower()
for i in range(0, len(letters) + 1):

    if lower_letters[:3] in string_names:
        output += 1
    elif lower_letters[:4] in string_names:
        output += 1
    elif lower_letters[:5] in string_names:
        output += 1
    lower_letters = lower_letters[1:]
print(output)
