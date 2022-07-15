group = int(input())
days = int(input())
earn = 0
current_day = 0

for i in range(days):
    days -= 1
    current_day += 1
    if current_day % 10 == 0:
        group -= 2
    if current_day % 15 == 0:
        group += 5
    earn += 50 - (2 * group)
    if current_day % 3 == 0:
        earn -= 3 * group
    if current_day % 5 == 0:
        earn += 20 * group
        if current_day % 3 == 0:
            earn -= 2 * group
per_person = int(earn / group)
print(f"{group} companions received {per_person} coins each.")



