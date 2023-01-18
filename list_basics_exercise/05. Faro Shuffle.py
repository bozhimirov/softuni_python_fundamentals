cards = input().split(" ")
shuffles = int(input())
len_cards = int(len(cards) / 2)

for shuf in range(shuffles):
    list1 = []
    list2 = []
    for i in range(0, len_cards):
        list1.append(cards[i])
    for i in range(len_cards, len(cards)):
        list2.append(cards[i])
    cards.clear()
    for j in range(len_cards):
        cards.append(list1[j])
        cards.append(list2[j])
print(cards)
