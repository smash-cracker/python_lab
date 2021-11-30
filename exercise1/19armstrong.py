n = int(input("Enter the number to be checked: "))
x = n
s = 0
while n>0:
    r=n%10
    s=s+(r*r*r)
    n=int(n/10)
if x==s:
    print("Number is armstrong")
else:
    print("Number is not armstrong")