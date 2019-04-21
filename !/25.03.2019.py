# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 
# і пропонує користувачу вгадати це число. 
# Програма зчитує числа, які вводить користувач і видає користувачу підказки 
# про те чи загадане число більше чи менше за введене користувачем. 
# Гра має тривати до моменту поки користувач не введе число, 
# яке загадане програмою, тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, 
# а з нього функцію randint())

# from random import randint as rnd

# num = rnd(1, 100)
# n = 0
# while num != n:
#     n = int(input('Guess my number: '))
#     if n < num:
#         print('My number bigger then you!')
#     elif n > num:
#         print('My number less then you!')
#     else:
#         print('You guess!')



############################################################# 
# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, 
# площу трикутника 0.5*h*a, 
# площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, 
# а з нього функцію pow() та значення змінної пі).
# from math import pow, pi

# hight = int(input('input hight:'))
# width = int(input('input width:'))
# radius = int(input('input radius:'))

# S_rectangle = hight * width
# S_triangle = hight * width * 0.5
# S_round = pi * pow(radius, 2)

# print('Square of rectangle is:', S_rectangle)
# print('Square of triangle is:', S_triangle)
# print('Square of round is:', S_round)