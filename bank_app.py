class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: {self.balance}")

    def transfer(self, target_account, amount):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred {amount} to {target_account.account_holder}.")
        else:
            print("Transfer failed. Insufficient funds or invalid amount.")

def main():
    # Create two bank accounts
    account_1 = BankAccount("Raju", 1000.0)
    account_2 = BankAccount("Avinash", 500.0)

    while True:
        print("\nWelcome to the Banking Application")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            account_1.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account_1.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            account_1.withdraw(amount)
        elif choice == '4':
            amount = float(input("Enter amount to transfer: "))
            account_1.transfer(account_2, amount)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
