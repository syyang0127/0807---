class Television2:
    objectCnt=0 #클래스 변수 #상수들은 변수명 전체를 대문자로(정확한 의미전달 위해서)
    
    def __init__(self,ch,vol,on):
        self.ch = ch
        self.vol = vol
        self.on = on
        Television2.objectCnt += 1 #객체를 만들때마다 cnt의 숫자 증가함.
        #class 변수는 클래스 이름으로 변수 지정해야함.
        
    def show(self):
        print(self.ch,self.vol,self.on,self.objectCnt)
        
myTv = Television2(24,10, True) #cnt의 값이 1 증가.
myTv.show() # cnt = 1

yourTv = Television2(24,10, False) #cnt의 값이 1 증가. 현재 2
yourTv.show() # cnt = 2
myTv.show() # cnt = 2

ourTv = Television2(24,10,True)
yourTv.show() # cnt = 3
myTv.show() # cnt = 3
ourTv.show() # cnt = 3