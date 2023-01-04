#Python Loops -
"""
Python has two primitive loop commands:

while loops
for loops
"""


#1.While Loop
"""
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.
"""

#1.1Normal While Loop
i = 1
while i < 6:
  print(i)
  i += 1


#1.2While loop with break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


#1.3While loop with continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#1.4While loop with else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#2 Python For Loops
"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
#The for loop does not require an indexing variable to set beforehand.

#2.1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2.2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#2.3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#2.4
for x in range(6):
  print(x)
