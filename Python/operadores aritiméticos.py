print ("Basic math operators")

product_1 = 20
product_2 = 10

print(product_1 + product_2)
print(product_1 + product_2 + 3.5)
print(product_1 - product_2)
print(product_1 / product_2)
print(product_1 // product_2)
print(product_1 * product_2)
print(product_1 % product_2)
print(product_1 ** product_2)

x = (10 + 5) * 4

print (x)

print ("-------------------------------------")
print ("Comparing operators. Checking equalities and differences between values")

balance = 1000
withdraw = 500

print(balance == withdraw)
print(balance != withdraw)
print(balance > withdraw)
print(balance >= withdraw)
print(balance < withdraw)
print(balance <= withdraw)

print ("-------------------------------------")
print ("Assignment operators. Adding values to variables from a mathematical operation")

balance += 200

print(balance)

withdraw -= 70

print (withdraw)

balance *= 2
print (balance)

balance //= 4
print(balance)

balance %= 11
print(balance)

balance **= 3
print(balance)

print ("-------------------------------------")
print ("Logical operators")

withdraw = 250
balance = 1000
limit = 200
accounts = []
special_account = True

print (withdraw >= balance and withdraw <= limit)
print (withdraw <= balance and withdraw >= limit)

print (withdraw <= balance or withdraw <= limit)
print (withdraw >= balance or withdraw <= limit)

print (not balance < withdraw)
print (not withdraw < balance)

print (not accounts)

print (not "bruno")
print (not "")

print ("-------------------------------------")
print ("An account real situation")

expression_1 = ((balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw))
print (expression_1)

withdraw = 250
balance = 1000
limit = 200
accounts = []
special_account = False

expression_2 = ((balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw))
print (expression_2)


normal_account_with_suficient_balance = (balance >= withdraw and withdraw <= limit) 
special_account_with_suficient_balance = (special_account and balance >= withdraw)

expression_3 = normal_account_with_suficient_balance or special_account_with_suficient_balance
print (expression_3)
