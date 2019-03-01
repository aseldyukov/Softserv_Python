# Will there be enough space?

# Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. 
# With so many passengers wanting to get aboard his bus, 
# he sometimes has to face the problem of not enough space left on the bus! 
# He wants you to write a simple program telling him if he will be able to fit all the passengers.
# Task Overview:
# You have to write a function that accepts three parameters:
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    return abs(cap-(on+wait))
