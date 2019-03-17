# class A:
#     def __init__(self, v1, v2):
#         self.field1 = v1
#         self.field2 = v2
# a = A(3, 4)
# print("Output without magic method str ", a)

# ?<__main__.A object at 0x7f840c8acfd0>

#####################################################
# Якщо ми хочемо, щоб, коли об'єкт передається у функцію print(), 
# виводилась інша інформація, 
# для цього необхідно в клас додати спеціальний метод __str__().
# Цей метод обовязково повинен повертати стрічку,
# яку буде виводити функція print():

# class A:
#     def __init__(self, v1, v2):
#         self.field1 = v1
#         self.field2 = v2
#     def __str__(self):
#         return str(self.field1) + " " + str(self.field2)
 
# a = A(3, 4)
# print("Output with magic method str ", a)


#####################################################
# яку саме стрічку повертає метод str не суттєво,
# він може навіть будувати квадратики
# class Rectangle:
#     def __init__(self, width, height, sign):
#         self.w = int(width)
#         self.h = int(height)
#         self.s = str(sign)
#     def __str__(self):
#         rect = []
#         for i in range(self.h):             # к-сть стрічок
#             rect.append(self.s * self.w)    # знак повторюється w раз
#         rect = '\n'.join(rect)              # перетворюємо список в стрічку
#         return rect
 
# b = Rectangle(10, 3, '*')
# print(b)