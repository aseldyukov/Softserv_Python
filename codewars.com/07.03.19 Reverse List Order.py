# Reverse List Order

# In this kata you will create a function 
# that takes in a list and 
# returns a list with the reverse order.

def reverse_list(*args):       
    new=[]
    for i in list(args)[::-1]:
        new.append(i)