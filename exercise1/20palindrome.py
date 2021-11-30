n = input("Enter string: ")
t = n
n = n[::-1]
if t==n:
    print("string is palindrome")
else:
    print("string is not palindrome")