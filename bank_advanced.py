class Bank:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def details(self):
        print("Your Details ==>", "Name:", self.name, ", Account Number:", self.account_number)

    def available_balance(self):
        print("Available Balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:  # Check for sufficient balance
            self.balance -= amount
            print("Amount Deducted:", amount)
            print("Final Balance:", self.balance)
        else:
            print("Insufficient Balance!")

    def deposit(self, amount):
        self.balance += amount
        print("Amount Added:", amount)
        print("Final Balance:", self.balance)


dict = {
    123: {"name": "sainadh", "balance": 500},
    234: {"name": "sridevi", "balance": 1000},
    345: {"name": "suma", "balance": 1500}
}

while True:
    account_number = int(input("Enter your account number: "))
    if account_number in dict:
        name = dict[account_number]["name"]
        balance = dict[account_number]["balance"]
        b = Bank(account_number, name, balance)

        while True:  # Inner loop for operations within an account
            print()
            print("Operations available ==>", "1.details", "2.check balance", " 3.deposit", "4.withdraw", "5.exit",
                  sep="\t")

            ch = int(input("Enter the operation number: "))

            if ch == 1:
                b.details()
            elif ch == 2:
                b.available_balance()
            elif ch == 3:
                amount_to_be_added = float(input("Enter amount to be added: "))
                b.deposit(amount_to_be_added)
                dict[account_number]["balance"] = b.balance
            elif ch == 4:
                amount_to_be_deducted = float(input("Enter amount to be withdrawn: "))
                b.withdraw(amount_to_be_deducted)
                dict[account_number]["balance"] = b.balance
            elif ch == 5:
                print("You have exited successfully...\n")
                break  # Exit the inner loop to handle a new account
            else:
                print("Please enter a valid operation number!.....\n")
    else:
        print("Invalid account number!......\n")
