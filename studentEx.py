class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def printInfo(self):
        print(self.name, self.age)
        
class Student:
    def __init__(self,id):
        self.id = id

    def getID(self):
        return self.id
    
class CollageStudent(Person,Student):
    def __init__(self,name,age,id):
        #부모클래스가 2개이기 때문에 super.를 쓰지 않는다.
        Person.__init__(self,name,age)
        Student.__init__(self,id)
    
    def printAllInfo(self):
        print(self.name, self.age, self.id)
           
obj = CollageStudent('kim', 22, '20202020')
obj.printAllInfo()