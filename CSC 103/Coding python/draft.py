# # # # h = int(input("Height: "))
# # # # w = int(input("Width: "))
# # # # for i in range(2*h - 1):
# # # #     res = ''
# # # #     if i % (2*h - 2) == 0:
# # # #         res = res + '+' + "-" * (w - 2) + "+"
# # # #         print(res)
# # # #     else:
# # # #         if i % 2 == 0:
# # # #             res = "|" + " " * (w - 2) + "|"
# # # #             print(res)
# # # #         else:
# # # #             print(res)

# # # # # res = 0
# # # # # max = 0

# # # # # for i in range(1,10001):
# # # # #     number_of_divisors = 0
# # # # #     for j in range(1,i + 1):
# # # # #         if i % j == 0:
# # # # #             number_of_divisors += 1
# # # # #     if number_of_divisors > max:
# # # # #         max = number_of_divisors
# # # # #         res = i

# # # # # print("So co so uoc lon nhat la ", res, "va no co ", max, "uoc.")
# # # # num = int(input('Enter a number: '))
# # # # if num%2==0:
# # # #     if num%3==0:
# # # #         print(num,'is divisible by 2 3 6')
# # # #     else:
# # # #         print(num,'is divisible by 2')
# # # #         print(num,'is not divisible by 3 6')
# # # # else:
# # # #     if num%3 == 0:
# # # #         print(num,'is divisible by 3')
# # # #         print(num,'is not divisible by 2 6')
# # # #     else:
# # # #         print(num,'is not divisble by 2 3 6')
# # # # import math
# # # # n = int(input('Input term: '))
# # # # for k in range(0,n+1):
# # # #     print('(z^',k,')/',math.factorial(k),'+', end='')
# # # # print('...')

# # # # import math

# # # # x = int(input('Enter x: '))
# # # # res = 0
# # # # n = int(input('Enter n: '))
# # # # for i in range(0,n+1):
# # # #     res += x**i/math.factorial(i)
    
# # # # print(res)
# # # # res = 0
# # # # max = 0
# # # # for i in range(1,11):
# # # #     number_of_divisors = 0
# # # #     for j in range(1,i + 1):
# # # #         if i % j == 0:
# # # #             number_of_divisors += 1
# # # #     if number_of_divisors > max:
# # # #         max = number_of_divisors
# # # #         res = i

# # # # print("Largest number with the most divisor is ", res, "and it has ", max, "divisors.")
# # # # print(I love {0} and {1}.format('python','java'))
# # # # print(I love {1} and {0}.format('python','java'))
# # # # n = int(input('Enter the number to be reversed: '))
# # # # print('Reverse of',n, 'is: ',end='')
# # # # while n > 0:
# # # #     d = n%10
# # # #     print(d,end='')
# # # #     n = n//10
# # # # print()
# # # # import string
# # # # string.ascii_uppercase
# # # # import random
# # # # compSel = random.choice(string.ascii_uppercase)
# # # # print(compSel)
# # # # import random
# # # # e = random.randrange(-1,2,2)
# # # # print(e)
# # # set1 = set([1, 2, 3, 4, 5])
# # # set2 = set([1, 2, 88, 45, 3])
# # # set3 = set.union(set1, set2)
# # # print(set3)
# # # print()
# # # set4 = set.intersection(set1, set2)
# # # print(set4)
# # # print()
# # # set5 = set1.difference(set2)
# # # print(set5)
# # # print()
# # # set6 = set2.difference(set1)
# # # print(set6)
# # # print()
# # # set8 = set1.symmetric_difference(set2)
# # # print(set8)
# # # print()

# # # #15
# # # set1 = set([1, 2, 3, 4, 4, 5])
# # # set2 = set([1, 2, 88, 45, 3])
# # # #Intersection
# # # for i in set1:
# # #     for v in set2:
# # #         if i == v:
# # #             print(i,end=' ')
# # # print()
# # # #Union
# # # print(*set1, end = ' ')
# # # for i in set2:
# # #     if i not in set1:
# # #         print(i, end = ' ')
# # # print()
# # # # Difference
# # # res = []
# # # for i in set2:
# # #     if i not in set1:
# # #         print(i, end = ' ')
# # #         res.append(i)
# # # print()
# # # for i in set1:
# # #     if i not in set2:
# # #         print(i, end = ' ')
# # #         res.append(i)
# # # print()
# # # # Symmetric difference
# # # print(*res, sep = ' ')

