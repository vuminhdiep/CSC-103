#“I affirm that I have carried out my academic endeavors with full academic honesty." 
# [Signed,Diep Vu]
#LAB1
#4: Print input/output
print()
print("Python is fun.")
message = "Python is fun."
print(message)

print('Python is fun.')
message='Python is fun.'
print(message)

print("Python\n is fun.")
print(message)

print("Python\n is \nfun.")
print("'Python is fun.'")
print("'Python' is fun\n.")
print("'Python' is fun\\n.")

print("Python\t is fun.")
message="Python\t is fun."
print(message)

print("Python\t is \tfun.")

a = 5
print(a)
print("a =",a)

print("a =")
print(a)

b = a
print('a =', a, '=b')

print('The value of a is',a)

print(1,2,3,4)

print(1,2,3,4,sep='*')

print(1,2,3,4,sep='#',end='&')

a=5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')
print()
x=5
y=10
print('The value of x is {} and y is {}'.format(x,y))

# print(I love {0} and {1}.format('python','java'))
# print(I love {1} and {0}.format('python','java'))

print('Hello {name}, {greeting}'.format(greeting = 'Good morning', name = 'John'))

x = 12.3456789
print('The value of x is %3.2f'%x)
print('The value of x is %3.4f'%x)

input()

name = input()

name = input('Name: ')
print(name)

input('Enter a number: ')
num = input('Enter a number: ')
num = int(input('Enter a number: '))
print(num)
print(num+5)

int('10')
float('10')
print(int('10')+5)
int('2+3')
eval('2+3')

import math
print(math.pi)
print()
# #LAB2
area = int(input('Total Area km2: '))
rank = int(input('Rank for area: '))
water = float(input('Water Area(%): '))
people = int(input('Population: '))
density = people/area
print('Population Density: ',density,'/km2')
print()
# #LAB3
# #2: Fareinheit - Celcius
print('1. F to C')
print('2. C to F')
sel = int(input('Your selection: '))
temp = int(input('Temperature: '))
if sel == 1:
    result = (temp-32)*(5/9)
    print(temp,'F =',result,'C')
else:
    result = (9/5)*temp+32
    print(temp,'C =',result,'F')
print()
# #3: Calculator
print('1. Addition\n2. Subtraction\n3. Multiplication\4. Division\n5. Modulus')
sel = int(input('Your selection: '))
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
if sel == 1:
    result = num1+num2
    print('Result=',num1,'+',num2,'=',result)
elif sel == 2:
    result = num1-num2
    print('Result=',num1,'-',num2,'=',result)
elif sel == 3:
    result = num1*num2
    print('Result=',num1,'*',num2,'=',result)
elif sel == 4:
    result = num1/num2
    print('Result=',num1,'/',num2,'=',result)
else:
    result = num1%num2
    print('Result=',num1,'%',num2,'=',result)
# #4: get family monthly income
inc = int(input('What is your family income: '))
if inc <= 1000:
    print('This family is VERY POOR!')
elif inc <= 2000:
    print('This family is POOR')
elif inc <= 3000:
    print('This family is NORMAL')
elif inc <= 4000:
    print('This family is RICH')
else:
    print('This family is VERY RICH!')
#5: even and odd number
num = int(input('Enter a number: '))
if num%2==0:
    print(num,'is','"Even"')
else:
    print(num,'is','"Odd"')
#6: Check divisible by 2 3 6
num = int(input('Enter a number: '))
if num%2==0:
    if num%3==0:
        print(num,'is divisible by 2 3 6')
    else:
        print(num,'is divisible by 2')
        print(num,'is not divisible by 3 6')
else:
    if num%3 == 0:
        print(num,'is divisible by 3')
        print(num,'is not divisible by 2 6')
    else:
        print(num,'is not divisble by 2 3 6')
#7: guessing number
import random
sel = random.randint(1,10)
guess = int(input('Enter your guess: '))
if sel == guess:
    print('User wins')
elif guess > sel:
    print('Guess is high')
else:
    print('Guess is low')
