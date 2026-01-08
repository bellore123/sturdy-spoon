balance = int(input("Enter current balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw % 100 != 0:
    print("Withdrawal amount must be a multiple of 100")
elif withdraw > balance:
    print("Insufficient balance")
else:
    balance -= withdraw
    print("Withdrawal successful")
    print("Updated balance:", balance)