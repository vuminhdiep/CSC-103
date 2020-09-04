# “I affirm that I have carried out my academic endeavors with full academic honesty." [Signed, Diep Vu]
print('1. Math calculation')
print('2. Guess the next character')
print('3. Exit')
choice = int(input('Your choice: '))
exit = False
while exit == False:
    if choice == 1:
        ques = int(input('How many questions? '))
        count = 0
        for i in range(1,ques+1):
            import random
            num1 = random.randint(0,101)
            num2 = random.randint(0,101)
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
            user_answer = int(input('What is' + ' ' + str(num1) + operator+ str(num2) +' '+ '? '))
            if user_answer == correct_answer:
                print('Correct!!!')
                count+=1
            else:
                print('Wrong!!! It is',correct_answer)

        print('Your score is: ',count,'/',ques)
        print('1. Math calculation')
        print('2. Guess the next character')
        print('3. Exit')
        choice = int(input('Your choice: '))
    if choice == 2:        
        ques = int(input('How many questions? '))
        count = 0
        for i in range(1,ques+1):
            import random
            i = random.randint(0,25)
            e = random.randrange(-1,2,2)
            word = ''
            if e == -1:
                word = 'before'
            else:
                word = 'after'
            import string
            alphabet = string.ascii_uppercase
            compSel = alphabet[i]
            correct = alphabet[i+e]
            guess = input('What comes' + ' ' + word + ' ' + compSel + ' ' + '? ')
            if correct == guess:
                print('Correct! Bravo!!!!')
                count+=1
            else:
                print('Incorrect! It was',correct)
        print('Your score is',count,'/',ques)
        print('1. Math calculation')
        print('2. Guess the next character')
        print('3. Exit')
        choice = int(input('Your choice: '))
    if choice == 3:
        answer = input("Are you sure? ")
        if answer == "Yes":
            print("Bye")
            exit = True
        else:
            print('1. Math calculation')
            print('2. Guess the next character')
            print('3. Exit')
            choice = int(input('Your choice: '))
