# def repeater(str, count):
#     return str * count


# new_str = ""
# for i in range(count):
#     new_str += str
# return new_str

repeater = lambda str, count: str * count

current_string = input()
current_count = int(input())

print(repeater(current_string, current_count))
