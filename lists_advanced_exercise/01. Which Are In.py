string1 = input().split(", ")
# string2 = input().split(", ")

string2 = input()
new_string = [el for el in string1 if el in string2]

print(new_string)

