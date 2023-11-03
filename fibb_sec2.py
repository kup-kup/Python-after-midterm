#Konkanok Umnartyuttithum
#6642003026

#lab2 assignment1
p3, p2, p1, res = 1, 1, 2, 0

in1 = int(input("Enter Your Number: "))
n = 4

if in1 == 1:
    print(1)
elif in1 == 2:
    print(1, 1, sep="\n")
elif in1 == 3:
    print(1, 1, 2, sep="\n")
else:
    print(1, 1, 2, sep="\n")
    while(n <= in1):
        res = p1 + p2 + p3
        print(res)
        p3, p2, p1 = p2, p1, res
        n += 1