# Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. 
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
def fibo(n):
    fib = [0, 1]
    i = 0

<<<<<<< HEAD
    while i <= n-2:
        i += 1                    
        fib.append(0)
        fib[-1] = fib[-2] + fib[-3]
        
    return fib
print(fibo(6))
=======
num = 0
while not(num >2):
    num = int(input('Введіть число:'))
fib = [0, 1]
i = 0

while i <= num-2:
    i += 1                    
    fib.append(0)
    fib[-1] = fib[-2] + fib[-3]
    
print(fib)



# varian 2 #################################################
# Function for nth Fibonacci number 

def Fibonacci(n): 
	if n<0: 
		print("Incorrect input") 
	# First Fibonacci number is 0 
	elif n==1: 
		return 0
	# Second Fibonacci number is 1 
	elif n==2: 
		return 1
	else: 
		return Fibonacci(n-1)+Fibonacci(n-2) 

	print(Fibonacci(9)) 

>>>>>>> 39d97b5b583f237551d05c46e2c4de40cba4999a
