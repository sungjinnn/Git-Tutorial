#사용자 정의 함수부
class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        
    
    

class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.__lt = Point(x1,y1)
        self.__rb = Point(x2,y2)
    def show(self):
        print(f'좌측 상단 꼭짓점이 ({self.__lt.x},{self.__lt.y})이고 우측 하단 꼭짓점이 ({self.__rb.x},{self.__rb.y})인 사각형입니다.')
    def getWidth(self):
        return self.__rb.x - self.__lt.x
    def getHeight(self):
        return self.__rb.y - self.__lt.y
    def getArea(self):
        return self.getWidth() * self.getHeight() 
    def getPerimeter(self):
        return (self.getWidth() + self.getHeight())*2

#주 프로그램부
r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')



