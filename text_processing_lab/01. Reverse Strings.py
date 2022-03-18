text = input()

while text != "end":
    rev = reversed(text)
    # reversed_text = ""
    # for char in rev:
    #     # print(char, end="")
    #     pass
    # reversed_text += char
    reversed_text = "".join(rev)
    # new_text = text[::-1]
    print(f"{text} = {reversed_text}")
    # print(new_text)

    text = input()
