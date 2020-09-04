r = 5
c = 3
for r1 in range(1,r+1):
    for c1 in range(1,c+1):
        if r1%2 == 1:
            print('XO',end='')
        else:
            print('OX',end='')
    print()

r = 5
for i in range(1,r+1):
    for j in range(1,i+1):
        print('*',end='')
    print()

        
