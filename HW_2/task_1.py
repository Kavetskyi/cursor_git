# Lecture #2 OOP
# Task 1

class Animal:
    def __init__(self, type, eat, sleep):
        self.type = type
        self.eat = eat
        self.sleep = sleep

    def animal_info(self):
        self.type = "The " + self.type + " must " + self.eat + ", " + self.sleep

class Eagle(Animal):
    def __init__(self, type, eat, sleep, fly):
        super().__init__(type, eat, sleep)
        self.fly = fly

    def eagle_info(self):
        self.type = self.type + ", " + self.fly

class Fish(Animal):
    def __init__(self, type, eat, sleep, swim):
        super().__init__(type, eat, sleep)
        self.swim = swim

    def fish_info(self):
        self.type = self.type + ", " + self.swim

class Dolphin(Fish):
    def __init__(self, type, eat, sleep, swim, jump):
        super().__init__(type, eat, sleep, swim)
        self.jump = jump

    def dolphin_info(self):
        self.type = self.type + ", " + self.jump

class Tiger(Animal):
    def __init__(self, type, eat, sleep, hunt):
        super().__init__(type, eat, sleep)
        self.hunt = hunt

    def tiger_info(self):
        self.type = self.type + ", " + self.hunt

class Raccoon(Animal):
    def __init__(self, type, eat, sleep, steal):
        super().__init__(type, eat, sleep)
        self.steal = steal

    def raccoon_info(self):
        self.type = self.type + ", " + self.steal


oneanimal = Eagle('eagle', 'eat', 'sleep', 'fly')
oneanimal.animal_info()
oneanimal.eagle_info()
print(oneanimal.type)

oneanimal = Fish('fish', 'eat', 'sleep', 'swim')
oneanimal.animal_info()
oneanimal.fish_info()
print(oneanimal.type)

oneanimal = Dolphin('dolphin', 'eat', 'sleep', 'swim', 'jump')
oneanimal.animal_info()
oneanimal.fish_info()
oneanimal.dolphin_info()
print(oneanimal.type)

oneanimal = Tiger('tiger', 'eat', 'sleep', 'hunt')
oneanimal.animal_info()
oneanimal.tiger_info()
print(oneanimal.type)

oneanimal = Raccoon('raccoon', 'eat', 'sleep', 'steal')
oneanimal.animal_info()
oneanimal.raccoon_info()
print(oneanimal.type)

# Task 1a
class Human:
    def __init__(self, study, work):
        self.study = study
        self.work = work

    def human_info(self):
        self.type = self.type + ", " + self.study + ", " + self.work

class Centaur(Animal, Human):
    def __init__(self, type, eat, sleep, study, work, sing):
        Animal.__init__(self, type, eat, sleep)
        Human.__init__(self, study, work)
        self.sing = sing

    def centaur_info(self):
        self.type = self.type + ", " + self.sing

oneman = Centaur('centaur', 'eat', 'sleep', 'study', 'work', 'sing')
oneman.animal_info()
oneman.human_info()
oneman.centaur_info()
print(oneman.type)
