key = int(input())
n = int(input())
for i in range(n):
    char = input()
    new_code = ord(char) + key
    new_letter = chr(new_code)
    print(new_letter, end="")
