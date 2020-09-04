i = int(input('What is your number? '))
k = 0
if i<0:
    i=-i

else:
    print(k,'to',i)
    while k<=i:
        print(k)
        k=k+1

print()

i=1
n=int(input('Up to what: '))
sum = 0
while i<=n:
    sum = sum+i
    i=i+1
    
print('Sum =',sum)
print('average =',sum/n)
i=0
#i is the amount of n numbers
sum=0
n=int(input('Next number: '))
while n>0:
    sum = sum+n
    i=i+1
    n=int(input('Next number: '))
print('Sum =',sum)
print('Average =',sum/i)
    