print()
# #LAB4
# #2: Input x as integer print all numbers from 0 to x
x = int(input('Up to what: '))
i = 0
while i <= x:
    print(i)
    i+=1
#3: Input x as integer print all numbers from x to 0
x = int(input('From what: '))
i = x
while i >= 0:
    print(i)
    i-=1
# #4: Input x as integer print all even numbers from 0 to x
x = int(input('Up to what: '))
i = 0
while i <= x:
    print(i)
    i+=2
#5: Input x as integer print all odd numbers from x to 0
x = int(input('From what: '))
i = x
while i >=0:
    if i%2==1:
        print(i)
        i-=2
    else:
        i-=1
        print(i)
        i-=2
#6: Input x as integer print x number of stars on a line
x = int(input('Enter x: '))
i = 1
while i <= x:
    print('*',end='')
    i+=1
print()
#7: Input x as integer print x number of stars one on each line
x = int(input('Enter x: '))
i = 1
while i <= x:
    print('*')
    i+=1
# #8: Input x as integer print digits of x one on each line
x = int(input('Enter a number: '))
y = len(str(x))
z = 10**(y-1)
i = 0
while i < y:
    a = x//z
    print(a)
    b = x%z
    x = b
    z = z//10
    i+=1
#9: Input x as integer print digits of x in reverse order one on each line
n = int(input('Enter n: '))
while n > 0:
    d = n%10
    print(d)
    n = n//10
#10: Input 10 numbers. Count the even numbers
start = 1
count = 0
while start <= 10:
    num = int(input('Enter number'+str(start)+': '))
    if num%2==0:
        count+=1
    start+=1
print('The number of even numbers: ',count)
#11: Input n as integer. Calculate n!=n*(n-1)*…*2*1
n = int(input('Enter n: '))
fact = 1
count = n
while count > 0:
    fact = fact*count
    count-=1
print('Factorial of',n,'is',fact)
#12: Input two numbers a and b (int) and calculate  ab (a to the power b i.e. multiply a by itself b times)
a = int(input('Enter a: '))
b = int(input('Enter b: '))
while b >= 0:
    print(a**b)
    b -=1
print()
#13: 
n = int(input('Enter the number to be reversed: '))
print('Reverse of',n, 'is: ',end='')
while n > 0:
    d = n%10
    print(d,end='')
    n = n//10
print()
#14: Get five numbers and find the number of zero, negative and positive value
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
#15: Get ten numbers from the user and count the ones that are divisible by 2.
count = 0
start = 1
verb = ''
noun = ''
while start <= 10:
    num = int(input('Enter number' + str(start) + ': '))
    if num%2 == 0:
        count +=1
    start +=1
if count >= 2:
    verb = 'are'
    noun = 'numbers'
    print(count,noun,verb,'divisible by 2')
else:
    verb = 'is'
    noun = 'number'
    print(count,noun,verb,'divisible by 2')
#16: Get ten numbers from the user and count the numbers that are divisible by 2, 3, 6 and none of them. Do not test the numbers by 6 instead use the idea that if a number is divisible by 2 and 3 then it is divisible by 6.
count2 = 0
count3 = 0
count6 = 0
start = 1
verb = ' '
noun = ' '
while start <= 10:
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
if 10 - count2 - count3 + count6 > 1:
    verb = 'are'
    noun = 'numbers'
else:
    verb = 'is'
    noun = 'number'
print(10 - count2 - count3 + count6,noun,verb,'not divisible by any of them')
print()
# #LAB5
# #1.	Input a number (int) and write the binary representation of it.
n = int(input('n: '))
my_str = ''
while n > 0:
   my_str = str(n%2) + my_str
   n = n//2
print(my_str)
#2.	Write a loop which will produce the following output (hint: use two nested loops) 
r = 5
for i in range(1,r+1):
   for j in range(1,i+1):
       print(i,end='')
   print()
###Question 3.1
r = 5
for i in range(1,r+1):
   for j in range(1,i):
       print(' ',end='')
   for j in range(1,2+r-i):
       print('*',end='')
   print()
