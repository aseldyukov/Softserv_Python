# Summation
# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.

def summation(num):
    a = [x for x in range(1, num+1)]
    print (a)
    return sum(a)