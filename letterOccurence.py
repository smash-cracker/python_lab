string = input("Enter string: ")
string = list(string)
count = 0
for i,x in enumerate(string):
    if x == string[0]:
        count+=1
        if count > 1:
            string[i] = "$"
string = "".join(string)
print(string)
