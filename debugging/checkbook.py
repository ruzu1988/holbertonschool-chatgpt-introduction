class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        Parameters:
        amount (float): The amount to be deposited.
        """
    self.blance += amount
    print("Deposit ${:.2f}".format(amount))
    print("Current Balance ${:.2f}".format(self.balance))
    
    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.
        
        Parameters
        amount (float): The amount to be withdrawn.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawl.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance of the account.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            print("Exiting the Check App. Goodbye!")
            break
        elif action.lower == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Deposit amount must be non-negative")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric for the deposit amount.")
            elif action.lower() == 'withdraw':
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount < 0:
                        print("Withdrawal amount must be non-negative.")
                    else:
                        cb.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the withrawal amount.")
                elif action.lower() == 'balance':
                    cb.get_balance()
                else:
                    print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
