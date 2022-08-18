long_enough = ()
valid_characters = False
least_two_digits = False


def lenght_validator(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        print('Password must be between 6 and 10 characters')


def character_validator(password):
    valid_char = 0
    for i in range(len(password)):
        number = ord(password[i])
        if number in range(65, 90):
            valid_char += 1
        elif number in range(48, 57):
            valid_char += 1
        elif number in range(97, 122):
            valid_char += 1
        else:
            valid_char -= 1
    if valid_char == len(password):
        return True
    else:
        print('Password must consist only of letters and digits')


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def digits_validator(password):
    count_numbers = 0
    for i in range(len(password)):
        if password[i] in numbers:
            count_numbers += 1
    if 2 <= count_numbers <= len(password):
        return True
    else:
        print('Password must have at least 2 digits')


def pass_validator():
    if lenght_validator(password):
        if character_validator(password):
            if digits_validator(password):
                print('Password is valid')


password = input()


pass_validator()
