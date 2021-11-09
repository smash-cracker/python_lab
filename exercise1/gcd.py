n1,n2 = input("Enter 2 numbers: ").split()
n1 = int(n1)
n2 = int(n2)
gcd = 1
for x in range(2,int(n1/2+1)):
    if n1%x == 0 and n2%x == 0:
        gcd = x
print(gcd)
