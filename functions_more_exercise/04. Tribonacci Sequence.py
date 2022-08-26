number = int(input())
first_num = 0
sec_num = 0
third_num = 1
sum_three = first_num + sec_num + third_num
print(f' {sum_three}', end="")
for _ in range(number - 1):
    current_first_num = first_num
    current_sec_num = sec_num
    current_third_num = third_num
    current_sum_three = current_first_num + current_sec_num + current_third_num
    third_num = current_sum_three
    sec_num = current_third_num
    first_num = current_sec_num
    print(f' {current_sum_three}', end="")
