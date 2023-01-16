factor = int(input())
count = int(input())
number = 0
list = []
for num in range(count):

    number = factor + number
    list.append(number)
print(list)
