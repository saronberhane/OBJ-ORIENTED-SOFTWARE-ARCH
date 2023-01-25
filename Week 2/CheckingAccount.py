
# class for the checking account
class CheckingAccount:
    def __init__(self, name, address, acountNum, phoneNumber, email="none"):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.acountNum = acountNum
        self._balance = 0.0

    def credit(self, amount):
        self._balance += amount

    def debit(self, amount):
        if amount > self._balance:
            print("insufficient funds.")
        else:
            self._balance -= amount 

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        print("Withdraw Amount: ", amount)
        if amount <= self._balance:
            print("You have enough to Withdraw: ", amount)
            self._balance = self._balance - amount 
            print("Your new balance is: ", self._balance)

        else:
            print("You don't have enough to withdraw.")


# driver application
if __name__ == "__main__":
    account = CheckingAccount("Stacy Dan", "123 Here st", "9875432176", "8324562312", "Stacydan@gmail.com")
    account.credit(10000.01)
    account.withdraw(55.53)