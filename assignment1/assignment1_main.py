# Part 1: 20 students's ages, sum and average
sum = 0

for i in range(20):
    age = input(f"Enter student number {i + 1}'s age:")
    sum += int(age)

age_ave = sum / 20
print(f"The sum of the students's ages is {sum}")
print(f"The average age is {age_ave}")

# Part 2: Swap 2 variables
a = 20
b = 10
print("\nbefore swap:")
print(f"a = {a}, b = {b}")

a, b = b, a # using python feature

print("after swap:")
print(f"a = {a}, b = {b}")

# using math
a = a + b
b = a - b
a = a - b

print("after swap (again):")
print(f"a = {a}, b = {b}")