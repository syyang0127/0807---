class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def getSpeed(self):
        return self.speed
        
myCar = Car(0,"blue","E-class")
print('자동차 객체를 생성함')
print('자동차의 속도는',myCar.speed)
print('자동차의 색상은',myCar.color)
print('자동차의 모델은',myCar.model)


myCar.setSpeed(60)
print('자동차의 속도는',myCar.speed,'으로 설정됨')
