n = int(input("Enter the number of terms: "))
def fib(n):
    a=0
    b=1 
    for i in range(1,n+1):
        if i==1:
            print(a,end=" ")
        if i==2:
            print(b,end=" ")
        if i>2:
            c = a+b
            print(c,end=" ")
            a=b
            b=c
fib(n)