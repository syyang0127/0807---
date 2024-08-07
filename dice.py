from random import randint
# random이라는 모듈에서 randint라는 기능만 쓴다는 의미.(메모리관리?)

class Dice:
    def __init__(self,x):
        self.x=x
#        self.y=y
#        self.__size = 30
#        self.__value = 1
        
    def getDiceValue(self):
        return self.__value
    
    def printDice(self):
        print('주사위의 값 = ', self.__value)
        
    def rollDice(self):
        self.__value = randint(1,6) # 1~6까지 정수 중에 1개 추출
        
dice1 = Dice(0)
dice1.rollDice()
dice1.printDice()
####################
####################