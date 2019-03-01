#  Роздрукувати всі непарні числа менші 100. 
# (написати два варіанти коду: один використовуючи оператор continue, 
# а інший без цього оператора).

#  1
for i in  range(1, 100):
    if i%2 == 0:
        continue
    print(i)    

#  2
i = 0
while i < 100:
    if i%2 == 0:
        i += 1
        continue
    print(i)    
    i += 1

#  3
for i in range(1, 100, 2):
    print(i)
