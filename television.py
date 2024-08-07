#객체는 변수+메소드


class Television:
    def __init__(self,ch,vol,on): #(변수)
        self.ch=ch
        self.vol=vol
        self.on=on
    
    def show(self):
        print(self.ch,self.vol,self.on)
        
    def setCh(self,ch):
        self.ch = ch
               
    def getCh(self):
        return self.ch
    
    def volUp(self):
        self.vol += 1
        
    def volDown(self):
        self.vol -= 1
        
    
    
# show() setCh() getCh() -> method

t = Television(9,10,True) #ch=9 vol=10 on=True 변수값 지정
t.show()

t.setCh(11) #ch=11 변수값 지정
t.show()

t.volUp()
t.show()

t.volDown()
t.show