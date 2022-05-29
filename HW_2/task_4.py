# Lecture #2 OOP
# Task 4
from abc import abstractmethod, ABC

class Laptop:
    @abstractmethod
    def Screen(self):
        raise NotImplementedError('This method must be defined!')

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError('This method must be defined!')

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError('This method must be defined!')

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError('This method must be defined!')

    @abstractmethod
    def Ports(self):
        raise NotImplementedError('This method must be defined!')

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError('This method must be defined!')


class HPLaptop(Laptop):
    def __init__(self):
        pass

    def Screen(self):
        self.screen = input('Please enter information about screen: ')
        return self.screen

    def Keyboard(self):
        self.keyboard = input('Please enter information about keyboard: ')
        return self.keyboard

    def Touchpad(self):
        self.touchpad = input('Please enter information about touchpad: ')
        return self.touchpad

    def WebCam(self):
        self.webcam = input('Please enter information about web cam: ')
        return self.webcam

    def Ports(self):
        self.ports = input('Please enter information about ports: ')
        return self.ports

    def Dynamics(self):
        self.dynamics = input('Please enter information about dynamics: ')
        return self.dynamics

    def laptop_info(self):
        self.Screen()
        self.Keyboard()
        self.Touchpad()
        self.WebCam()
        self.Ports()
        self.Dynamics()
        print('Information: ' + 'Screen - ' + self.screen + ';')
        print('             ' + 'Keyboard - ' + self.screen + ';')
        print('             ' + 'Touchpad - ' + self.touchpad + ';')
        print('             ' + 'WebCam - ' + self.webcam + ';')
        print('             ' + 'Ports - ' + self.ports + ';')
        print('             ' + 'Dynamics - ' + self.dynamics + '.')

mycomp = HPLaptop()
mycomp.laptop_info()
