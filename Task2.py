def number(text):
    while True:
        try:
            num = float(input(text+"\n"))
            if (num > 0):
                return num
            else:
                print("\tЗначение должно больше 0")
        except ValueError:
            print("\tВведено нечисловое значение")

def houseNum(text):
    while True:
        try:
            num = int(input(text))
            if (num >= 0 and num<=len(houseList)):
                return num-1
            else:
                print("\tНеправильно: от 0 до ",len(houseList))
        except ValueError:
            print("\tВведено нечисловое значение")


class House:
    def __init__(self, price, area):
        self._price = price
        self._area = area

    def __str__(self):
        return f' Площадь: {self._area}, цена: {self._price}'

    def final_price(self, discount):
        return self._price * (1 - discount * 0.01)


class SmallHouse(House):
    def __init__(self,price):
        self._price=price
        self._area=40


class Human:
    def __init__(self):
        self.budget = 10000
        self.name = "Hooman"
        self.houses = []

    def buy_house(self, house, discount):
        pr = house.final_price(discount)
        if self.budget < pr:
            print("У вас нет денег (можно заработать)")
        else:
            self.make_deal(house, pr)
            houseList.remove(house)

    def make_deal(self, house, pr):
        self.budget = self.budget - pr
        self.houses.append(house)
        print(self.name, " купил дом площадью", house._area, " за ", pr, " со скидкой",discount, " %")

    def earn_money(self):
        self.budget=self.budget+2000
        print("Непосильным трудом вы заработали 2000 денег")

    def see_your_status(self):
        print("Бюджет: ",self.budget)
        print("----Твои дома----:")
        if(len(self.houses)==0): print("\tУ вас нет домов")
        else:
            for i,val in enumerate(self.houses):
                print("Дом ", i + 1, ": ", val)


houseList = []
hum=Human()
discount=0
while True:
    choice = number("\nВыберите действие:"
                    "\n 1 - Создать дом"
                    "\n 2 - Создать маленький дом"
                    "\n 3 - Ввести скидку"
                    "\n 4 - Купить дом"
                    "\n 5 - Заработать денег (если их не хватает)"
                    "\n 6 - Просмотреть свой статус"
                    "\n 7 - Выйти")
    if (choice == 1):
        area = number("Введите площадь дома: ")
        price = number("Введите цену дома: ")
        h = House(price, area)
        houseList.append(h)
        print("Вы добавили дом")
    elif (choice == 2):
        price = number("Введите цену дома: ")
        h = SmallHouse(price)
        houseList.append(h)
        print("Вы добавили маленький дом")
    elif (choice==3):
        while True:
            discount=number("Введите скидку (в процентах): ")
            if(discount<100):break
            else:print("Скидка меньше 100%")
    elif (choice == 4):
        if(len(houseList)==0):print("Нет домов в наличии")
        else:
            for i, val in enumerate(houseList):
                print("Дом ", i + 1, ": ", val)
            print("\t(скидка: ",discount," %)")
            i=houseNum("Введите номер дома или 0 для выхода:\n")
            if(i!=-1):
                hum.buy_house(houseList[i],discount)
    elif (choice == 5):hum.earn_money()
    elif (choice == 6):hum.see_your_status()
    elif (choice == 7):break
    else:print('\tНеправильный номер')