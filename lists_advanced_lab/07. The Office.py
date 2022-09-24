people = input().split(" ")
people = list(map(int, people))
factor = int(input())

happy = list(filter(lambda emp: emp >= sum(people) / len(people), people))

if len(happy) >= len(people) / 2:
    print(f'Score: {len(happy)}/{len(people)}. Employees are happy!')
else:
    print(f'Score: {len(happy)}/{len(people)}. Employees are not happy!')
