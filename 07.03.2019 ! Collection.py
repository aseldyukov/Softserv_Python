# 1
# середнє значення довільної кількості чисел

# def average(*args):    
#     return sum(list(args)) / len(list(args))

# test
# print(average(12,123,34,34,35,56))
# print(average(12))
# print(average(12,213,234234.3434))


# 2
# Написати функцію, яка повертає абсолютне значення числа

# def absolut(num):        
#     if num < 0:
#         return num * -1
#     else:
#         return num
# test
# print(absolut(-12))
# print(absolut(-1234234.6762))
# print(absolut(2312))



# 3
# Написати функцію, яка знаходить максимальне число з двох чисел, 
# а також в функції використати рядки документації DocStrings.
# def maximum(n1, n2):
#     '''знаходить максимальне число з двох чисел'''
#     print("maximum: ", n1 if n1>n2 else n2)

# maximum(23, 45)

# print(maximum.__doc__)


# 4
# Написати програму, яка обчислює площу
# прямокутника, 
# трикутника 
# кола 
# (написати три функції для обчислення площі, 
# і викликати їх в головній програмі в залежності від вибору користувача)
# choice  = int(input("What we will calc?. (1,2,3)"))

# def Square(choice):
#     if choice == 1:        
#         x = int(input("x:"))
#         y = int(input("y:"))
#         print("S=:",x*y)        
#     elif choice == 2:
#         x = int(input("x:"))
#         h = int(input("h:"))        
#         print("S=:", x*h)        
#     else:
#         r = int(input("r:"))                
#         print("S=:", 2 * 3.14 * r**2)        

# Square(choice)


# 5
# Написати функцію, яка обчислює суму цифр введеного числа.
# def sum(num): 
#     count = 0   
#     for i in str(num): 
#         count += int(i)
#     return count

# print(sum(123123123))
# print(sum(12))
# print(sum(1))


# 6
# Написати програму калькулятор, яка складається з наступних функцій:
expresion = input("Go!")
for i in expresion:
    