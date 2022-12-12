#Variales can store data of different types, and different types can do different things

"""

1.Text: str
2.Numeric Types: int, float, complex
3.Sequence Types: list, tuple, range
4.Mapping Type: dict
5.Set Types: set, frozenset
6.Boolean Type: bool
7.Binary Types bytes, bytearray, memoryview
8.None Type: NoneType


#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#str

"""
x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#int

"""
x = 60

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#float

"""
x = 10.2

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#complex

"""
x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#list - Mutable
 
"""
x = ["car", "bike", "train"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#Tuple - Immutable

"""
x = ("car", "bike", "train")

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#range

"""
range()

range(start, stop, step) - start(Optional), stop(required), step(Optional)

x = range(10, 0, -2)
for i in x:
    print(n)

x = range(0, 10, 2)
for i in x:
    print(n)

We can also define reverse Sequence like this:
x = range(6)[::-1]
for i in x:
    print(i)


#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#dict - use to map key to val or to store value in key:value pairs

"""
x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#set - print only unique data filter duplicates

"""
x = {"apple", "banana", "banana"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#frozenset - same property as set + immutable

"""
x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#bool

"""
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#bytes - The BYTE data type stores any kind of binary data in an undifferentiated byte stream. - immutable

"""
x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#bytearray - bytearray() method returns a bytearray object (i.e. array of bytes) which is mutable (can be modified) sequence of integers in the range

"""
x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""

#memoryview - The memoryview() function returns a memory view object from a specified object.

"""
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""


#NoneType - NoneType in Python is a data type that simply shows that an object has no value/has a value of None .

"""
x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
