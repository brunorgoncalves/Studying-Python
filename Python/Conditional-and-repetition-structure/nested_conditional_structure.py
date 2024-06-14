normal_account = True
universitary_account = False
balance = 1000
withdraw = 500
overdraft = 600

if normal_account:

    if balance >= withdraw:
        print("Withdraw successfuly done !")
    elif withdraw > balance and withdraw <= (balance + overdraft):
        print("Withdraw successfuly done, using part of your overdraft limit")
    else:
        print("Sorry, you don't have limit for this withdraw")

elif universitary_account:

    if balance >= withdraw:
        print("Withdraw successfuly done !")
    else:
        print("Sorry, you don't have limit for this withdraw")

else:
    print("Account not exist. Try a valid account")