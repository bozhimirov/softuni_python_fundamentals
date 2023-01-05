ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
quantity = int(input())
days = int(input())
total_cost = 0
total_spirit = 0
condition_5th_day = False
for i in range(1, days+1):
    condition_5th_day = False
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        total_spirit += 5
        total_cost += ornament_set * quantity
    if i % 3 == 0:
        total_spirit += 13
        total_cost += (tree_skirt * quantity) + (tree_garlands * quantity)
        condition_5th_day = True
    if i % 5 == 0:
        total_spirit += 17
        total_cost += tree_lights * quantity
        if condition_5th_day:
            total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        total_cost += 23
        if i == days:
            total_spirit -= 30


print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')







