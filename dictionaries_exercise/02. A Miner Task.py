def miner_task():
    my_items = {}

    while True:
        resource = input()

        if resource == "stop":
            break
        quanity = int(input())

        if resource not in my_items:
            my_items[resource] = quanity
        else:
            my_items[resource] += quanity

    for key, value in my_items.items():
        print(f"{key} -> {value}")


miner_task()

