class Student:
    def __init__(self,name=None, age=0): #접근 하지 못하는 변수 선언 or 지정
        self.__name=name #__를 붙이면 private
        self.__age=age
        
    def getAge(self): #변경불가능으로 지정한 값을 필요할때 쓰려면 따로 함수 지정해야함.
        return self.__age
    
    def setAge(self,age):
        self.__age = age
    
obj = Student("hong",50)
#print(obj.__age) -> 은닉 처리 됐기 때문에 오류가 남.
print(obj.getAge())
obj.setAge(100)
print(obj.getAge())