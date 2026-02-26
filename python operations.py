Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = "Hello world"
>>> b = [2,4,6,8,10]
>>> c = 500
>>> 
>>> #Arithemetic operation#
>>> 
>>> c+100
600
>>> c-50
450
>>> c*2
1000
>>> c/10
50.0
>>> c//10
50
>>> c%10
0
>>> c**5
31250000000000
>>> 
>>> #Comparison (relational) operation
>>> 
>>> c==500
True
>>> c!=500
False
>>> c>400
True
>>> c<400
False
>>> c>=400
True
>>> c<=400
False
>>> 
#Logical operation#

#and both true 5>2and 3>1
#or any true 5>2or3<1
#not reverse result not(5>2)

##Assignment operation

c+=100
c
600
c-=300
c
300
c*=5
c
1500
c/=10
c
150.0
c//=10
c
15.0
c%=10
c
5.0

#Bitwie operation

&
SyntaxError: invalid syntax
## &       AND
## XOR NOT LEFT SHIFT RIGHT SHIFT

# Membership operation

a is h
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a is h
NameError: name 'h' is not defined
a in h
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a in h
NameError: name 'h' is not defined
'h' in a
False
'H' in a
True
'H' is not a
True
'H' not in a
False
'z' not in a
True

#Identify operation

#checking variable like
a is b
False
a is a
True
a is not a
False
a is not b
True
