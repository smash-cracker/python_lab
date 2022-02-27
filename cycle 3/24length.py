words = input("Enter list of words: ").split()
print(len(max(words, key=len)))
