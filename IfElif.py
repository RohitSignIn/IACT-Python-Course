#Python Conditions and If statements
"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.


#normal if else
a = 33
b = 200
if b > a:
  print("b is greater than a")


#if and elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#if elif and else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#Simple Even Odd
num = int(input("Enter a number: "))
num = num & 1
if(num == 0):
    print("Entered number is Even")
else:
    print("Entered number is Odd")

"""

