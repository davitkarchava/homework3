# მაგალითი_1
class Celsius:

    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, new_temperature):
        self.__temperature = new_temperature

    def del_temperature(self):
        del self.__temperature

    temperature = property(get_temperature, set_temperature, del_temperature)


temper_1 = Celsius(30)
print("პირველი ტემპერატურის საწყისი ტემპერატურა: ", "\n", temper_1.temperature)
temper_1.temperature = 25
print("პირველი ტემპერატურის შეცვლილი ტემპერატურა: ", "\n", temper_1.temperature)
temper_2 = Celsius(40)
print("მეორე ტემპერატურის საწყისი ტემპერატურა: ", "\n", temper_2.temperature)
temper_2.temperature = 35
print("მეორე ტემპერატურის შეცვლილი ტემპერატურა: ", "\n", temper_2.temperature)
del temper_1.temperature
print(temper_1.temperature)
del temper_2.temperature
print(temper_2.temperature)


# მაგალითი_2

class Bank_Account:

    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    def __str__(self):
        return F"გამარჯობა {self.__account_name}, თქვენ ანგარიშზე გაქვთ: {self.__balance} ლარი"

    def get_acname(self):
        return self.__account_name

    def set_acname(self, new_account_name):
        self.__account_name = new_account_name

    def deposit(self):
        plus_balance = int(input(f"{self.__account_name} შეიყვანეთ თანხა, რომლის დამატებაც გსურთ ანგარიშზე: "))
        self.__balance += plus_balance
        print(f"თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ: {self.__balance} ლარი")

    def withdraw(self):
        minus_balance = int(input(f"{self.__account_name} შიყვანეთ თანხა, რომლის გამოტანაც გსურთ ანგარიშიდან: "))
        self.__balance -= minus_balance
        if self.__balance < 0:
            print(f"{self.__account_name} თქვენ ანგარიშზე არ გაქვთ საკმარისი თანხა.")
        else:
            print(f"თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ: {self.__balance} ლარი")


bank_account = Bank_Account("დავითი")
print(bank_account)
bank_account.deposit()
bank_account.withdraw()

# მაგალითი_3
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)


point1 = Point(3, 4)
point2 = Point(6, 9)
print("\n", point1.distance(), "\n", point2.distance())


# ბონუს დავალება_1
class Fraction:

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def sum(self, fraction_1, fraction_2):
        return f"წილადების ჯამია: \n {((fraction_2.bottom * fraction_1.top) + (fraction_1.bottom * fraction_2.top))}/{(fraction_1.bottom * fraction_2.bottom)}"

    def inverse(self):
        return f"{self.bottom}/{self.top}"


wiladi_1 = Fraction(2, 5)
wiladi_2 = Fraction(3, 5)
print("პირველი წილადია: ", "\n", wiladi_1)
print("მეორე წილადია: ", "\n", wiladi_2)
print(wiladi_1.sum(wiladi_1, wiladi_2))
print("პირველი წილადი შემობრუნებულად: ", "\n", wiladi_1.inverse())
