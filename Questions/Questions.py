#Reverse of a Number
"""
num = 6798
rev = 0
while num > 0:
    reminder = num % 10
    rev = (rev * 10) + reminder
    num = num // 10

print(rev)
"""

#Print No of NOTES Require for amount a 
"""
amount = int(input("Enter Amount: "))
AllNotes = (100, 50, 20, 1);
NoteReq = []
temp = 0
for i in range(len(AllNotes)):
    # print(amount)
    temp = amount//AllNotes[i]
    if (temp > 0):
        NoteReq.append(temp)
        amount  = amount % AllNotes[i]
    else:
        NoteReq.append(0)

for i in range(len(NoteReq)):
    if (NoteReq[i] == 0):
        continue;    
    match i:
        case 0: 
            out = " Require {} Note of 100 Rs"
            print(out.format(NoteReq[i]))
        case 1: 
            out = " Require {} Note of 50 Rs"
            print(out.format(NoteReq[i]))
        case 2: 
            out = " Require {} Note of 20 Rs"
            print(out.format(NoteReq[i])) 
        case 3: 
            out = " Require {} Note of 1 Rs"
            print(out.format(NoteReq[i]))
"""

#Reverse of List
"""
list1 = [1,2,3,4,5,6]
no = 6
i = 0
j = no - 1
temp = 0
while(i<j):
    temp = list1[i]
    list1[i] = list1[j]
    list1[j] = temp
    i += 1
    j -= 1

print(list1)
"""

#Print Max and Min from a LIST
"""
list1 = [2,4,3,6,7,10] 
no = 6
max, min = list1[0]
for i in range(1, 6, 1)
    if (max < list[i+1]):
        max = list[i+1]
    if (min > list[i+1]):
        min = list[i+1]

output = "Maximum no is {} and the Minimum no is {}";
print(output.format(max, min))
"""

#Find Unique from an List
"""
You have an Integer list of size N where N = [2m+1]. Now in the given list,
'm' numbers are present twice and one number is present only once

We need to find and return that number which is unique in the List list

list1 = [2,4,2,6,4,1,6]; #List of Odd Length
N = 7 #Length of List
uniq = 0

for i in range(N):
    uniq = uniq ^ list1[i]

output = "Unique no is: {}"
print(output.format(uniq))
"""


# FInd Duplicate in List
"""
You are given an List of size N containing each number 1 and N-1 at least once.
There is a single integer value that is present in the List twice.

You're task is to find the integer value that present in the array.

list1 = [1,2,3,4,3]
N = 5
dplc = 0

for i in range(N):
    dplc = dplc ^ list1[i]

for i in range(1, 5, 1):
    dplc = dplc ^ i

print(dplc)
"""

list1 = [1,2,3,4,2]
N = 5
dplc = 0

for i in range(N):
    dplc = dplc ^ list1[i]

for i in range(1, 5, 1):
    dplc = dplc ^ i

output = "Duplicate no is: {}"
print(output.format(dplc))
    
