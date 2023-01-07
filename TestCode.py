Ques1 = { 'question': 'What does the abbreviation HTML stand for', 
        'a': 'HyperText Markup Language', 
        'b': 'Hyper Markup Language',
        'c': 'HyperText M Language', 
        'd': 'HText Markup Language',
        'ans': 'a' }

Ques2 = { 'question': 'The correct sequence of HTML tags for starting a webpage is -', 
        'a': 'Head, Title, HTML, body', 
        'b': 'HTML, Body, Title, Head',
        'c': 'HTML, Head, Title, Body', 
        'd': 'HTML, Head, Title, Body',
        'ans': 'd' }

Ques3 = { 'question': 'Which of the following element is responsible for making the text bold in HTML?', 
        'a': '<pre>', 
        'b': '<a>',
        'c': '<b>', 
        'd': '<br>',
        'ans': 'c' }

print("\n\n"+Ques1['question'] + "\n"+ 
    " a: " + Ques1['a'] + "\n"+
    " b: " + Ques1['b'] + "\n"+
    " c: " + Ques1['c'] + "\n"+
    " d: " + Ques1['d'] + "\n")

q1 = input("Enter Your Choice: ")

print("\n\n"+Ques2['question'] + "\n"+ 
    " a: " + Ques2['a'] + "\n"+
    " b: " + Ques2['b'] + "\n"+
    " c: " + Ques2['c'] + "\n"+
    " d: " + Ques2['d'] + "\n")

q2 = input("Enter Your Choice: ")

print("\n\n"+Ques3['question'] + "\n"+ 
    " a: " + Ques3['a'] + "\n"+
    " b: " + Ques3['b'] + "\n"+
    " c: " + Ques3['c'] + "\n"+
    " d: " + Ques3['d'] + "\n")
    
q3 = input("Enter Your Choice: ")


# **** 
# *  *
# *  *
# ****

# star = ""
# mid_row = ""
# counter = 0
# for a in range(1,5,1):
#     if(a!=1 and a!=4): # a 1 4
#         # For Mid
#         counter = 4-2
#         mid_row = "*"
#         for j in range(counter):
#             mid_row += " "
#         mid_row += "*"
#         print(mid_row)
#     else:
#         # for starting and for ending
#         for i in range(1,5,1):
#             star += "*";
#         print(star)
#         star = ""
