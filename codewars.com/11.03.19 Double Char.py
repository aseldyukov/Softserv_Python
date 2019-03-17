# Double Char

# Given a string, you have to return a string 
# in which each character (case-sensitive) is repeated once*.

# repeated twice (it's more correctly!)

def double_char(s):
    output = ''
    i = 0    
    while i < len(list(s)):                
        output += s[i] * 2
        i += 1
    return output