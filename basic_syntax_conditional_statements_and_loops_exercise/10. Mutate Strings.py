first = input()
second = input()

for i in range(len(first)):
    if first[i] != second[i]:
        replacement = second[i]
 #       print(replacement)
        word = first[0:i] + replacement + first[i + 1:]
        first = word
        print(word)