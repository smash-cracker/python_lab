l1 = input("Enter a list of integers: ").split()
l2 = input("Enter a list of integers: ").split()
l1 = list(map(int,l1))
l2 = list(map(int,l2))
if len(l1)==len(l2):
    print("Same length");
else:
    print("Not of same length")
if sum(l1)==sum(l2):
    print("Sum is same");
else:
    print("Sum is not same")
for x in l1:
    if x in l2:
        print(x," is present in both list")

