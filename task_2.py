# Lecture #2 OOP
# Task 2
# a. Composition
class Person:
    def __init__(self):
        arm_left = Arm('with tattoo')
        arm_right = Arm('without a tattoo')
        self.arms = [arm_left.shape, arm_right.shape]

class Arm:
    def __init__(self, shape):
        self.shape = shape

person = Person()
print(person.arms)

#b. Agregation
class CellPhone:
    def __init__(self, screens):
        self.screens = screens

class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type

screens = Screen('PrintScreen')
print(screens.screen_type)
cellphone = CellPhone(screens.screen_type)
print(cellphone.screens)

