def number(text):
    while True:
        try:
            num = float(input(text))
            if(num>0):
                return num
            else:print("\tЗначение должно больше 0")
        except ValueError:
            print("\tВведено нечисловое значение")

class Shape:
    def __init__(self):
        self.name=""
        pass
    def area(self):
        pass
    def __str__(self):
        return f'{self.name},{self.area()}'

class Rectangle(Shape):
    def __init__(self):
        self.name="Прямоугольник"
        self.s1=number("\nВведите первую сторону прямоугольника:")
        self.s2=number("Введите вторую сторону прямоугольника:")
    def area(self):
        return self.s1*self.s2

class Square(Shape):
    def __init__(self):
        self.name="Квадрат"
        self.s=number("\nВведите сторону квадрата:")
    def area(self):
        return self.s**2

class Circle(Shape):
    def __init__(self):
        self.name="Круг"
        self.rad=number("\nВведите радиус круга:")
    def area(self):
        return 3.14*self.rad**2

rec=Rectangle()
sq=Square()
cir=Circle()
print("\n-------------------------------\n")
print(rec)
print(sq)
print(cir)