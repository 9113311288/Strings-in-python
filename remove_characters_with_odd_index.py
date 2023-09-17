a=input("enter a string")
b=""
for i,char in enumerate(a):
    if i%2==0:
        b+=char
    else:
       continue
print(b,end=" ")