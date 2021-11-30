n = int(input("Enter the number to be reversed: "))
s = 0
while n>0:
    r=n%10
    s=s*10+r
    n=int(n/10)
print(s)