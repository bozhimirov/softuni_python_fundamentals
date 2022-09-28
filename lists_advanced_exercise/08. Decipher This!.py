words = input().split(' ')
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for position in words:
    new_list = []
    letter_list = []
    for i in position:

        if i in number_list:
            new_list.append(i)
        else:
            letter_list.append(i)
        first_letter = ("".join(new_list))
        first_letter = chr(int(first_letter))
        last_from_word = ("".join(letter_list))
    letter_list[0], letter_list[-1] = letter_list[-1], letter_list[0]
    letter_list = ("".join(letter_list))

    word = first_letter + letter_list
    print(word, end=" ")