# # grades = [1, 2, 3, 4, 678, 444]
# # setgrades = set(grades)
# # print('Set grade: ',setgrades)
# # # #Add existing item to the set
# # for i in range(0,len(grades)):
# #     setgrades.add(grades[i])
# # # #Add new item to the set
# # new = int(input('Add new grades: '))
# # setgrades.add(new)
# # print(setgrades)
# #Lab5ques4
# # res = ''
# # for i in range(1,6):
# #     num = int(input('Enter number'+str(i)))
# #     if num == 0:
# #         res = str(num) + ' ' + 'Yes  No  No' #use {} {} {}.format
# # print(res)
# # def stringVowels(x):
# #     vowels = ['i','a','o','u','e','I','A','O','U','E']
# #     count = 0
# #     for j in x:
# #         if j in vowels:
# #             count +=1
# #     print('Number of vowels: ',count)
# # x = input('Enter a string: ')
# # stringVowels(x)
# # def permutation(): 
# #     n = int(input('Enter n: '))
# #     r = int(input('Enter r: '))
# #     fact = 1
# #     denom = 1
# #     x = n-r
# #     while n > 0:
# #         fact = fact * n
# #         n -= 1
# #     while x > 0:
# #         denom = denom * x
# #         x -= 1
# #     print(fact/denom)
# # permutation()
# # def permutation(n, r): 
    
# #     fact = 1
# #     denom = 1
# #     x = n-r
# #     while n > 0:
# #         fact = fact * n
# #         n -= 1
# #     while x > 0:
# #         denom = denom * x
# #         x -= 1
# #     print('Permutation is: ',fact/denom)
# # n = int(input('Enter n: '))
# # r = int(input('Enter r: '))
# # permutation(n, r)

# # def combination (n, r):

# #     fact = 1
# #     denom1 = 1
# #     denom2 = 1
# #     x = n-r
# #     while n > 0:
# #         fact = fact * n
# #         n -= 1
# #     while x > 0:
# #         denom1 = denom1 * x
# #         x -= 1
# #     while r > 0:
# #         denom2 = denom2 * r
# #         r -= 1
# #     res = fact/(denom1*denom2)
# #     print('Combination is: ',res)
# # n = int(input('Enter n: '))
# # r = int(input('Enter r: '))
# # combination(n, r)
# #14
# # def list_fcn(x):
# #     count = 0
# #     for i in x:
# #         if i < 0:
# #             count+=1
# #     print('Negative number: ',count)
# # x = [1,2,-3,45,-66,-45,33,4.5,-2.4]
# # list_fcn(x)
# #15
# # def set_fcn(x,y):
# #     z = x.union(y)   
# #     b = set.intersection(x,y)  
# #     print('Union1: ',z)
# #     print('Intersect2: ',b)
# # x = {'apple',1,3,'google',-3.5,2.0}
# # y = {'google','facebook',1,-3.5}
# # set_fcn(x, y)
# #16
# # def sales_fcn(x):

# #     mon = sum(sales['Mon'])
# #     tue = sum(sales['Tue'])
# #     wed = sum(sales['Wed'])
# #     thu = sum(sales['Thu'])
# #     fri = sum(sales['Fri'])
# #     sat = sum(sales['Sat'])
# #     sun = sum(sales['Sun'])
# #     print('Sales daily')
# #     print('Monday =',mon)
# #     print('Tuesday =',tue)
# #     print('Wednesday =',wed)
# #     print('Thursday =',thu)
# #     print('Friday =',fri)
# #     print('Saturday =',sat)
# #     print('Sunday =',sun)
# # sales = {
# #     'Mon': [20,10],
# #     'Tue': [10],
# #     'Wed': [20],
# #     'Thu':[10,5,10],
# #     'Fri':[200],
# #     'Sat':[0],
# #     'Sun':[0]

# # # }
# # # sales_fcn(sales)
# def combination (n, r):    
#     fact = 1
#     denom1 = 1
#     denom2 = 1
#     x = n-r
#     while n > 0:
#         fact = fact * n
#         n -= 1
#     while x > 0:
#         denom1 = denom1 * x
#         x -= 1
#     while r > 0:
#         denom2 = denom2 * r
#         r -= 1
#     res = fact//(denom1*denom2)
#     return res
# # n = int(input('Enter n: '))
# # r = int(input('Enter r: '))

# n = 7
# for i in range(n):
#     lst = []
#     for j in range(i + 1):
#         lst.append(combination(i, j))
#     print(*lst, sep = ' ')
# # def stringVowels():
# #     x = input('Enter a string: ')
# #     vowels = {'i','a','o','u','e','I','A','O','U','E'}
# #     count = 0
# #     for j in x:
# #         if j in vowels:
# #             count +=1
# #     print('Number of vowels: ',count)

# # stringVowels()
    

# def reverse_num():
#     list_num = []
#     x = int(input('Number: '))  
#     while x > 0:
#         y = x%10
#         print(y,end='')
    
#         list_num.append(y)
#         x = x//10
#     print()
#     print(list_num)

# reverse_num()

def star_on_line(x):
    for i in range(1, x+1):
        print("*", end = '')
how_many = int(input('Stars: '))
star_on_line(how_many)
print()