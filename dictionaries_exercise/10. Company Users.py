command = input()
company_users = {}

while command != "End":
    command = command.split(" -> ")
    name = command[0]
    employee_id = command[1]
    if name not in company_users:
        company_users[name] = [employee_id]
    else:
        if employee_id not in company_users[name]:
            company_users[name].append(employee_id)

    command = input()


for key in company_users:
    print(f"{key}")
    for value in company_users[key]:
        print(f'-- {value}')
