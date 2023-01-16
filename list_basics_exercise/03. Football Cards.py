count_a = 11
count_b = 11
info = input().split(" ")
player_loses = []
condition = False
for card in info:
    if card not in player_loses:
        player_loses.append(card)
        if "A" in card:
            count_a -= 1
        elif "B" in card:
            count_b -= 1

        if count_a < 7 or count_b < 7:
            condition = True
            break
print(f'Team A - {count_a}; Team B - {count_b}')
if condition:
    print("Game was terminated")