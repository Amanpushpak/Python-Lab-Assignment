a=input("Enter a string: ")
str=""
#x=a[8:: -1]
#print(x)

for i in range (len(a)-1,-1,-1):
    str=str+a[i]
   # print(a[i])
    print(str)
