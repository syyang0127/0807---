class Car: #부모클래스
    def __init__(self, make, model, color, price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price
    
    def setMake(self,make):
        self.make = make
        
    def getMake(self):
        return self.make
    
    def printInfo(self):
        return '메이커='+self.make + '모델='+self.model + '색상='+self.color + '가격='+str(self.price) 
        #self.price가 정수라서 문자형으로 

    
class ElectricCar(Car): #자식클래스(부모클래스)
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make,model,color,price) #부모클래스에 있는 생성자 실행하라는 의미
        self.batterySize = batterySize
    
    def setBatterySize(self, batterySize):
        self.batterySize = batterySize
        
    def getBatterySize(self):
        return self.batterySize
    
    def printInfoElec(self):
        return super().printInfo() + str(self.batterySize)
    
def main():
    basicCar = Car("Hyundae ","Avante ", " Black ", 20000)
    print(basicCar.printInfo())
    myCar = ElectricCar("tesla"," model-s"," blue ", 100000, 0)
    myCar.setMake('tesla')
    myCar.setBatterySize(60)
    print(myCar.printInfoElec())
    print(type(basicCar))              #객체의 타입 확인
    print(type(ElectricCar))
    print(type(myCar))
    print(type(1))    

main()
