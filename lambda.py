#  Нет return
##############################
add = lambda x, y: x * y

print (add(2, 5)) # 10

##############################
print ((lambda x, y: x * y)(2, 6)) # 12

##############################
fun = lambda *args: args
print(fun (12,23,45))  #(12, 23, 45)