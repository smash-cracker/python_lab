s = input("Enter text").split()
checked = list()
for x in s:
    if x not in checked:
        count = 0
        for i in s:
            if i == x:
                count += 1
        print(x, " occured ", count, " times")
        checked.append(x)