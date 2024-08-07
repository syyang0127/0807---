class Counter: # class의 이름은 대문자로 시작해야함.
    def __init__(self): # 생성자는 암기해야함. 객체 생성할때 자동으로 실행.
        self.count = 0 #변수
    def increment(self): #위 변수를 다루는 함수
        self.count += 1

a=Counter()
b=Counter()
c=Counter()

#각각의 객체가 클래스에 정의된 변수를 가지고 있다.
a.increment()
a.increment()

b.increment()

print(a.count)
print(b.count)
print(c.count)

#클랜스도 모듈화해서 사용 가능함.