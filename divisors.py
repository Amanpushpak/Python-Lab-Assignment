#Program to find divisors of a number.

n=int(input("Enter a number: "))
print("The divisors of the number are: ")
for i in range(1,n+1):
    if(n%i==0):
        print(i)
