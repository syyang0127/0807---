## 연산자에 대응하는 각각 메소드가 정의돼있다.
## x +y ---> __add__(self,y)


#객체끼리 연산하는 예제
class Vector2D:
    def __init__(self,x,y): 
        self.x=x
        self.y=y
        ## 변수 2개만 쓰겠다는 의미
    
    def __add__(self,other):  #vector2D로 만든 값을 받는다.
        return Vector2D(self.x+other.x, self.y+other.y)
    
    def __sub__(self,other):
        return Vector2D(self.x-other.x, self.y-other.y)
    
    def __eq__(self,other):
        return (self.x==other.x and self.y==other.y)     #논리값 리턴
    
    def __str__(self):        #self값만
        return '(%g,%g)'%(self.x, self.y)                #문자열 리턴
    
u = Vector2D(0,1) #2차원 좌표값
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v

print(a)