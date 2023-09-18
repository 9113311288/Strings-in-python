def isomorphic(str1,str2):
  def helpers(word):
    list1=[]
    dict1={}
    i=1
    for w in word:
      if w not in dict1:
        dict1[w]=i
        i+=1
      list1.append(dict1[w])
    return list1
  return helpers(str1)==helpers(str2)

if __name__=="__main__":
    str1=input("enter string 1:")
    str2=input("enter string 2:")
    print(isomorphic(str1,str2))