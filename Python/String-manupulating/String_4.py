name = "Bruno"

print(f"""
           Hello, my name is {name},
    I'm studying python to be a developer
        And on this mudule we are learning about strings !    
      """)

# or, I can declarate the message variable

message = f"""
           Hello, my name is {name},
    I'm studying python to be a developer
        And on this mudule we are learning about strings !    
      """

# and then, call it with print (message)

print(message)

print(f'''
      
================== Menu ==================
      
    1 - Depositar
    2 - Sacar
    0 - Sair

==========================================
      
      Obrigado por usar nosso sistema !!!
      ''')
print(int(input("Escolha o menu a ser aberto: ")))