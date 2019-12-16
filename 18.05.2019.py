def unique_in_order(iterable):    
    sing = iterable[0]
    z = [sing]
    for i in iterable:
        if i != z[-1]:
            z.append(i)
    return z
    
print(unique_in_order('AAAABBBCCDAABBB'))