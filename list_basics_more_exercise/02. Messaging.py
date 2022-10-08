numbers = input().split(" ")
string = input()
string_list = list(string)
answer = []
for i in numbers:
    sum = 0
    letter = list(map(int, i))
    for j in range(len(letter)):
        sum += letter[j]
    if sum > len(string_list):
        index = sum // len(string_list)
    else:
        index = sum
    answer.append(string_list[index])
    string_list.remove(string_list[index])
print(''.join(answer))


