#“I affirm that we have carried out all of our academic endeavors with full academic honesty.” [Signed, Diep Vu]

# #1
def menu(a):
    print(a)
m1 = '1. F to C'
m2 = '2. C to F'
sel = int(input('Your selection: '))

if sel == 1:
    menu(m1)
    f = int(input('Temperature: '))
    c = (f-32)*5/9
    print(f,'F =',c,'C')
else:
    menu(m2)
    c = int(input('Temperature: '))
    f = (9/5)*c+32
    print(c,'C =',f,'F')
#2
def num(x):
    for i in range(0,x+1):
        print(i)
up_to = int(input('Up to: '))
num(up_to)
# #3
def num_from(x):
    for i in range(x,-1,-1):
        print(i)
    
from_num= int(input('From what: '))
num_from(from_num)
#4
def even(x):
    for i in range(0,x,2):
        print(i)
even_num = int(input('Even: '))
even(even_num)
#5
def odd(x):
    if x%2 == 0:
        for i in range(x-1,0,-2):
            print(i)
    else:
        for i in range(x,0,-2):
            print(i)
odd_num = int(input('Odd: '))
odd(odd_num)
#6
def star_on_line(x):
    for i in range(1, x+1):
        print("*", end = '')
how_many = int(input('Stars: '))
star_on_line(how_many)
print()
# #7
def star_each_line(x):
    for i in range(1,x+1):                    
        print('*')
how_many = int(input('Stars: '))
star_each_line(how_many)
#8                                         
def digits_each_line(x):    
    y = len(str(x))
    z = 10**(y-1)
    i = 0
    while i < y:
        a = x//z
        print(a)
        b = x%z
        x = b
        z = z//10
        i = i + 1
x = int(input('What number: '))                   
                                                    
digits_each_line(x)
#9
def reverse_digits_each_line(x):
    while x > 0:
        y = x%10
        print(y)
        x = x//10
x = int(input('Number: '))
reverse_digits_each_line(x)
#10
def power(x):
    print(x)
a = int(input('a: '))
b = int(input('b: '))
x = a**b
power(x)
#11                                                
def reverse_num():
    list_num = []
    x = int(input('Number: '))  
    while x > 0:
        y = x%10
        print(y,end='')
        list_num.append(y)
        x = x//10
    print()
    print(list_num)

reverse_num()
#12
def test_odd_even(x):
    if num%2 == 0:
        print('Even')
    else:
        print('Odd')
num = int(input('Enter number: '))
test_odd_even(num)
#13
def divisible(x,y):
    if num1 % num2 == 0:
        print(num1,'is divisible by',num2)
    else:
        print(num1,'is not divisible by',num2)
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
divisible(num1,num2)
#14
def list_fcn(x):
    count = 0
    for i in x:
        if i < 0:
            count+=1
    print('Negative number: ',count)
x = [1,2,-3,45,-66,-45,33,4.5,-2.4]
list_fcn(x)
#15
def set_fcn(x,y):
    z = x.union(y)   
    b = set.intersection(x,y)  
    print('Union1: ',z)
    print('Intersect2: ',b)
x = {'apple',1,3,'google',-3.5,2.0}
y = {'google','facebook',1,-3.5}
set_fcn(x, y)
#16
def sales_fcn(x):

    mon = sum(sales['Mon'])
    tue = sum(sales['Tue'])
    wed = sum(sales['Wed'])
    thu = sum(sales['Thu'])
    fri = sum(sales['Fri'])
    sat = sum(sales['Sat'])
    sun = sum(sales['Sun'])
    print('Sales daily')
    print('Monday =',mon)
    print('Tuesday =',tue)
    print('Wednesday =',wed)
    print('Thursday =',thu)
    print('Friday =',fri)
    print('Saturday =',sat)
    print('Sunday =',sun)
sales = {
    'Mon': [20,10],
    'Tue': [10],
    'Wed': [20],
    'Thu':[10,5,10],
    'Fri':[200],
    'Sat':[0],
    'Sun':[0]

}
sales_fcn(sales)

#17
def stringVowels(x):
    vowels = ['i','a','o','u','e','I','A','O','U','E']
    count = 0
    for j in x:
        if j in vowels:
            count +=1
    print('Number of vowels: ',count)
x = input('Enter a string: ')
stringVowels(x)
#18
def fact(n):
    res=1
    if n == 0:
        return res
    else: 
        for c in range(1,n+1):
            res = res*c
    
        return res
n = int(input('n: '))
r = int(input('r: '))
print('Factorial:',fact(n))

#19
def perm(n,r): 
    result = fact(n)//fact(n-r)
    return result

print('Permutation:',perm(n,r))

#20
def combn (n, r):    
    my_res = perm(n,r)//fact(r)
    return my_res
print('Combination:',combn(n,r))
#21

for i in range(0, n+1):
    for j in range(1, n+1-i):
        print("  ", end="")
    for k in range(0, i+1):
        print('  ',combn(i,k), end="")
    
    print()

