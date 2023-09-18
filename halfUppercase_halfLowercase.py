a=input("enter a string:")
n=len(a)
s=""
if n%2==0:
    for i in range(0,n//2):
        s+=a[i].upper()
    for i in range(n//2,n):
        s+=a[i].lower()
    
else:
    for i in range(0,n//2-1):
         s+=a[i].upper()
    for i in range(n//2-1,n):
        s+=a[i].lower()
   
print(s)