
#Danny: def menu(), def new_account()
#John: def menu_op(), def deposit(), def withdraw()
#Emma def operations(), execution part
#Option B: Use dictionaries
#“We affirm that we have carried out my academic endeavors with full academic honesty." [Signed, Danny, Emma, John]

#Define menu function to print main menu and call when needed
def menu():
    print('Welcome to our bank\n1: New account \n2: Operations \n3: Exit')
    return int(input("Your selection: "))

x = menu() #Assign to a variable to call x later
customer = ''    #Assign a variable to each customer's dict of info
created_accounts = []    #An empty list to store accounts that have been created
account_number_lists = [i for i in range(1,101)]
#Create an account number list so that each new user have different account number

#Create an empty dict to store customers' input
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
    account_number_lists.remove(res["Account number"])
    #remove already existed account number
    created_accounts.append(res)        #add new account number to the list
    print('Your account has been succesfully created as: ')
    for k in res:
        if k != 'Status':
            print(k, ':',  res[k])
    print('Do not forget your account number and password')
    return res

#Define menu operations to print operations
def menu_op():
    print('Select operations from the menu\n1: Change password\n2: Deposit\n3: Withdraw\n4: Print\n5: Exit')
    
#Function to calculate balance after deposit
def deposit():
    amount = int(input('Amount: '))
    customer['Balance'] += amount
    print('Operation successful')
    return customer['Balance']

#Function to calculate balance after withdraw
def withdraw():
    amount = int(input('Withdraw: '))
    while amount > customer['Balance']:
        amount = int(input('The balance is not enough to proceed. Type again: '))

        if amount <= customer['Balance']:
            customer['Balance'] -= amount
            print('Operation successful')
            return customer['Balance']
        


#Function to run different operations when customer input info 
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
            menu_op()
            choice = int(input('Your choice: '))
        if choice == 4:
            for k in customer:
                if k != 'Status':
                    print(k, ':',  customer[k])       
            menu_op()
            choice = int(input('Your choice: '))
    print('Goodbye!')

#EXECUTION PART!!!  
while x != 3:
    if x == 1:
        customer = new_account()
        i = input("Press -1 for main menu 2 for operations: ")
        while i != '-1':
            if i == '2':
                i = "-1"     #Assign different value to i so that it can exit while loop and operations().          
                operations()
            else:
                i = input("Invalid, retype again")
        x = menu()    
    elif x == 2:
        a = int(input('Enter your account number or type -1 to exit: '))
        if a == -1:
            x = menu()
        else: 
            get = False  #Assign a condition for a while loop to run
            while get == False:
                for i in range(len(created_accounts)): #Run i to all items index in created_accounts
                    if a == created_accounts[i]['Account number']:
#get value from key 'Account number' from item i (which is also a dict) in list created_account    
                        customer = created_accounts[i] #Assign item i (which is also a dict) in list created_account
                        get = True     #Change condition to exit while loop
                if get == False:
                    a = int(input('Account not exist. Re-enter your account number or type -1 to exit: '))
                    if a == -1:
                        x = menu()
                        break          #Exit while loop
                        
            if customer['Status'] == 'Blocked':
                print('Your account has been blocked')
                x = menu()
            else:        
                b = input('Enter your password: ')
                count = 0
                while b != customer['Password']:
                    count += 1
                    b = input('Retype again: ')
                    if count >= 2:
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
    print('Operations done!')
 


