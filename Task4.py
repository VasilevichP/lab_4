def number(text):
    while True:
        try:
            num = int(input(text+"\n"))
            if (num > 0):
                return num
            else:
                print("\tЗначение должно больше 0")
        except ValueError:
            print("\tВведено нечисловое значение")

def catNum(text):
    while True:
        try:
            num = int(input(text+"\n"))
            if (num > 0 and num<=len(Cat.cats)):
                return num-1
            else:
                print("\tНеправильно: от 1 до",len(Cat.cats))
        except ValueError:
            print("\tВведено нечисловое значение")

class Cat:
    total_number=0
    cats=[]

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Cat.add_cat(self)

    @staticmethod
    def info():
        print("Котов много не бывает. Добавь.")

    @classmethod
    def add_cat(cls,cat):
        cls.total_number=cls.total_number+1
        cls.cats.append(cat)

    def pet(self):
        return f'{self.name} потерся о вашу ладонь'

    def birthday(self):
        self.age=self.age+1
        return f'{self.name} стал старше на год! теперь ему {self.age}'

    @classmethod
    def show(cls):
        if(len(cls.cats)!=0):
            for i in cls.cats:
                print(i)
            print("У вас ", cls.total_number, " кот(а/ов)")
        else:
            print("У вас нет котов")
        cls.info()

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}'

print("Вы - начинающий кошатник")
while True:
    choice = number("\nВыберите действие:"
                    "\n 1 - Добавить кота"
                    "\n 2 - Погладить кота"
                    "\n 3 - Отпраздновать день рождения кота"
                    "\n 4 - Пересчитать своих котов"
                    "\n 5 - Выйти")
    if (choice == 1):
        name = input("Дайте ему хорошее имя: \n")
        age = number("Сколько лет? ")
        с = Cat(name,age)
        print("Теперь у вас есть",name)
    elif (choice == 2):
        if (len(Cat.cats) != 0):
            for i,val in enumerate(Cat.cats):
                print("",i+1, " : ",val)
            i=catNum("Кого погладить? (Выберите номер кота)")
            c=Cat.cats[i]
            print(c.pet())
        else:
            print("У вас нет котов")
            Cat.info()
        print()
    elif (choice==3):
        if (len(Cat.cats) != 0):
            for i, val in enumerate(Cat.cats):
                print("", i+1, " : ", val)
            i = catNum("Чей день рождения отпраздновать? (Выберите номер кота)")
            c = Cat.cats[i]
            print(c.birthday())
        else:
            print("У вас нет котов")
            Cat.info()
        print()
    elif (choice == 4):
        Cat.show()
    elif (choice == 5):break
    else:print('\tНеправильный номер')