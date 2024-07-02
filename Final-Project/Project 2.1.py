name = input("Which is your name ? ")

import textwrap 

def menu():
    menu = f"""
    =======================Access Menu=======================        
    

    Hello {name} ! We are glad to have you here again !
    What do you want to do today ?                       
                    
    [1] Withdraw 
    [2] Deposit 
    [3] Extract
    [4] Balance
    [5] New User
    [6] New Account
    [7] List Accounts
    [0] Exit 
    ========================================================= 
    Choose an option: """
    return input(textwrap.dedent(menu))

def main():

    AGENCY = "0001"
    WITHDRAW_LIMIT_TIMES = 3
    balance = float(1000)
    withdraw_limit = 500
    number_of_withdrawals = 0
    extract = ""
    registered_users = []
    registered_accounts = []

    while True:
        
        option = menu()

        if option == "1":
            value = float(input("Type your withdraw value: "))

            balance, extract = withdraw(
                balance=balance,
                value=value,
                extract=extract,
                withdraw_limit=withdraw_limit,
                number_of_withdrawals=number_of_withdrawals,
                withdraw_limit_times=WITHDRAW_LIMIT_TIMES,
                )


        elif option == "2":
            print("Ok, let's make your deposit")
            value = float(input("Type your deposit value: "))

            balance, extract, = deposit(balance, value, extract)
                

        elif option == "3":

            balance, extract = show_extract(balance, extract=extract)

        elif option == "4":
            print("Ok, here is your balance: R$", balance)
            print("You want to performe another acction?")
        
        elif option == "5":
            register_user(registered_users)

        elif option == "6":
            account_number = len(registered_accounts) + 1
            account = register_account(AGENCY, account_number, registered_users)

            if account:
                registered_accounts.append(account)

        elif option == "7":
            list_accounts(registered_accounts)
        

        elif option == "0":
            print(f"Thank you for the preference {name}. Enjoy your day and until the next time !")
            break
       
        else:
           print("Invalid option. Try again !")

def withdraw(*, balance, value, extract, withdraw_limit, number_of_withdrawals, withdraw_limit_times):

    exceeded_balance = value > balance
    exceeded_limit = value > withdraw_limit
    exceeded_withdrawals = number_of_withdrawals >= withdraw_limit_times

    if exceeded_balance:
        print("Invalid balance limit. You have R$", balance, "in your account.") 

    elif exceeded_limit:
        print("Withdraw limit value reached. Just R$ 500 per withdraw")

    elif exceeded_withdrawals:                                                                    #NÃO FUNCIONANDO, FALTA ARRUMAR
        print("Number of daily withdraw limit reached. Just 3 per day")

    elif value > 0:
        print(number_of_withdrawals)
        number_of_withdrawals += 1
        print("Withdrawing...")
        print("Withdraw successfuly done !")
        print(number_of_withdrawals)
        balance -=  value
        extract += f"Withdraw: R$ {value:.2f}\n"
        print("Your new Balance is R$", balance) 
        print("You want to performe another acction?")
        
    else:
        print("Invalid withdraw value")

    return balance, extract

def deposit(balance, value, extract, /):
    if value > 0:
        number_of_deposits = 0
        balance += value
        number_of_deposits += 1
        extract += f"Deposit: R$ {value:.2f}\n"
        print("Your new Balance is R$", balance)
        print("You want to performe another acction?")
    else:
        print("Invalid deposit")

    return balance, extract
    
def show_extract(balance, /, *, extract):
    print(f"""

    ========== Extract ==========

    {name}, here is your extract ! 

    """)
    print("No movimentations done !" if not extract else extract)

    return balance, extract
    
def register_user(registered_users):
    cpf = input("Type your CPF (only numbers): ")
    user = user_filter(cpf, registered_users)

    
    if user:
        print("\nAlready exist a user with this CPF")
        return
    
    
    name = input("Type your name: ")
    birthday = input("Type your date of birth (dd-mm-yy): ")
    adress = input("Type your adress (Logradouro, nº - Bairro - Cidade/Sigla do Estado ): ")

    return {"Name": name, "CPF": cpf, "Birthday": birthday, "Adress": adress}
    print("\n==== User successfuly registered ====")
    print(registered_users)

def user_filter(cpf, registered_users):
    filtered_users = [user for user in registered_users if user ["CPF"] == cpf]
    return filtered_users [0] if filtered_users else None

def register_account(agency, account_number, registered_users):
    cpf = input("Type your CPF (only numbers): ")
    user = user_filter(cpf, registered_users)

    if user:
        print ("\n==== Account successfuly created ====")
        return {"agency": agency, "account": account_number, "user": registered_users}
        
    
    print("User not found. If you are a new user, go to option [5] first. Account creation stopped !")

def list_accounts(registered_accounts):
    for account in registered_accounts:
        line = f"""
              Agency: {account["agency"]}
             Account: {account["account"]}

               Owner: {account["user"][0]["Name"]}
                 CPF: {account["user"][0]["CPF"]}
            Birthday: {account["user"][0]["Birthday"]}
              Adress: {account["user"][0]["Adress"]}    
        """
        print("=" * 100)
        print(textwrap.dedent(line))
    

          


main()









                       




