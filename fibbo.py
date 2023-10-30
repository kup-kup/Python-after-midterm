p0 = 0
p1 = 1
p2 = 1

end = 100

print(p1)
print(p2)
while (p0 <= end):
    p0 = p1 + p2
    print(p0)
    p2 = p1
    p1 = p0