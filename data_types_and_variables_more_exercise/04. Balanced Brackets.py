n = int(input())
counter = 0
condition = False
for i in range(n):
    string = input()

    if string == "(":
        counter += 1
    elif string == ")":
        counter -= 1
    if counter < 0:
        condition = True
        break
    if counter > 1:
        condition = True
        break
if condition:
    print("UNBALANCED")
else:
    print("BALANCED")