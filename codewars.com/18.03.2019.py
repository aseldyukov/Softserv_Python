# 1. Напишіть програму, яка пропонує користувачу ввести ціле число 
# і визначає чи це число парне чи непарне, чи введені дані коректні.
# try:
#     a = int(input("Input number: "))
#     if a == 0:
#         raise Exception("zero")

#     if a%2 == 0:
#         raise Exception("even number")

#     if a%2 != 0:
#         raise Exception("odd number")
        
# except Exception as e:
#    print("Exception exception " + str(e))


# 2.  Напишіть програму, яка пропонує користувачу ввести свій вік, 
# після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
# Необхідно передбачити можливість введення від’ємного числа, 
# в цьому випадку згенерувати власну виняткову ситуацію. 
# Головний код має викликати функцію, яка обробляє введену інформацію.

# def age(y):
#     try:
#         a = y
#         if a < 0:
#             raise Exception("wrong number")
#         if a == 0:
#             raise Exception("zero")
#         if a%2 == 0:
#             raise Exception("even number")
#         if a%2 != 0:
#             raise Exception("odd number")
            
#     except Exception as e:
#         print("Your age is " + str(e))

# age(int(input("Input your age: ")))

#################################################
# 3.  Напишіть програму для обчислення частки двох чисел, 
# які вводяться користувачем послідовно через кому, 
# передбачити випадок ділення на нуль, 
# випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
# Використати блоки else та finaly.

# OK = False
# while OK == False:
#     try:
#         a = input("Input two numbers with coma:").split(sep=",")    
#         n1 = int(a[0])
#         n2 = int(a[1])
#         rez = n1 / n2        
#     except ZeroDivisionError:
#         print("You can't divide on zero!")
#     except ValueError:
#         print("You input wrong information!")
#     except NameError:
#         print("You can't use letters!")
#     except TypeError:
#         print("You can't use letters!")
#     else:
#         print("Result is:", rez)
#         OK = True
#     finally:
#         print("Thank you!")
        

    
        
############################################# (1)
# n = input("Input entire number: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("\n You entered incorrect data!\n")
#         n = input("Input entire number:\n ")
 
# if n % 2 == 0:
#     print("{0} is the even number.".format(n))
# else:
#     print("{0} is the odd number.".format(n))
        
############################################# (2)
# def enterage(age):
#     if age < 0:
#         raise ValueError("Only positive integers are allowed")
 
#     if age % 2 == 0:
#         print("age is even")
#     else:
#         print("age is odd")
 
# try:
#     num = int(input("Enter your age: "))
#     enterage(num)
 
# except ValueError:
#     print("Only positive integers are allowed")
# except:
#     print("something is wrong")

########################################################(3)
# try:
#     num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
#     result = num1 / num2
#     print("Result is", result)
 
# except ZeroDivisionError:
#     print("Division by zero is error !!")
 
# except SyntaxError:
#     print("Comma is missing. Enter numbers separated by comma like this 1, 2")
#  #65866hgjh75785
# except:
#     print("Wrong input")
 
# else:
#     print("No exceptions")
 
# finally:
#     print("This will execute no matter what")


# 4.  Написати  програму, яка аналізує введене число та в залежності 
# від числа видає день тижня, який відповідає цьому числу 
# (1 це Понеділок, 2 це Вівторок і т.д.). 
# Врахувати випадки введення чисел від 8 і більше, 
# а також випадки введення не числових даних.

week = {1:'пон', 2:'вт', 3:'сер', 4:'чт', 5:'птн', 6:'суб', 7:'нед'}
try:
    day = int(input('Input # day:'))
    if day in week:
        raise Exception(week[day])
    else:
        raise Exception('Wrong number!')
except:
    print('Wrong number!')

except Exception as e:
    print("The day is:" + str(e))


##################################################(4)
# d = {
#     1: 'Monday',
#     2: 'Tuesday',
#     3: 'Wednesday',
#     4: 'Thursday',
#     5: 'Friday',
#     6: 'Saturday',
#     7: 'Sunday'
# }
# while True:
#     try:
#         i = int(input('Enter the day of the week: '))
#     except ValueError:
#         print('You did not enter a number!')
#     else:
#         print(d.get(i, 'There is no such day of the week!'))

##################################################(4)

# day_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# try:
#     num = int(input("Enter number from 1 to 7: "))
#     if num <= 0 or num > 7:
#         raise IndexError("Youre number is out of range")
#     print(day_list[num-1])
# except ValueError:
#     print("Wrong Input!")