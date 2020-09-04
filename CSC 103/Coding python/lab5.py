###Question 2
##r = 5
##for i in range(1,r+1):
##    for j in range(1,i+1):
##        print(i,end='')
##    print()
###Question 3.4
##r = 5
##for i in range(1,r+1):
##    for j in range(1,i+1):
##        print('*',end='')
##    print()
###Question 3.2
##r = 5
##for i in range(r+1,1,-1):
##    for j in range(i,1,-1):
##        print('*',end='')
##    print()
#Question 1
##n = int(input('n: '))
##my_str = ''
##while n > 0:
##    my_str = str(n%2) + my_str
##    n = n//2
##print(my_str)
#Question 3.3
##r = 5
##for i in range(1,r+1):
##    for j in range(1,r+1-i):
##        print(' ',end='')
##    for j in range(1,i+1):
##        print('*',end='')
##    print()
###Question 3.1
##r = 5
##for i in range(1,r+1):
##    for j in range(1,i):
##        print(' ',end='')
##    for j in range(1,2+r-i):
##        print('*',end='')
##    print()
####Question 4
##res = [
##    {
##        "Number": 0,
##        "Zero": "No",
##        "Positive": "No",
##        "Negative": "No",
##    },
##    {
##        "Number": 0,
##        "Zero": "No",
##        "Positive": "No",
##        "Negative": "No",
##    },
##    {
##        "Number": 0,
##        "Zero": "No",
##        "Positive": "No",
##        "Negative": "No",
##    },
##    {
##        "Number": 0,
##        "Zero": "No",
##        "Positive": "No",
##        "Negative": "No",
##    },
##    {
##        "Number": 0,
##        "Zero": "No",
##        "Positive": "No",
##        "Negative": "No",
##    },
##]
##for i in range(5):
##    n = int(input(str("Enter number " + str(i + 1) + ":")))
##    res[i]["Number"] = n
##    if n < 0:
##        res[i]["Negative"] = "Yes"
##    elif n == 0:
##        res[i]["Zero"] = "Yes"
##    else:
##        res[i]["Positive"] = "Yes"
## 
##print("Number Zero  Positive Negative")
##for i in range(5):
##    for j in res[i].values():
##        print(j, end = '\t')
##    print(end = '\n')
##    
#4

##Check a number is prime or not
# n = int(input('n: '))
# count = 0
# for div in range(2,1+n//2):
#    if n%div==0:
#        count+=1
# if count==0:
#    print(n)
# print()
#Print diamond
# n = 9
# for a1 in range(1, (n+1)//2 + 1):
#     for a2 in range((n+1)//2 - a1):
#         print(" ", end = "")
#     for a3 in range((a1*2)-1):
#         print("*", end = "")
#     print()

# for a1 in range((n+1)//2 + 1, n + 1):
#     for a2 in range(a1 - (n+1)//2):
#         print(" ", end = "")
#     for a3 in range((n+1 - a1)*2 - 1):
#         print("*", end = "")
#     print()
#Rectangle
width = int(input('Width: '))
height = int(input('Height: '))
w = width
h = height
for i in range(1,1+w):
    for j in range(1,1+h):
        if i == 1 or j == 1 or i == w or j == h:
            print('+-',end='')
        elif i%2==0:
            print(' ',end='')
    print()
#Question 7
num = int(input('Enter n: '))
n = num
result = 1
fact = 1
for j in range(1,n+1):
    fact = fact*j
for i in range(0,n+1):
   result = result + ((2**i)/fact)
print(result)





