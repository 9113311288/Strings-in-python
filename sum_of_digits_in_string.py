a=input("enter a string with digits:")
digit=[]
for i in a:
    if (i.isdigit()):
        digit.append(int(i))
print(digit)
print(sum(digit))