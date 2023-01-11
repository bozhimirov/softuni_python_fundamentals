import math
people = int(input())
capacity = int(input())
courses = 0
for i in range(people):
    people -= capacity
    courses += 1
    if people <= 0:
        break

print(courses)
