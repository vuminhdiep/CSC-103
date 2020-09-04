def menu():
    print('1: New account \n2: Operations \n3: Exit')
    return int(input("Your selection: "))

x = menu() #Assign a variable to call x later
customer = ''
created_accounts = []
account_number_lists = [i for i in range(100)] #Create an account number list so that each new user have different account number

def new_account():
    res = {
        "Name": '',
        "Address": '',
        "Phone": '',
        "Balance":  0,
        "Password": '',
        "Account number": 0,
        'Status': 'Opened'
    }
    res['Name'] = input('Your \nName: ')
    res['Address'] = input('Address: ')
    res['Phone'] = input('Phone: ')
    res['Balance'] = int(input('Amount: '))
    res['Password'] = input('Password: ')
    retype = input('Retype password: ')
    while retype != res['Password']:
        retype = input("Password doesn't match, type again: ")
    import random
    res["Account number"] = random.choice(account_number_lists)
    account_number_lists.remove(res["Account number"])         #remove already existed account number
    created_accounts.append(res)                               #add new account number to the list
    print('Your account has been succesfully created as: ')
    for k in res:
        if k != 'Status':
            print(k, ':',  res[k])
    print('Do not forget your account number and password')
    return res

def menu_op():
    print('1: Change password\n2: Deposit\n3: Withdraw\n4: Print\n5: Exit')
def deposit():
    amount = int(input('Amount: '))
    customer['Balance'] += amount
    print('Operation successful')
    return customer['Balance']

def withdraw():
    amount = int(input('Withdraw: '))
    customer['Balance'] -= amount
    print('Operation successful')
    return customer['Balance']
def operations():
    menu_op()
    choice = int(input('Your choice: '))
    while choice != 5:
        if choice == 1:
            customer['Password'] = input('New password: ')
            pw = input('Retype new password: ')
            while pw != customer['Password']:
                pw = input('They dont match, retype again: ')
            print('Your password has been updated')
            menu_op()
            choice = int(input('Your choice: '))
        if choice == 2:
            deposit()
            menu_op()
            choice = int(input('Your choice: '))
        if choice == 3:
            withdraw()
            choice = int(input('Your choice: '))
        if choice == 4:
            for k in customer:
                if k != 'Status':
                    print(k, ':',  customer[k])       
            menu_op()
            choice = int(input('Your choice: '))
    print('Goodbye')

    
while x != 3:
    if x == 1:
        customer = new_account()
        i = input("Press -1 for main menu 2 for operations: ")
        while i != '-1':
            if i == '2':
                i = "-1"            
                operations()
            else:
                i = input("Invalid, retype again")
        x = menu()    
    elif x == 2:
        a = int(input('Enter your account number: '))
        
        get = False
        while get == False:
            for i in range(len(created_accounts)):
                if a == created_accounts[i]['Account number']:
                    customer = created_accounts[i]
                    get = True
            if get == False:
                a = int(input('Account not exist. Please re-enter your account number: '))
        if customer['Status'] == 'Blocked':
            print('Your account has been blocked')
            x = menu()
        else:     
            b = input('Enter your password: ')
            count = 0
            while b != customer['Password']:
                count += 1
                b = input('Retype again: ')
                if count >= 3:
                    print('Your account has been blocked! Call the bank immediately!')
                    customer['Status'] = 'Blocked'
                    break
            if customer['Status'] == 'Blocked':
                x = menu()
            else:
                operations()
                x = menu()
    else:
        print("Type in a valid number")
        x = menu()
if x == 3:
    print('Operations done')
 


