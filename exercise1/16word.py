l = input("Enter string: ").split()
checked = list()
for x in l:
    if x not in checked:
        count = 0
        for i in l:
            if x==i:
                count+=1
        print(x, "is repeated ",count, " time")
        checked.append(x)