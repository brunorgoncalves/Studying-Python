option = -1
name = "Bruno"

while option != 0:

    option = int(input(f"""
                       
=======================Access Menu=======================
            
Hello {name} ! We are glad to have you here again !
What do you want to do today ?                       
                    
    [1] Withdraw 
    [2] Extract 
    [3] Historic 
    [0] Sair 

========================================================= 

Choose an option: """))

    if option == 1:
        print("Whitdrawing...")
        print("Withdraw successfuly done !")
        print("You want to performe another acction?")

    elif option == 2:
        print("Here is your extract")
        print("You want to performe another acction?")

    elif option == 3:
        print("Ok, here is your historic")
        print("You want to performe another acction?")

    elif option > 3 or option < 0:
        print("Invalid option. Try again !")
else:
    print(f"Thank you for the preference {name}. Enjoy your day and until the next time !")