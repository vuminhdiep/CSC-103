import random
random.randint(10, 99)
num1 = random.randint(10, 99)
num2 = random.randint(10, 99)
compSel = random.randint(1, 3)
operator = ''
correct_answer = 0
if compSel == 1:
    operator = '+'
    correct_answer = num1+num2
elif compSel == 2:
    operator = '-'
    correct_answer = num1-num2
else:
    operator = '*'
    correct_answer = num1*num2
user_answer = int(input('What is'+str(num1)+operator+str(num2)+'?'))
if user_answer == correct_answer:
    print('Correct!!!')
else:
    print('Wrong!!! It is',correct_answer)
