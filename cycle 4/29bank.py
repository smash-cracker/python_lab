class BankAccount:
    def __init__(self,accNo, name, type, balance):
        self.accNo = accNo
        self.name = name
        self.type = type
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Rs ",amount, " debited from ", self.type , " account ", self.accNo)
        print("Balance : ",self.balance)
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Rs ",amount, " credited to ", self.type , " account ", self.accNo)
            print("Balance : ",self.balance)
        else:
            print("Insufficent balance!")

c1 = BankAccount(14145, "denny", "savings", 5000)
c1.deposit(2500)
c1.withdraw(500)