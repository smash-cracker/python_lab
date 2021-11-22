n=input("Enter a year: ")
n=int(n)
if n%4==0 and n%400==0 and n%100==0:
    print("leap")
elif n%4==0 and n%100!=0:
    print("leap")
else:
    print("no")
