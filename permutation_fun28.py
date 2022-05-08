def fact(n):
    fact_n=1
    for i in range(1,n+1):
         fact_n*=i
    print("Factorial of",n,"=",fact_n)

x=int(input("Enter total:"))
y=int(input("enter value:"))
fact(x)
fact(y)
