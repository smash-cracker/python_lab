l = input("Enter a list of numbers: ").split()
l = list(map(int, l))
for x in l:
    if x%2==0:
        l.remove(x)
print(l)
