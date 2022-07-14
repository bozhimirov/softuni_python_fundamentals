number = int(input())
capacity = 255
total_liters = 0
for i in range(number):
    liters = int(input())
    capacity -= liters
    total_liters += liters
    if capacity < 0:
        print('Insufficient capacity!')
        total_liters -= liters
        capacity += liters


print(total_liters)
