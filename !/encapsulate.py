# class A:
#     def _private(self):
#         print("This is a private method!")

# a = A()
# a._private()

#################################
# class B:
#      def __private(self):
#          print("This is a private method!")

# b = B()
# # b.__private()
# # # ####але атрибут залишається доступним 
# # # #від імені класу
# b._B__private()



# #Encapsulation
# class Sample:
#     def __init__(self):
#         self._protected="Protected"
#         self.__private="Private"

# s=Sample()

# print(s._protected) 

# print(s.__private)   #

# print(s._Sample__private)

# #від наслідуваного класу достукатися 
# # до цього поля ми не зможемо
# ######################
# class Sample2(Sample):
#     pass
# s2=Sample2()
# #
# print(s2._protected) 
# #
# print(s2._Sample2__private)

##################################################
# class Encapsulation():
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c

# ###############################

# x = Encapsulation(11,13,17)
# print(x.public)
# print(x._protected)
# ######
# x._protected = 23
# print(x._protected)
# ####
# print(x.__private) #Error