###Question 3.2
r = 5
for i in range(r+1,1,-1):
   for j in range(i,1,-1):
       print('*',end='')
   print()
#Question 3.3
r = 5
for i in range(1,r+1):
   for j in range(1,r+1-i):
       print(' ',end='')
   for j in range(1,i+1):
       print('*',end='')
   print()
###Question 3.4
r = 5
for i in range(1,r+1):
   for j in range(1,i+1):
       print('*',end='')
   print()
#4.	Get five numbers and for each of them print if they are zero, negative or positive. Write a tabular output.
res = [
   {
       "Number": 0,
       "Zero": "No",
       "Positive": "No",
       "Negative": "No",
   },
   {
       "Number": 0,
       "Zero": "No",
       "Positive": "No",
       "Negative": "No",
   },
   {
       "Number": 0,
       "Zero": "No",
       "Positive": "No",
       "Negative": "No",
   },
   {
       "Number": 0,
       "Zero": "No",
       "Positive": "No",
       "Negative": "No",
   },
   {
       "Number": 0,
       "Zero": "No",
       "Positive": "No",
       "Negative": "No",
   },
]
for i in range(5):
   n = int(input(str("Enter number " + str(i + 1) + ":")))
   res[i]["Number"] = n
   if n < 0:
       res[i]["Negative"] = "Yes"
   elif n == 0:
       res[i]["Zero"] = "Yes"
   else:
       res[i]["Positive"] = "Yes"

print("Number Zero  Positive Negative")
for i in range(5):
   for j in res[i].values():
       print(j, end = '\t')
   print(end = '\n')
#5.	Find the prime numbers in a given range. In the output write at most 10 prime numbers on each line then put a newline. 
start = int(input('From: '))
end = int(input('To: '))
num_prime = 0
for n in range(start,end+1):
    count = 0
    for div in range(2,1+(n//2)):
        if n%div==0:
            count+=1
    if count==0:
        print(n,end=" ")
        num_prime+=1
        if num_prime%10==0:
            print()
print()
#Question 6: Triangle base
base = int(input('Base: '))
n = base
for i in range(1,(n+1)//2 + 1):
    for j in range((n+1)//2 - i):
        print(' ',end='')
    for k in range(1,i*2):
        print('#',end='')
    print()
#Question 6: Diamond
diagonal = int(input('Diagonal: '))
n = diagonal
for i in range(1,(n+1)//2 + 1):
    for j in range((n+1)//2 - i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
for x in range((n+1)//2+1,n+1):
    for y in range(x-(n+1)//2):
        print(' ',end='')
    for z in range((n+1-x)*2-1):
        print('*',end='')
    print()
#Question 6: Rectangle
h = int(input("Height: "))
w = int(input("Width: "))
for i in range(2*h - 1):
    res = ''
    if i % (2*h - 2) == 0:
        res = res + '+' + "-" * (w - 2) + "+"
        print(res)
    else:
        if i % 2 == 0:
            res = "|" + " " * (w - 2) + "|"
            print(res)
        else:
            print(res)
#Question 7:
import math

x = int(input('Enter x: '))
res = 0
n = int(input('Enter n: '))
for i in range(0,n+1):
    res += x**i/math.factorial(i)
    
print(res)
#Question 8: Which integer between 1 and 10000 has the largest number of divisors, and how many divisors does it have? Write a program to find the answers and print out the results. It is possible that several integers in this range have the same, maximum number of divisors. Your program only has to print out one of them. You might need some hints about how to find a maximum value. The basic idea is to go through all the integers, keeping track of the largest number of divisors that you've seen so far. Also, keep track of the integer that had that number of divisors.
res = 0
max = 0
for i in range(1,10001):
    number_of_divisors = 0
    for j in range(1,i + 1):
        if i % j == 0:
            number_of_divisors += 1
    if number_of_divisors > max:
        max = number_of_divisors
        res = i

print("Largest number with the most divisor is ", res, "and it has ", max, "divisors.")
