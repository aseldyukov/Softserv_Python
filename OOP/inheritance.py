# Inheritance
class Part1:
    def m1(self):
        print("Part1 m1")
    def m2(self):
        print("Part1 m2")
class Part2:
    def m2(self):
        print("Part2 m2")
    def m3(self):
        print("Part2 m3")
class Child(Part1,Part2):
    pass

c=Child()
#
c.m3()
#
c.m1()
# #
c.m2()
#
# множинне наслідування bad practice
#змінні рівня класу називаються статичні змінні
#статичні методи до даних класу не доступаються
