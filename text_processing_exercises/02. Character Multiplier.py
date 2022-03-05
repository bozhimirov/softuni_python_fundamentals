def sum_func(first, second):
    total_sum = 0
    for i in range(len(first)):
        if i < len(second):
            total_sum += ord(first[i]) * ord(second[i])
        else:
            total_sum += ord(first[i])
    return total_sum


def char_multiplier(first, second):
    result = 0
    if len(first) > len(second):
        result = sum_func(first, second)
    else:
        result = sum_func(second, first)

    print(result)


data = input().split(" ")
char_multiplier(data[0], data[1])
