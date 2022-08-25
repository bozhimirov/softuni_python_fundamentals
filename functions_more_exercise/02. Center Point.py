import math

x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))



if abs(x1) + abs(y1) < abs(x2) + abs(y2):
    print(f'({int(x1)}, {int(y1)})')
else:
    print(f'({int(x2)}, {int(y2)})')




