# Count of positives sum of negatives

# Given an array of integers.
# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):    
    count = 0
    sum = 0     
    for i in arr:
        if i > 0:        
            count += 1
        elif i < 0:
            sum += i        
    
    if count != 0 or sum !=0:
        return [count] + [sum]
    elif len(arr)>0:
        return [count] + [sum]
    else: return []