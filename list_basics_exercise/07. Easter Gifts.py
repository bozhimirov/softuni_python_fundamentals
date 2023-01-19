gifts = input().split(" ")
while True:
    command = input().split(" ")
    if command[0] == "No" and command[1] == "Money":
        break
    elif command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if command[1] == gifts[i]:
                gifts[i] = "None"

    elif command[0] == "Required":

        if 0 < int(command[2]) <= len(gifts) - 1:
            gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
new_gifts = []
for i in range(len(gifts)):
    if gifts[i] != "None":
        print(gifts[i], end=" ")
