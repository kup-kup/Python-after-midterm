#Konkanok Umnartyuttithum
#6642003026

#lab2 assignment1
p3, p2, p1, res = 1, 1, 2, 0

in1 = int(input("Enter Your Number: "))

print(p3, p2, p1, sep = "\n")
while (True):
    res = p3 + p2 + p1
    if (res >= in1): break

    print(res)
    p3 = p2
    p2 = p1
    p1 = res