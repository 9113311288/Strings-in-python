a=input("enter a string")
b=a.split()
i=0
count=0
while i<len(b):
    for j in b:
     if a[i]==j:
      count+=1
    print(b[i],"found",count,"times")
    i=i+1