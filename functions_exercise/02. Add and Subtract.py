def sum_numbers(a, b):
    return a + b


def subtract(current_sum, d):
    return current_sum - d

a, b, d = int(input()), int(input()), int(input())
result = subtract(sum_numbers(a, b), d)
print(result)
