#2619038_Diep_Vu
# “I affirm that I have carried out my academic endeavors with full academic honesty."[Signed, Diep Vu]

# # #2
grades = []
names = []
# #3
gr = int(input('Grade: '))
while gr >= 0:
    name = input('Name: ')
    grades.append(gr)
    names.append(name)
    gr = int(input('Grade: '))    
print('Grades: ',grades)
print('Names: ',names)
# # #4
small = min(grades)
large = max(grades)
total = sum(grades)
averageGradeF = total/len(grades)
averageGradeI = total//len(grades)
print('Average floating point is ',averageGradeF)
print('Average integer is ',averageGradeI)
print('Minimum value is', small)
print('Maximum value is', large)
print('Sum is', total)

# # #5
max_value = grades[0]
for n in grades:
    if n > max_value:
        max_value = n
print('Maximum value is', n)
min_value = grades[0]
for i in grades:
    if min_value > i:
        min_value = i
print('Minimum value is', min_value)
sum_value = 0
for i in range(0,len(grades)):
    sum_value = sum_value + grades[i]
print('Sum is', sum_value)
sum_val = 0
for n in range(0,len(grades)):
    sum_val = sum_val + grades[n]
averageGradeF = sum_val/len(grades)
averageGradeI = sum_val//len(grades)
print('Average floating point is ',averageGradeF)
print('Average integer is ',averageGradeI)
# # #6
nm = input('Name: ')
gr = grades[names.index(nm)]
print('Grade: ',gr)
# # #7
avg = sum(grades)//len(grades)
print('Average integer is', avg)
above = 0
below = 0
at = 0

for i in grades:
    if i < avg:
        below+=1
    elif i > avg:
        above+=1
    else:
        at+=1
print('Number of grades below average is', below)
print('Number of grades above average is', above)
print('Number of grades equal to average is', at)
# # #8
nc = 0
while nc < 2:
    gr = int(input('Grade: '))
    nm = input('Name: ')
    grades.append(gr)
    names.append(nm)
    nc+=1
print('New grades: ',grades)
print('New names: ',names)
# # #Repeat ques 4 5 6 7
# # #8.4
minimum = min(grades)
maximum = max(grades)
sumgr = sum(grades)
averageGradeF = sumgr/len(grades)
averageGradeI = sumgr//len(grades)
print('Minimum value is ',minimum)
print('Maximum value is ',maximum)
print('Sum is', sumgr)
print('Average floating point is ',averageGradeF)
print('Average integer is ',averageGradeI)
# # #8.5
ming = grades[0]
for g in grades:
    if g < ming:
        ming = g
print('Min grade is ',ming)
maxgr = 0
for i in range(0,len(grades)):
    if grades[i] > maxgr:
        maxgr = grades[i]
print('Max grade is ',maxgr)
sumgr = 0
for i in range(0,len(grades)):
    sumgr += grades[i]
print('Sum is ',sumgr)
averageGradeF = sumgr/len(grades)
averageGradeI = sumgr//len(grades)
print('Average floating point is ',averageGradeF)
print('Average integer is ',averageGradeI)
# # #8.6
nm = input('Name: ')
gr = grades[names.index(nm)]
print('Grade: ',gr)
# # #8.7
avg = sum(grades)//len(grades)
print('Average integer is ',avg)
above = 0
below = 0
at = 0
for i in grades:
    if i < avg:
        below+=1
    elif i > avg:
        above+=1
    else:
        at+=1
print('Number of grades below average is ',below)
print('Number of grades above average is ',above)
print('Number of grades equal to average is ',at)
# #9
from collections import namedtuple
employee = namedtuple('employee',['name','SSN','department','dateofbirth'])
# #10
emp1 = employee('A',123456,'CSC','3/12/1976')
emp2 = employee('B',789012,'ECO','5/23/1982')
print('Employee 1: ',emp1)
print('Employee 2: ',emp2)
# #11: Cant change attributes of tuple
# #12
setgrades = set(grades)
print('Set grade: ',setgrades)
# #Add existing item to the set
for i in range(0,len(grades)):
    setgrades.add(grades[i])
