print("Tis script is intended to swap te value of two data variable using 3rd temporary variable")
print()
a=input("Enter first number:")
b=input("Enter second number:")
print("values before swapping :")
print("a="+a)
print("a="+b)
a=int(a)
b=int(b)

c=a
a=b
b=c
print("values after swapping :")
print("a="+str(a))
print("b="+str(b))
