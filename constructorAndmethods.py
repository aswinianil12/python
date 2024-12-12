class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance


    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
        else:
            self.balance += amount
            print(f"Deposited: (amount)")
            print(f"Updated Balance: {self.balance}")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount}")
            print(f"Updated Balance: {self.balance}")
    def display(self):
        print("\n Account Details:")
        print(f"Account Number: {self.acc_no}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.acc_type} ")
        print(f"Account Balance: {self.balance}")


acc_no = int(input("Enter account number:"))
name = input("Enter account holder name:")
acc_type = input("Enter account type (Saving/Current): ")
balance = int(input("Enter initial balance:"))

account = BankAccount(acc_no, name, acc_type, balance)

account.display()

deposit_amount = int(input("\n Enter the amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("\n Enter the amount to withdraw:"))
account.withdraw(withdraw_amount)

