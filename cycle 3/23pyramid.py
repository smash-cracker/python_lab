n = int(input("Enter a number: "))
for i in range(1,n+1):
	for x in range(1,i+1):
		print(i*x,end=" ")
	print() 