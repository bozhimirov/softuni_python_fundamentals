number = int(input())

positives = list()
negatives = list()
sum_of_negatives = 0

for i in range(number):
    current = int(input())
    if current >= 0 :
        positives.append(current)
    else:
        negatives.append(current)
        sum_of_negatives += current
sum2_of_negatives = 0
for neg in negatives:
    sum2_of_negatives += neg

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum2_of_negatives}')
