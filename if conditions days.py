num=int(input("Enter a number :"))
if num>=1:
    print("positive number")

elif num==0:
    print("Zero")

else:
    print("Negative number")


##


num2=int(input("enter a number :"))

if num2%2==1:
    print("Odd number")
else: 
    print("Even number")

    ##



num3=int(input("Enter a number :"))
num4=int(input("Enter second number :"))

if num3 > num4:
    print("First number is larger than 2nd number") 
    print(num3)
else:
    print("First number is larger than 1st number")
    print(num4) 

##

age=int(input("Enter the age : "))

if age>18:
    print("Eligible for vote")

else:
    print("Ineligible for vote")

### 


word=input("enter a word:")
if word[0] in ['a','e','i','o','u']:
    print("an", word)
else:
    print("a", word)

##    

ex=int(input("Enter your work experience :"))

salary=int(input("Enter your current salary :"))

if ex >5 and salary >50000:
    print("10% Bonus ")

else:
    print("5% Bonus")

##

mark=int(input("Enter the mark :"))

if mark>75:
    print("Distingtion")

elif mark >40:
    print("pass")

else:
    print("fail") 


##    

name=input("Enter consumer name :")
ci=int(input("Enter consumer id : "))
unit=int(input("How much unit used :"))

if unit>=300:
    print("Payable Amount is",unit*6)


elif unit>201:
    print("Payable Amount is",unit*4)

elif unit>101:
    print("Payable Amount is",unit*2.5)

else:
    print("Payable Amount is",unit*1.5) 


##

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))

if num1>=num2:
    if num1==num2:
        print(num1,"is equal than ",num2)

    else:
        print(num1,"greater than ",num2) 

else:
    print(num1,"is less than",num2) 


##

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

## 







