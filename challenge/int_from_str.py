string = "12l3j;n1lk2b3'k1231km346;l5kj6l4nk"

ls = [int(num) for num in string if num.isnumeric()]
print(ls)
print(sum(ls))