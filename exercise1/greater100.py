intlist = input("Enter list of numbers: ").split()
intlist = list(map(int, intlist))
for i,x in enumerate(intlist):
    if x>100:
        intlist[i]="over"
print(intlist)