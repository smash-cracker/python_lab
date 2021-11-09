s = input("Enter a string: ").split()
d = dict()
for x in s:
    d[x] = 0
for x in s:
   if x in d:
        d[x]+=1
print(d)
