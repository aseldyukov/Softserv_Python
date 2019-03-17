# No yelling!

# Write a function taking in a string like WOW this is REALLY amazing 
# and returning Wow this is really amazing. 
# String should be capitalized and properly spaced. 
# Using re and string is not allowed.

def filter_words(st):        
    st = st.strip(' ')
    while '  ' in st:
        st = st.replace('  ',' ')        
    return st.upper()[0] + st.lower()[1:] 