from abc import abstractmethod, ABC


class House(ABC):

    def __init__(self, house_area, house_cost):
        self.house_area = house_area
        self.house_cost = house_cost

    @abstractmethod
    def apply_discount(self, percent):
        raise NotImplementedError('This method is not realized')


class Person(ABC):
    def __init__(self, person_name, person_age, person_money, person_home):
        self.person_name = person_name
        self.person_age = person_age
        self.person_money = person_money
        self.person_home = person_home

    @abstractmethod
    def human_info(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def make_money(self, house_cost):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError('This method is not realized')


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):

    def __init__(self, realtor_name, realtor_houses, realtor_discount):
        self.realtor_name = realtor_name
        self.realtor_houses = realtor_houses
        self.realtor_discount = realtor_discount

    def houses_info(self):
        print(f"Hello, I'm {self.realtor_name} and I offer {self.realtor_houses} houses.")
        return

    def give_discount(self):
        print(f"I can give you discount: {self.realtor_discount}%")

    def steal_money(self):
        pass


class OneHouse(House):

    def __init__(self, house_area, house_cost):
        super().__init__(house_area, house_cost)

    def apply_discount(self, percent):
        self.house_cost = self.house_cost * (100 - percent) / 100
        print(f'The cost of the house at a discount is $ {self.house_cost}\n')

    def onehouse_info(self):
        print(f'A {self.house_area} sq m house worth $ {self.house_cost} is for sale')


class OnePerson(Person):
    def __init__(self, person_name, person_age, person_money, person_home):
        super().__init__(person_name, person_age, person_money, person_home)

    def human_info(self):
        print(f'Hi, my name is {self.person_name}, I am {self.person_age} years old.')
        print(f'I have {self.person_money} dollars, and I want to buy a small house. \n')

    def make_money(self, house_cost):
        while self.person_money < house_cost:
            print('Not enough money. I need to go to make.')
            salary_for_the_month = 3000
            print(f'{self.person_name} worked for a month and earned $ 3000')
            self.person_money = self.person_money + salary_for_the_month
            print(f'I now have {self.person_money} dollars\n')
        else:
            return

    def buy_house(self, area, cost):
        print(f'Congratulations on buying a home!')
        self.person_home[area] = cost
        self.person_money = self.person_money - cost
        print(
            f'{self.person_name} bought a house {list(self.person_home)} sq.m for $ {list(self.person_home.values())}')
        print(f'{self.person_name} has $ {self.person_money} left')


realtor = Realtor('Alice', 'small', 10)
house1 = OneHouse(40, 70000)
person1 = OnePerson('Sara', 30, 70000, {})
person1.human_info()
realtor.houses_info()
house1.onehouse_info()

if person1.person_money < house1.house_cost:
    realtor.give_discount()

print('\n')
print('Well, make a purchase?')

buy_ok = ''
while buy_ok != 'Y' and buy_ok != 'N':
    buy_ok = input('Please enter Y or N : ')

    if buy_ok == "Y":
        house1.apply_discount(realtor.realtor_discount)
        person1.make_money(house1.house_cost)
        person1.buy_house(house1.house_area, house1.house_cost)

    elif buy_ok == 'N':
        print('Goodbye.')
    else:
        continue
