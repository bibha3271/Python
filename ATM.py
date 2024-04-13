class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def authenticate(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

class Withdraw(Transaction):
    def __init__(self, amount):
        super().__init__('Withdraw', amount)

class Deposit(Transaction):
    def __init__(self, amount):
        super().__init__('Deposit', amount)

class Transfer(Transaction):
    def __init__(self, amount, recipient):
        super().__init__('Transfer', amount)
        self.recipient = recipient

class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users:
            return self.users[user_id].authenticate(user_id, pin)
        return False

    def withdraw(self, user_id, amount):
        if user_id in self.users and self.users[user_id].balance >= amount:
            self.users[user_id].balance -= amount
            self.users[user_id].add_transaction(Withdraw(amount))
            return True
        return False

    def deposit(self, user_id, amount):
        if user_id in self.users:
            self.users[user_id].balance += amount
            self.users[user_id].add_transaction(Deposit(amount))
            return True
        return False

    def transfer(self, sender_id, recipient_id, amount):
        if sender_id in self.users and recipient_id in self.users and self.users[sender_id].balance >= amount:
            self.users[sender_id].balance -= amount
            self.users[recipient_id].balance += amount
            self.users[sender_id].add_transaction(Transfer(amount, recipient_id))
            self.users[recipient_id].add_transaction(Transfer(amount, sender_id))
            return True
        return False

    def get_transaction_history(self, user_id):
        if user_id in self.users:
            return self.users[user_id].transaction_history
        return []

def main():
    atm = ATM()
    # Create some users
    user1 = User("123456", "1234")
    user2 = User("654321", "4321")
    atm.add_user(user1)
    atm.add_user(user2)

    while True:
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")
        if atm.authenticate_user(user_id, pin):
            print("Authentication successful!")
            break
        else:
            print("Authentication failed. Please try again.")

    while True:
        print("\nOptions:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Transactions History")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to withdraw: "))
            if atm.withdraw(user_id, amount):
                print("Withdrawal successful!")
            else:
                print("Withdrawal failed. Insufficient balance.")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if atm.deposit(user_id, amount):
                print("Deposit successful!")
            else:
                print("Deposit failed.")

        elif choice == "3":
            recipient_id = input("Enter recipient's user ID: ")
            amount = float(input("Enter amount to transfer: "))
            if atm.transfer(user_id, recipient_id, amount):
                print("Transfer successful!")
            else:
                print("Transfer failed. Insufficient balance or invalid recipient.")

        elif choice == "4":
            transactions = atm.get_transaction_history(user_id)
            print("Transaction History:")
            for transaction in transactions:
                print(f"{transaction.type}: {transaction.amount}")

        elif choice == "5":
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
