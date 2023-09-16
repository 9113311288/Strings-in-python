a=input("enter a string")
word=0
space=0
for i in a:
    if i== ' ':
        space+=1
print("no. of words",space+1)
print("no. of spaces :",space)