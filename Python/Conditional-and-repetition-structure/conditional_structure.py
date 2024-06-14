LEGAL_AGE = 18
SPECIAL_AGE = 17

idade = int(input ("Enter your age: "))

if idade >= LEGAL_AGE:
    print("Alright, let's proceed with your driver's license registration !")

elif idade == SPECIAL_AGE: 
    print("For students aged 17, we can just release the theoretical classes")

else:
    print("Sorry, we can just register legal age people. Try again we you are 18")

