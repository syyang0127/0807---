class BankAccnt:
    def __init__(self, balance, name, accnt):
        self.balance = balance
        self.name = name
        self.accnt = accnt
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
class CheckingAccnt(BankAccnt):
    def __init__(self, balance, name, accnt):
        super().__init__(balance, name, accnt)
        self.withdraw_charge = 10000
        
    def withdraw(self,amount):
        return BankAccnt.withdraw(self, amount+self.withdraw_charge)

class SavingAccnt(BankAccnt):
    def __init__(self, balance, name, accnt, interest_rate):
        super().__init__(balance, name, accnt)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        return BankAccnt.deposit(self, self.balance*self.interest_rate)
    
a1 = SavingAccnt('홍길동', 123456, 30000, 0.03)
a1.add_interest()
print('저축예금의 잔액 : ', a1.balance)

a2 = CheckingAccnt('김철수', 23456, 1000000)
a2.withdraw(100000)
print('예금 잔액 : ', a2.balance)
