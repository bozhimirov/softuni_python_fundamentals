numbers = input().split(', ')
numbers = list(map(int, numbers))
even_indexes = list()

# even_indexes = map(lambda  num: , )

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indexes.append(i)

print(even_indexes)
