def menu():
    print('1: New account \n2: Operations \n3: Exit') 
    x = int(input('Your selection: '))
    if x == 1:
        customer = new_account()
        menu()
    if x == 2:
        operations()
        menu()
    if x == 3:
        print('dfjlkdjlf')
 
 
def new_account():
    res = {
        "Name": '',
        "Address": '',
        "Phone": '',
        "Initial amount": 0,
        "Password": '',
        "Account number": ''
    }
    res['Name'] = input('Your \nName: ')
    res['Address'] = input('Address: ')
    res['Phone'] = input('Phone: ')
    res['Initial amount'] = int(input('Inital amount: '))
    res['Password'] = input('Password: ')
    retype = input('Retype password: ')
    while retype != res['Password']:
        retype = input("Password doesn't match, type again: ")
    import random
    res["Account number"] = random.randint(1,100)
    print('Your account has been succesfully created as: ')
    for k in res:
        print(k, ':',  res[k])
    print('Do not forget your account number and password')
    i = input("Press -1 for main menu 2 for operations: ")
    while i != '-1':
        i = input("You f**king dumbass! PRESS THE F**CKING -1!!!! ")
    return res

sel2 = int(input('Press -1 for main menu and 2 for operations '))
if sel2 == -1:
    menu()

def operations():
    print('Select your operations from the menu')
    print('1: Change password\n2: Deposit\n3: Withdraw\n4: Print\n5: Exit')
    choice = int(input('Your choice: '))
    if choice == 1:
        pw3 = input('New password: ')
        pw4 = input('Retype new password: ')
        while pw4 != pw3:
            pw4 = input('They dont match, retype again: ')
        print('Your password has been updated')
    if choice == 2:
        deposit(account, amount)
    if choice == 3:
        withdraw(account, amount)

#Deposit
def deposit(account, amount):
    
account = res['Initial amount']
#Withdraw
def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']
 



  




   