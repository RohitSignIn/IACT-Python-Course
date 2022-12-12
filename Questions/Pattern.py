#Pattern1
"""
****
****
****
****

star = ''
for i in range (4):
    for j in range(4):
        star += '*'
    print(star)
    star = ''

"""

#Pattern 2:
"""
*
**
***
****

star = ''
for i in range(5):
    for i in range(i):
        star += '*'
    print(star)
    star = ''
"""

#Pattern 3
"""
****
***
**
*

star = ''
for i in range(4, 0, -1):
    for j in range(i):
        star += '*'
    print(star)
    star = ''
"""

#Pattern 4
"""
****
 ***
  **
   *
  
star = '' 
space = ''
counter = 0
for i in range(4, 0, -1):
    for j in range(counter):
        space += ' '
    for j in range(i):
        star += '*'
    print(space + star)
    star = '' 
    space = ''
    counter += 1
"""

#Pattern 5
"""
   *
  **
 ***
**** 

star = '' 
space = ''
counter = 0
no = 0
for i in range(1, 5, 1):
    counter = 4 - i;
    for j in range(counter):
        space += ' '
    for j in range(i):
        star += '*'
    print(space + star)
    star = '' 
    space = ''
    counter += 1
"""

#Pattern 6 - Pyramid
"""
   *    3 1 1+(i-1)
  ***   2 3 2+(i-1)
 *****  1 5 3+(i-1)
******* 0 7 4+(i-1)

no = int(input("Enter No of Rows for Pyramid: "))
space = ''
star = ''
counter = 0
for i in range (1, no+1, 1):
    counter = no - i
    for j in range(counter):
        space += ' '
    
    counter = i + (i-1)
    for j in range(counter):
        star += '*'

    print(space+star)
    space = ''
    star = ''

"""

