number_characters = int(input())
total_sum = 0
for n in range(number_characters):
    character = input()
    current_sum = ord(character)
    total_sum += current_sum
print(f"The sum equals: {total_sum}")
