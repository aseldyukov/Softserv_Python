# Створити список цілих чисел, які вводяться з терміналу 
# та визначити серед них максимальне та мінімальне число.

arr = [int(input("Введіть число:")) for x in range(10)]


print('максимальне число: ', max(arr))
print('мінімальне число: ', min(arr))
print(arr)