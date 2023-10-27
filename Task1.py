import math

def number(text):
    while True:
        try:
            num = float(input(text+"\n"))
            return num
        except ValueError:
            print("Введено нечисловое значение")
class Triangle():
    side1=0
    side2=0
    side3=0
    def __init__(self,s1,s2,s3):
        if(self.check(s1,s2,s3)):
            self.side1=s1
            self.side2=s2
            self.side3=s3
    @staticmethod
    def check(a,b,c):
        if(a<=0 or b<=0 or c<=0 ):
            print("Стороны треугольника должны быть больше 0")
            return False
        if(a+b<=c or b+c<=a or a+c<=b):
            print("Такого треугольника не существует")
            return False
        return True
    def perimetr(self):
        return self.side1+self.side2+self.side3


    def area(self):
            p=self.perimetr()/2
            return math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))

a=number("Введите сторону а: ")
b=number("Введите сторону b: ")
c=number("Введите сторону c: ")
tr1=Triangle(a,b,c)
if(tr1.side1!=0):
    print("Периметр: ",tr1.perimetr())
    print("Площадь: ",tr1.area())