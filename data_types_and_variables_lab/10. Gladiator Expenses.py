lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
current_fight = 0
shields_broken = 0
for i in range(lost_fights_count):
    current_fight += 1
    if current_fight % 2 == 0:
        expenses += helmet_price
    if current_fight % 3 == 0:
        expenses += sword_price
        if current_fight % 2 == 0:
            expenses += shield_price
            shields_broken += 1
            if shields_broken % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
