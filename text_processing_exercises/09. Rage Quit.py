text = input().upper()
unique_symbols = []
symbols_to_repeat: str = ""
new_text = ""
for i in range(len(text)):
    if text[i].isdigit():
        if i != len(text) - 1:
            if text[i + 1].isdigit():
                cycles = int(text[i]+text[i + 1])
                for l in range(cycles):
                    new_text += symbols_to_repeat
                symbols_to_repeat = ""
            else:
                cycles = int(text[i])
                for j in range(cycles):
                    new_text += symbols_to_repeat
                symbols_to_repeat = ""
        else:
            cycles = int(text[i])
            for k in range(cycles):
                new_text += symbols_to_repeat
            symbols_to_repeat = ""
    else:

        if text[i] not in unique_symbols:
            unique_symbols += text[i]
        symbols_to_repeat += text[i]

print(f"Unique symbols used: {len(unique_symbols)}")
print(new_text)


