#Question 16
count2 = 0
count3 = 0
count6 = 0
start = 1
verb = ' '
noun = ' '
while start <= 5:
    num = int(input('Enter the number' + str(start) + ': '))
    if num%2 == 0:
        count2 +=1
        
        if num%3 == 0:
            count3 += 1
            count6 += 1
            
        
        
    elif num%3 == 0:
        count3 += 1
        
        if num%2 == 0:
            count2 +=1
            count6 +=1
        
            
    start +=1
if count2 > 1:
    verb = 'are'
    noun = 'numbers'
else:
    verb = 'is'
    noun = 'number'
print(count2,noun,verb,'divisible by 2')
if count3 > 1:
    verb = 'are'
    noun = 'numbers'
else:
    verb = 'is'
    noun = 'number'
print(count3,noun,verb,'divisible by 3')
if count6 > 1:
    verb = 'are'
    noun = 'numbers'
else:
    verb = 'is'
    noun = 'number'
print(count6,noun,verb,'divisible by 6')
if 5 - count2 - count3 + count6 > 1:
    verb = 'are'
    noun = 'numbers'
else:
    verb = 'is'
    noun = 'number'
print(5 - count2 - count3 + count6,noun,verb,'not divisible by any of them')

#Question 14
zero = 0
start = 1
neg = 0
pos = 0
verb = ' '
while start <= 5:
    num = int(input('Enter number' + str(start) + ': '))
    if num > 0:
        pos +=1
        
    elif num < 0:
        neg +=1
        
    else:
        zero +=1
        
    start +=1
if pos >= 2:
    verb = 'are'
else:
    verb = 'is'
print('There',verb,pos,'positive value')
if neg >= 2:
    verb = 'are'
else:
    verb = 'is'
print('There',verb,neg,'negative value')
if zero >= 2:
    verb = 'are'
else:
    verb = 'is'
print('There',verb,zero,'zero value')
#Question 10
count = 0
start = 1
while start <= 10:
    num = int(input('Enter number' + str(start) + ': '))
    if num%2 == 0:
        count +=1
    start +=1
print('The number of even numbers:',count)
print('The number of number that is divisible by 2: ',count)
#Question 12
a = int(input('Enter a: '))
b = int(input('Enter b: '))
while b >= 0:
    print(a**b)
    b -=1
print('Done')


