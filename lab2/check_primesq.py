#lab2 assignment3
end = int(input("Enter Your Number: "))
num = 1

while (num <= end):
    qc = 2
    prime_var = True
    if (num == 1): prime_var = False

    while (qc < num):
        if (num % qc == 0): 
            prime_var = False
            break
        qc += 1

    print(f"{num: >{len(str(end))}}: {prime_var}")
    num += 1