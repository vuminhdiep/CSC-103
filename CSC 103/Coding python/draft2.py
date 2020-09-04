




#Print isoceles triangle with base
# base = int(input('Base: '))
# n = base
# for i in range(1,(n+1)//2 + 1):
#     for j in range(0,(n+1)//2 - i+1):
#         print(' ',end='')
#     for k in range(1,i*2):
#         print('*',end='')
#     print()

# def fact(n):
#     res=1
#     for c in range(1,n+1):
#         res = res*c
    
#     return res
# rows = int(input("Enter the number of rows : "))
# for i in range(0, rows):
#     for k in range(1, rows-i):
#         print("  ", end="")
#     for k in range(0, i+1):
#         coff = int(fact(i)/(fact(k)*fact(i-k)))
#         print("  ", coff, end="")
#     print()

# def fact(n):
#     res=1
#     for c in range(1,n+1):
#         res = res*c
    
#     return res
# n = int(input('n: '))
# r = int(input('r: '))
# print('Factorial:',fact(n))

#19
# def perm(n,r): 
#     result = fact(n)//fact(n-r)
#     return result

# print('Permutation:',perm(n,r))

# #20
# def combn (n, r):    
#     my_res = perm(n,r)//fact(r)
#     return my_res
# print('Combination:',combn(n,r))
# def stringVowels(x):
#     vowels = {'i','a','o','u','e','I','A','O','U','E'}
#     count = 0
#     for j in x:
#         if j in vowels:
#             count +=1
#     print('Number of vowels: ',count)
# x = input('Enter a string: ')
# stringVowels(x)
# for i in range(0, n+1):
#     for j in range(1, n+1-i):
#         print("  ", end="")
#     for k in range(0, i+1):
        
#         print('  ',combn(i,k), end="")
    
#     print()
# def stringVowels(x):
#     vowels = ['i','a','o','u','e','I','A','O','U','E']
#     count = 0
#     for j in x:
#         if j in vowels:
#             count +=1
#     print('Number of vowels: ',count)
# x = input('Enter a string: ')
# stringVowels(x)
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