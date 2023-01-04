budget = float(input())
price_left = budget
flour_price = float(input())
eggs = 0.75 * flour_price
milk = 1.25 * flour_price
price = 0
breads = 0
price_for_bread = flour_price + eggs + (0.25 * milk)
colored_eggs = 0

while price < budget:
    price_left -= price_for_bread
    if price_left > 0:
        price += price_for_bread
        colored_eggs += 3
        breads += 1
        if breads % 3 == 0:
            colored_eggs -= (breads - 2)
    else:
        break
diff = abs(budget - price)
print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {diff:.2f}BGN left.")




