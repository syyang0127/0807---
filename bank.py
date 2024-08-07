class BankAccnt:
    def __init__(self):
        self.name = "hong"
        self.__balance = 0
        
    def withdraw(self,amnt):
        self.__balance -= amnt
        print('통장에서',amnt,'원이 출금됐습니다.')
        return self.__balance

    def deposit(self,amnt):
        self.__balance += amnt
        print('통장으로',amnt,'원이 입금됐습니다.')
        return self.__balance

cus1 = BankAccnt()
cus1.deposit(100)
cus1.withdraw(50)

#print('현재 잔액은',self.__balance,'입니다')