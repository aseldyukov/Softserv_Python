# a = [12,23,34,56,67]
# a = [] # очистка списка через присваивание
# a[:] = [] # очистка списка через срез
# a.clear() # очистка списка методом clear()
# print (a)

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

man = Person('Ivan', 23)
print(man.name)
print(man.age)


