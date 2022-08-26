def multiplication_func(num1, num2):
    return num1 * num2


number1 = int(input())
number2 = int(input())
number3 = int(input())
if multiplication_func(multiplication_func(number1, number2), number3) == 0:
    print('zero')
if multiplication_func(multiplication_func(number1, number2), number3) > 0:
    print('positive')
if multiplication_func(multiplication_func(number1, number2), number3) < 0:
    print('negative')
