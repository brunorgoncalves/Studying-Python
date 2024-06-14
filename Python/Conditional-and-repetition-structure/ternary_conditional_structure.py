balance = 1000
withdraw = 1500

status = "Success" if balance >= withdraw else "Fault"

print (f"{status} to withdraw")