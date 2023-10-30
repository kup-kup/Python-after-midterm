#calculator
#Konaknok Umnartyuttithum
#6642003026

i1 = int(input("Enter First Number: "))
o1 = input("First operator(+, -, *, /): ")
i2 = int(input("Enter First Number: "))
o2 = input("First operator(+, -, *, /): ")
i3 = int(input("Enter First Number: "))

if (o1 == "+"):
    cal = (i1 + i2)
elif (o1 == "-"):
    cal = (i1 - i2)
elif (o1 == "*"):
    cal = (i1 * i2)
elif (o1 == "/"):
    cal = (i1 / i2)

if (o2 == "+"):
    print(cal + i3)
elif (o2 == "-"):
    print(cal - i3)
elif (o2 == "*"):
    print(cal * i3)
elif (o2 == "/"):
    print(cal / i3)