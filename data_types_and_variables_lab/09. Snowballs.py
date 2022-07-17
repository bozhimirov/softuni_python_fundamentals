import sys

N = int(input())
# best_snowball_data = ''
snowball_weight = ()
snowball_time = ()
snowball_value = -sys.maxsize
snowball_quality = ()
for _ in range(N):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = int(weight / time) ** quality
    if value > snowball_value:
        snowball_value = value
        # best_snowball_data = f'{weight} : {time} = {value} ({quality})'
        snowball_quality = quality
        snowball_time = time
        snowball_weight = weight

print(f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})")
