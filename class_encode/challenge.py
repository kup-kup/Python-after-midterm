l1 = [1, 2, 3, 4, 5, 6, 7, "aa", "bb", "11", "4"]
l2 = list()

for item in l1:
    try:
        item_new = int(item)
        l2.append(item_new)
    except ValueError:
        pass

print(max(l2))