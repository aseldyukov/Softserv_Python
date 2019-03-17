# I found this code, but don't undersand how it works
# I need explanation for this code

def func(x):
    def add(a):
        return x + a
    return add

test = func(100)
print (test (200) )

# 300