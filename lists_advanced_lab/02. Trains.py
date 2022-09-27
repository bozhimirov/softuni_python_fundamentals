wagons = int(input())
trains = [0 for i in range(wagons)]
# trains = [0] * wagons
command = input()

while command != "End":
    explode = command.split(" ")
    current = explode[0]
    if current == 'add':
        num_people = int(explode[1])
        trains[-1] += num_people
    if current == 'insert':
        position = int(explode[1])
        num_people = int(explode[2])
        trains[position] += num_people
    if current == 'leave':
        position = int(explode[1])
        num_people = int(explode[2])
        trains[position] -= num_people
    command = input()
print(trains)