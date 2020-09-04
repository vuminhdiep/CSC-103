#“I affirm that I have carried out my academic endeavors with full academic honesty."[Signed,Diep Vu]
#I saved all the data in a big list with 20 items corresponding to year 2000 to year 2019. Inside the list, each item is a dict with 12 months and 12 rainfall amounts of a year
#The data above is put into a rainfall table(which is a function I saved) so I didn't read from file outside
#I rounded up the result of average rainfall amounts to 2 digits after decimal point
#I also checked if the user input valid year. Else, they will have to input again
#When the user input month that is not case-sensitive(for example: jANuAry), I changed the input to all normal letters and the first letter is uppercase. Then I assemble those letter to the right format (for example: January)
import random
lst = []
dict_rain = {}
for i in range(20):
    
    data = {
    'January': random.randint(1,100),
    'February': random.randint(1,100),
    'March': random.randint(1,100),
    'April': random.randint(1,100),
    'May': random.randint(1,100),
    'June': random.randint(1,100),
    'July': random.randint(1,100),
    'August': random.randint(1,100),
    'September': random.randint(1,100),
    'October': random.randint(1,100),
    'November': random.randint(1,101),
    'December' : random.randint(1,100)
    }
    
    lst.append(data)
def print_table():
    print('{:<9}'.format('Year'), end= '')
    for k in lst[0].keys():
        print('{:<9}'.format(k),end='')
    print()
    for i in range(len(lst)):
        print('{:<9}'.format(i + 2000), end='')
        
        for j in lst[i].keys():
            
            print('{:<9}'.format(lst[i][j]), end = '')
        print()

def menu():

    print('1. Average rainfall for a given year')
    print('2. Average rainfall for a given month')
    print('3. Min. rainfall for a given year')
    print('4. Min. rainfall for a given month')
    print('5. Max. rainfall for a given year')
    print('6. Max. rainfall for a given month')
    print('7. Exit')
    
    return int(input('Your choice: '))
    
def ops():
    x = menu()
    while x!= 7:
        if x == 1:
            year = int(input('What year: '))
            while year < 2000 or year > 2019:
                year = int(input('Invalid year. Type again: '))
    
            for i in range(20):
                if year % 100 == i:
                    rainfall_sum_year = 0
                    avg_year = 0
                    for j in lst[i].keys():
                        rainfall_sum_year += lst[i][j]
                    avg_year = round(rainfall_sum_year/12, 2)
        print_table()           
        print('Average rainfall for year',year,'is =',avg_year)
        x = menu()
        if x == 2:
            month = input('Which month: ')
            month = month.lower()
            month_letters = [i for i in month]
            month_letters[0] = month_letters[0].upper()
            month = ''
            for i in month_letters:
                month += i
            rainfall_sum_month = 0
            avg_month = 0
            for i in range(20):
                rainfall_sum_month += lst[i][month]
            avg_month = round(rainfall_sum_month/len(lst), 2)
            print_table()
            print('Average rainfall for month',month,'is =',avg_month)
            x = menu()
        if x == 3:
            year = int(input('What year: '))
            while year < 2000 or year > 2019:
                year = int(input('Invalid year. Type again: '))
            for i in range(20):
                if year % 100 == i:
                    min_rain_val = min(lst[i].values())
                    min_rain_key = min(lst[i], key=lst[i].get)
            print_table()
            print('Min. rainfall is in',min_rain_key,'and',min_rain_val,'units')
            x = menu()
        if x == 4:
            month = input('Which month: ')
            
            month = month.lower()
            month_letters = [i for i in month]
            month_letters[0] = month_letters[0].upper()
            month = ''
            for i in month_letters:
                month += i
            min_rain_month = 1e9
            k = 0
            for i in range(len(lst)):
                if lst[i][month] < min_rain_month:
                    min_rain_month = lst[i][month]
                    k = i + 2000
            print_table()
            print('Min. rainfall for month',month,'is in year',k,'and is =',min_rain_month)
            x = menu()


        if x == 5:
            
            year = int(input('What year: '))
            while year < 2000 or year > 2019:
                year = int(input('Invalid year. Type again: '))
            for i in range(20):
                if year % 100 == i:
                    max_rain_val = max(lst[i].values())
                    max_rain_key = max(lst[i], key=lst[i].get)
            print_table()
            print('Min. rainfall is in',max_rain_key,'and is =',max_rain_val,'units')
            x = menu()
        if x == 6:
            month = input('Which month: ')
            month = month.lower()
            month_letters = [i for i in month]
            month_letters[0] = month_letters[0].upper()
            month = ''
            for i in month_letters:
                month += i
            max_rain_month = 0
            m = 0
            for i in range(len(lst)):
                if lst[i][month] > max_rain_month:
                    max_rain_month = lst[i][month]
                    m = i + 2000
            print_table()
            print('Max. rainfall for month',month,'is in year',m,'and is =',max_rain_month)
            x = menu()

    if x == 7:
        print('Goodbye!')
#EXECUTION PART!!!
ops()
        

