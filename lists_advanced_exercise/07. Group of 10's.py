
data = list(map(int, input().split(", ")))
group = 10
lst = []

while len(data) > 0:
    lst = ([num for num in data if (group - 10) < num <= group])
    print(f"Group of {group}'s: {lst}")
    data = [num for num in data if (group - 10) < num > group]
    group += 10




