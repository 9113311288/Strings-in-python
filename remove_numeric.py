a=input("enter a string:")
s=""
for i in a:
    if i.isdigit():
        continue
    else:
        s+=i
print(s)