# number = int(input())
# number_list = list()
#
# for i in range(number):
#     current = int(input())
#     number_list.append(current)
#
# filter_word = input()
# filtered = list()
#
# for current_number in number_list:
#     if filter_word == "even":
#         if current_number % 2 == 0:
#             filtered.append(current_number)
#     if filter_word == "odd" and current_number % 2 != 0:
#         filtered.append(current_number)
#     if filter_word == "positive" and current_number >= 0:
#         filtered.append(current_number)
#     if filter_word == "negative" and current_number <= 0:
#         filtered.append(current_number)
# print(filtered)

number = int(input())
positive = list()
negative = list()
odd = list()
even = list()

for i in range(number):
    current = int(input())
    if current % 2 == 0:
        even.append(current)
    else:
        odd.append(current)
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)


filter_word = input()

# if filter_word == 'even':
#     print(even)
# if filter_word == 'odd':
#     print(odd)
# if filter_word == 'positive':
#     print(positive)
# if filter_word == 'negative':
#     print(negative)

print(eval(filter_word))


