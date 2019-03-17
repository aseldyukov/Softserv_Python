# Створити батьківський клас Figure з методами init: ініціалізується колір, 
# get_color: повертає колір фігури,
# info: надає інформацію про фігуру та колір,  
# від якого наслідуються такі класи як Rectangle, Square, 
# які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.

class Figure():
    def __init__ (self, color):
        self.color = color
    def get_color (self):
        return "Color is: {}".format(self.color)
    def info (self):
        return "Info about figure is: bla-bla-bla fnd color is: {}".format(self.color)
       
class Rectangle():



f = Figure(3)
print(f.get_color())


    