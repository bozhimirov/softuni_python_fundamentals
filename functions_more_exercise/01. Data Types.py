def data_types(method):
    if method == "int":
        result = float(data) * 2
        print(f"{result:.0f}")
    elif method == "real":
        result = float(data) * 1.5
        print(f"{result:.2f}")
    elif method == "string":
        print(f'${data}$')


method = input()
data = input()
data_types(method)

