i = j = k = 1

while (i <= 12):
    while (j <= 12):
        while (k <= 12):
            print(f"{i: >2} x {j: >2} x {k: >2} = {i * j * k}")
            # print(i, j, k)
            k += 1
        j += 1
        k = 1
        print("\n")
    i += 1
    j = 1
    k = 1

# for i in range(15):    
#     print(f"{i: >2}")