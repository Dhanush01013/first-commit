def larger_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return  c
    
x=int(input("Enter a number  "))
y=int(input("Enter second number  "))
z=int(input("Enter third number  "))

result =larger_number (x,y,z)
print("larger number is",result)