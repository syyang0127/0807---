
"""
class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn
        
book = Book("the python tutorial","2883948234")
print(book)

# terminal output
# <__main__.Book object at 0x7fd90bc47c10>
"""
# __repr__ 메소드를 사용한 후

class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn

    def __repr__(self):    
        return "ISBN:"+ self.__isbn+", Name : "+self.__title

book = Book("the python tutorial", "2883948234")
book2 = Book("the machine language", "1291029312")

print(book)
print(book2)

# terminal output
# ISBN:2883948234, Name : the python tutorial
# ISBN:1291029312, Name : the machine language