# #Add new item to the set
new = int(input('Add new grades: '))
setgrades.add(new)
print('Set grade: ',setgrades)
# #13
avg = sum(grades)//len(grades)
print(avg)
removeEl = []
for v in setgrades:
    if v < avg:
        removeEl.append(v)
print('Remove: ',removeEl)
for i in removeEl:
    setgrades.remove(i)
print('Set grade: ',setgrades)
#14
set1 = set([1, 2, 3, 4, 5])
set2 = set([1, 2, 88, 45, 3])
set3 = set.union(set1, set2)
print('Union set: ',set3)

set4 = set.intersection(set1, set2)
print('Intersection set: ',set4)

set5 = set1.difference(set2)
print('Difference set1: ',set5)

set6 = set2.difference(set1)
print('Difference set2: ',set6)

set8 = set1.symmetric_difference(set2)
print('Symmetric difference: ',set8)

#15
set1 = set([1, 2, 3, 4, 5])
set2 = set([1, 2, 88, 45, 3])
#Intersection
for i in set1:
    for v in set2:
        if i == v:
            print(i,end=' ')
print()
#Union
print(*set1, end = ' ')
for i in set2:
    if i not in set1:
        print(i, end = ' ')
print()
# Difference
res = []
for i in set2:
    if i not in set1:
        print(i, end = ' ')
        res.append(i)
print()
for i in set1:
    if i not in set2:
        print(i, end = ' ')
        res.append(i)
print()
# Symmetric difference
print(*res, sep = ' ')
#16
namedgrades = {}
#17
gr = int(input('Grade: '))
while gr >= 0:
    name = input('Name: ')
    namedgrades[gr] = name
    gr = int(input('Grade: '))    
print('Named grade: ',namedgrades)
#18
minVal = 10**10
sumVal = 0
maxVal = 0
for i in namedgrades.keys():
    sumVal += i
    if i < minVal:
        minVal = i
    if i > maxVal:
        maxVal = i
print('Min grade: ',minVal)
print('Student with min grade: ',namedgrades[minVal])
print('Max grade: ',maxVal)
print('Student with max grade: ',namedgrades[maxVal])
print('Sum grade: ',sumVal)
avgValF = sumVal/len(namedgrades)
avgValI = sumVal//len(namedgrades)
print('Average floating point: ',avgValF)
print('Average integer: ',avgValI)
# #19
nm = input('Name: ')
a = [grade for grade, name in namedgrades.items() if name == nm]
print('Grade: ',a)
# #20
at = 0
above = 0
below = 0
avg = sumVal // len(namedgrades)
print('Average integer: ',avg)
for i in namedgrades.keys():
    if i < avg:
        below+=1
    elif i > avg:
        above += 1
    else:
        at +=1
print('Grades below average: ',below)
print('Grades above average: ',above)
print('Grades equal to average: ',at)
#21
nc = 0
while nc < 2:
    gr = int(input('Grade: '))
    nm = input('Name: ')
    namedgrades[gr] = nm
    nc +=1
print('New grades: ',namedgrades)
#Repeat 18 19 20
#21.18
minVal = 10**10
sumVal = 0
maxVal = 0
for i in namedgrades.keys():
    sumVal += i
    if i < minVal:
        minVal = i
    if i > maxVal:
        maxVal = i
print('Min: ',minVal)
print('Name with min grade: ',namedgrades[minVal])
print('Max: ',maxVal)
print('Name with max grade: ',namedgrades[maxVal])
print('Sum: ',sumVal)
avgValF = sumVal/len(namedgrades)
avgValI = sumVal//len(namedgrades)
print('Average floating point: ',avgValF)
print('Average integer: ',avgValI)
#21.19
nm = input('Name: ')
a = [grade for grade, name in namedgrades.items() if name == nm]
print('Grade: ',a)
#21.20
at = 0
above = 0
below = 0
avg = sumVal // len(namedgrades)
print('Average integer: ',avg)
for i in namedgrades.keys():
    if i < avg:
        below+=1
    elif i > avg:
        above += 1
    else:
        at +=1
print('Grades below: ',below)
print('Grades above: ',above)
print('Grades equal: ',at)
