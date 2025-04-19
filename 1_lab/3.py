n = int(input())
fac = 1
while n > 0:
    fac *= n
    print(n)
    n -= 1
print(fac)