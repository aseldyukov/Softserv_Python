# Поліморфізм - різна поведінка одного і того ж метода в різних класах. 
# Наприклад, ми можемо додати два числа, і можемо додати дві стрічки. 
# При цьому отримаємо різний результат, так як числа і стрічки є різними класами.
# Поліморфізм це різна реалізація методів з однаковими іменами

# print(1+1)
# print("1"+"1")
# print("*"*20)

# Поліморфізм дає можливість реалізувати так звані єдині інтерфейси для обєктів різних класів. 
# Наприклад, різні класи можуть передбачувати різний спосіб виводу тої чи іншої інформації обєктів. 
# Але однакова назва метода виводу дозволить не спантеличити
# програму, зробити код більш зрозумілішим.

class T1:
     N=10
     def total(self, n):
          self.total = int(self.N) + int(n)
 
class T2:
     def total(self,s):
          self.total = len(str(s))
 
t1 = T1()
t2 = T2()
t1.total(45)
t2.total(45)
print(t1.total) # output: 55
print(t2.total) # output: 2