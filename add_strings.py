a=input("enter string 1:")
b=input("enter string 2:")
sum=0
carry=0
i=len(a)-1
j=len(b)-1
l=[]
while i>=0 or j>=0: 
    sum=carry
    if i>=0:
     sum+=ord(a[i])-ord('0')
    if j>=0:
       sum+=ord(b[j])-ord('0')
    i-=1
    j-=1
    l.append(sum%10)
    carry=sum//10
if carry!=0:
 l.append(carry)
r=""
for i in reversed(l):
   r+=str(i)
print(r)