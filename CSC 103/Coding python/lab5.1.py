###Right triangle backwards up
##r = 5
##for i in range(1,1+r):
##    for j in range(1,1+r-i):
##        print(' ',end='')
##    for j in range(1, 1+i):
##        print('*',end='')
##    print()
##print()
##print()
###XOXO
##r=8
##for i in range(1,1+r):
##    for j in range(1, 1+r//2):
##        if i%2==1:
##            print('XO',end='')
##        else:
##            print('OX',end='')
##    print()
###Rectangle *
##r = 5
##for i in range(1, 1+r):
##    for j in range(1, 1+r):
##        print('*',end='')
##    print()
#Picture frame
r = 5
for i in range(1, 1+r):
   for j in range(1, 1+r):
       if i==1 or i==r or j==1 or j==r:
           print('*',end='')
       else:
           print(' ',end='')
   print()
#Right triangle
##r = 5
##for i in range(1,1+r):
##    for j in range(1,i+1):
##        print('*',end='')
##    print()
##r = 5
##for i in range(1,1+r):
##    for j in range(1,2+r-i):
##        print('*',end='')
##    print()
#Right triangle backwards down
##r = 5
##for i in range(1,1+r):
##    for j in range(1, i):
##        print(' ',end='')
##    for j in range(1,2+r-i):
##        print('*',end='')
##    print()
#Triangle with spaces between each lines
##r=5
##for i in range(1,1+r):
##    for j in range(1,1+r):
##        if i%2==1:
##            print('*',end='')
##        else:
##            print(' ',end='')
##    print()
#Print digits of a number in order high to low
##x = int(input('Enter a number: '))
##y = len(str(x))
##z = 10**(y-1)
##i = 0
##while i<y:
##    a = x//z
##    print(a)
##    b = x%z
##    x = b
##    z = z//10
##    i = i+1
# start = int(input('Start: '))
# end = int(input('End: '))
# num_prime = 0
# for n in range(start,end+1):
#     count = 0
#     for div in range(2,1+(n//2)):
#         if n%div==0:
#             count+=1
#     if count==0:
#         print(n,end=" ")
#         num_prime+=1
#         if num_prime%10==0:
#             print()
#Print isoceles triangle with base
# base = int(input('Base: '))
# n = base
# for i in range(1,(n+1)//2 + 1):
#     for j in range(0,(n+1)//2 - i+1):
#         print(' ',end='')
#     for k in range(1,i*2):
#         print('*',end='')
#     print()
# diagonal = int(input('Diagonal: '))
# n = diagonal
# for i in range(1,(n+1)//2 + 1):
#     for j in range(0,(n+1)//2 - i+1):
#         print(' ',end='')
#     for k in range(1,i*2):
#         print('*',end='')
#     print()
# for x in range((n+1)//2+1,n+1):
#     for y in range(x-(n+1)//2+1,0,-1):
#         print(' ',end='')
#     for z in range((n+1-x)*2-1,0,-1):
#         print('*',end='')
#     print()
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

