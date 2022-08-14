def char_in_range(char1, char2):
    for i in range(ord(char1) + 1, ord(char2)):
        print(chr(i), end=" ")


char1 = input()
char2 = input()
char_in_range(char1, char2)
