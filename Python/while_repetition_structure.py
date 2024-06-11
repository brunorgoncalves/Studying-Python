option = -1

while option != 0:
    option = int(input(" [1] Withdraw \n [2] Extract \n [3] Historic \n [0] Sair \n Choose an option: "))

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
    print("Thank you for the preference. Enjoy you day and until the next time !")