class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print('도형을 그림')
            
class Circle(Shape): #부모 클래스의 생성자 상속 받겠다는 의미
    def __init__(self, x, y, radius) : #상속받은 것 외에 쓰고자 하는 변수를 추가하면 됨.
        super().__init__(x,y)
        self.radius = radius
        
    def printArea(self):
        print('원의 면적 = ', 3.14*(self.radius**2))
    
    def draw(self):
        print('원을 그림')
            
class Rectangle(Shape):
    def __init__(self,x,y,base,height):
        super().__init__(x,y)
        self.base = base
        self.height = height
        
    def printArea(self):
        print("사각형의 면적 =", self.base*self.height)
        
    def draw(self):
        print('도형을 그림')
        
c1 = Circle(5,6,10) 
c1.printArea()
c1.draw()

r1 = Rectangle(100,200,5,6)
r1.printArea()
r1.draw()

# 다양성
# 같은 draw라는 이름을 쓰지만 다른 기능이 가능함.
