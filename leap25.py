yr= int(input("Enter a year to check: "))

if yr%100!=0 and yr%4==0:
       print("Its a leap year")

elif yr%400==0:
      print("Its a leap year")
else:
    print("It is not a leap year")
