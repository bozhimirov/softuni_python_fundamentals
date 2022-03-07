def encrypted(data):
    result = [chr(ord(ch) + 3) for ch in data]
    print("".join(result))


data = input()
encrypted(data)
