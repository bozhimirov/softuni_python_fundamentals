import math


def division(number):
    sum_nums = 0
    num = number
    while num != 1:
        num = math.ceil(num / 2)
        sum_nums += num
    if sum_nums == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
division(number)


