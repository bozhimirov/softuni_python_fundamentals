# number = int(input())
# search_word = input()
# string = list()
# filtered = list()
#
# for i in range(number):
#     current_string = input()
#     string.append(current_string)
#     if search_word in current_string:
#         filtered.append(current_string)
# print(string)
# print(filtered)
#
# number = int(input())
# search_word = input()
# string = list()
# for i in range(number):
#     string.append(input())
# print(string)
#
# filtered = list()
# for current_string in string:
#     if search_word in current_string:
#         filtered.append(current_string)
#
# print(filtered)
# number = int(input())
# search_word = input()
# string = list()
# filtered = list()
#
# for i in range(number):
#     current_string = input()
#     string.append(current_string)
#     if search_word in current_string:
#         filtered.append(current_string)
# print(string)
# print(filtered)
#
number = int(input())
search_word = input()
string = []
for i in range(number):
    current_string = input()
    string.append(current_string)
print(string)

for i in range(len(string) - 1, -1, -1):
    if search_word not in string[i]:
        string.remove(string[i])

print(string)
