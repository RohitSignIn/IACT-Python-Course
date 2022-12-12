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

#Reverse of an Array
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


    

