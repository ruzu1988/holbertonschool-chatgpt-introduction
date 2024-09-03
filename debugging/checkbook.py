class Checkbook:
    def __init__(self):
        self.balance = 0.0
        print("Welcome to the Checkbook App!")
        self.get_balance()   #  Muestra el saldo inicial

    def deposit(self, amount):
        if amount <= 0:
            print("Amount to deposit should be positive.")
        return
    self.blance += amount
    print("Deposit ${:.2f}".format(amount))
    self.get_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount to withdraw should be positive.")
            return
        if amount > self.balnce:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(amount))
            self.get_balance()

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ")
        if action == 'exit':
            print("Exiting the Check App. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number")
            elif action == 'withdraw':
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                elif action == 'balance':
                    cb.get_balance()
                else:
                    print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
