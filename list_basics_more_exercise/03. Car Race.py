numbers = input().split(" ")
numbers = list(map(int, numbers))
len_num = int(len(numbers) / 2)
time_one = 0
time_two = 0
for i in range(len_num):
    if numbers[i] == 0:
        time_one *= 0.8
    else:
        time_one += numbers[i]
for j in range(int(len(numbers) - 1), len_num, -1):
    if numbers[j] == 0:
        time_two *= 0.8
    else:
        time_two += numbers[j]
if time_one < time_two:
    print(f'The winner is left with total time: {time_one:.1f}')
else:
    print(f'The winner is right with total time: {time_two:.1f}')


