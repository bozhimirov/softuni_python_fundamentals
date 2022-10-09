string = input().split(", ")
string = list(map(int, string))
# for i in range(len(string) - 1, 0, -1):
#     if string1[i] == 0:
#         string1.append(string1[i])
#         string1.remove(string1[i])
# print(string1)

for i in string:
    if i == 0:
        string.append(0)
        string.remove(0)
print(string)
