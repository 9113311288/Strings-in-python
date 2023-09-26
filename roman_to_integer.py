a=input("enter an integer in roman:")
dict={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
n=len(a)
i=n-1
output=0
while i>=0:
    if i<n-1 and dict[a[i]]<dict[a[i+1]]:
        output-=dict[a[i]]
    else:
        output+=dict[a[i]]
    i-=1
print(output)