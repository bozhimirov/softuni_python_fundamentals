word = input()
capitals = ["Q", "W", "E", "R", "T", "Y", 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

listo = []
for i in range(len(word)):
    if word[i] in capitals:
        listo += {i}

print(f'{listo}')
