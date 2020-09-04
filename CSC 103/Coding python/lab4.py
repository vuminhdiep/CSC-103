
#Question 9
k = 1
n = int(input('Enter number: '))
for i in range(100):
    if n > 10**i and n < 10**(i+1):
        k = i
        break
while k >=0:
    d = n//(10**k)
    print(d)
    n = n%(10**k)
    k -=1
#Question 8
n = int(input('Enter n: '))
while n > 0:
    d = n%10
    print(d)
    n = n//10





