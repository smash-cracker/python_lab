def factors(n):
    for x in range(1, n+1):
        if n%x == 0:
            print(x)
n = int(input("Enter a numebr"))
factors(n)
