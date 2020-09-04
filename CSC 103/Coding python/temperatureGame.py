import random
temp1 = random.uniform(-200,300)
temp2 = random.uniform(-200,300)
print(temp1, temp2, sep=',')
phase1 = input('Enter the starting phase: ')
phase2 = input('Enter the ending phase: ')
if temp1 < 0:
    water1 = 'solid'
    if water1 == phase1:
        print('Correct')
    else:
        print('Wrong, the starting phase is:',water1)
elif temp1 <= 100:
    water1 = 'liquid'
    if water1 == phase1:
        print('Correct')
        
    else:
        print('Wrong, the starting phase is:',water1)
        
else:
    water1 = 'gas'
    if water1 == phase1:
        print('Correct')
        
    else:
        print('Wrong, the starting phase is:',water1)
if temp2 < 0:
    water2 = 'solid'
    if water2 == phase2:
        print('Correct')
    else:
        print('Wrong, the ending phase is:',water2)
elif temp2 <= 100:
    water2 = 'liquid'
    if water2 == phase2:
        print('Correct')
    else:
        print('Wrong, the ending phase is:',water2)
else:
    water2 = 'gas'
    if water2 == phase2:
        print('Correct')
    else:
        print('Wrong, the ending phase is:',water2)
                

user_state = input('What is the state: ')
if phase1 == 'solid' and phase2 == 'liquid':
    state1 = 'melting'
    if user_state == state1:
        print('Correct')
    else:
        print('Wrong, the state is: ',state1)
elif phase1 == 'solid' and phase2 == 'gas':
    state2 = 'sublimation'
    if user_state == state2:
        print('Correct')
    else:
        print('Wrong, the state is: ',state2)
elif phase1 == 'liquid' and phase2 == 'solid':
    state3 = 'freezing'
    if user_state == state3:
        print('Correct')
    else:
        print('Wrong, the state is: ',state3)
elif phase1 == 'liquid' and phase2 == 'gas':
    state4 = 'evaporation'
    if user_state == state4:
        print('Correct')
    else:
        print('Wrong, the state is: ',state4)
elif phase1 == 'gas' and phase2 == 'solid':
    state5 = 'deposition'
    if user_state == state5:
        print('Correct')
    else:
        print('Wrong, the state is: ',state5)
elif phase1 == 'gas' and phase2 == 'liquid':
    state6 = 'condensation'
    if user_state == state6:
        print('Correct')
    else:
        print('Wrong, the state is: ',state6)
    
    
    


