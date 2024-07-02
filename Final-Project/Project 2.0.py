name = "Bruno"
menu = f"""
                       
=======================Access Menu=======================
            
Hello {name} ! We are glad to have you here again !
What do you want to do today ?                       
                    
    [1] Withdraw 
    [2] Deposit 
    [3] Extract
    [4] Balance
    [0] Sair 

========================================================= 

Choose an option: """
balance = float(1000)
limit = 500
extract = f"""

========== Extract ==========

{name}, here is your extract ! 

"""
number_of_withdrawals = 0
WITHDRAW_LIMIT_TIMES = 3
number_of_deposits = 0




while True:

    option = int(input(menu))
                       

    if option == 1:
            withdraw = float(input("Type your withdraw value: "))

            exceeded_balance = withdraw > balance
            exceeded_limit = withdraw > limit
            exceeded_withdrawals = number_of_withdrawals >= WITHDRAW_LIMIT_TIMES




            if withdraw > 0 and not exceeded_balance and not exceeded_limit and not exceeded_withdrawals:
                print("Withdrawing...")
                print("Withdraw successfuly done !")
                balance -=  withdraw
                number_of_withdrawals += 1
                extract += f"Withdraw: R$ {withdraw:.2f}\n"
                print("Your new Balance is R$", balance) 
                print("You want to performe another acction?")
            elif exceeded_balance:
                print("Invalid balance limit. You have R$", balance, "in your account.")
            elif exceeded_withdrawals:
                print("Number of daily withdraw limit reached. Just 3 per day")
            elif exceeded_limit:
                print("Withdraw limit value reached. Just R$ 500 per withdraw")
            else:
                print("Invalid withdraw value")

    elif option == 2:
        print("Ok, let's make your deposit")
        deposit = float(input("Type your deposit value: "))
        if deposit > 0:
            balance += deposit
            number_of_deposits += 1
            extract += f"Deposit: R$ {deposit:.2f}\n"
            print("Your new Balance is R$", balance)
            print("You want to performe another acction?")
        else:
            print("Invalid deposit")
        

    elif option == 3:
        print("No movimentations done !" if (number_of_deposits or number_of_withdrawals) == 0 else extract)

    elif option == 4:
        print("Ok, here is your balance: R$", balance)
        print("You want to performe another acction?")

    elif option == 0:
        print(f"Thank you for the preference {name}. Enjoy your day and until the next time !")
        break
       
    else:
        print("Invalid option. Try again !")