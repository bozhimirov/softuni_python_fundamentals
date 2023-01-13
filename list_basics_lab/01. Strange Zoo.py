meerkat = []
meerkat.append(input())
meerkat.append(input())
meerkat.append(input())
# tail = input()
# body = input()
# head = input()
# meerkat = [tail, body, head]

# temp = meerkat[0]
# meerkat[0] = meerkat[2]
# meerkat[2] = temp

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# meerkat = [ head, body, tail]
print(meerkat)