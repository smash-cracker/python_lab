s = input("Enter string: ")
s = list(s)
count = 0
for i,x in enumerate(s):
    if x==s[0]:
        count+=1
        if count!=1:
            s[i]="$"
print("".join(s))
