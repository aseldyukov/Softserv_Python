# Створити список, який містить елементи цілочисельного типу, 
# потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# (Підказка: використати вбудовану функцію float ()).

s = [123, 213, 345, 345, 345]
j = 0
for i in s:
    s[j]= float(i)
    j += 1

print(s)