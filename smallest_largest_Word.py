a = input("Enter a sentence string: ")
b = a.split()
smallest = b[0]
longest = b[0]
for word in b:
        if len(word) >= len(longest):
            longest = word
        if len(word) <= len(smallest):
            smallest = word

print("Longest string is:", longest.upper())
print("Smallest string is:", smallest)
