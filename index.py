account_balance = 100

def dashboard():
    print(
        """
    1. Withdraw
    2. Deposit
    3. Check Balance
    4. Exit
"""
    )

    option = input('option: ')
    if option == '1':
       withdraw()
    elif option == '2':
        pass
    elif option == '3':
        check_balance()
    elif option == '4':
        exit()  
    else:
        print('Invalid option, Try again!')
        dashboard() #having the same define inside the same define is called RECURSIVE FUNCTION

def withdraw():
    global account_balance

    amount = float(input('Amount: '))
    if amount > account_balance:
        print('Insufficient Fund')
    else:
        account_balance -= amount
        print(f'You,ve successfully withdraw #{amount},\n account balance is #{account_balance}') 

        option = input('press 1 to go back to dashboard or enter to retry: ')
        if option == '1':
            dashboard()
        else:
            withdraw()

def check_balance():
    print(f'Your account balance is {account_balance}')


dashboard()
           
