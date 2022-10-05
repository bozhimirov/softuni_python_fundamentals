numbers = input().split(" ")
number = list(map(int, numbers))
skipped = int(input())
count = 0

result = []
new_number = []

while len(result) != len(numbers):
    len_number = len(number)
    for i in range(0, len_number):
        count += 1
        if count % skipped == 0:
            result.append(number[i])
        else:
            new_number.append(number[i])
    number = new_number
    new_number = []
print(str(result).replace(" ", ''))


