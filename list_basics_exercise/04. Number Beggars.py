numbers = input().split(', ')
copy_numbers = list(map(int, numbers))
beggars = int(input())
list = []

for j in range(beggars):
    num = 0
    for i in range(j, len(copy_numbers), beggars):
        num += copy_numbers[i]
    list.append(num)

print(list)

