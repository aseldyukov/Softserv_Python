# even = 0,2,4
# odd  = 1,3,5


def parse_number(num):
    odd = even = 0
    d = {}
    if isinstance(num, str):
        return 'word'         
    for i in list(str(num)):
        i = int(i)
        if i == 0 or i%2 == 0:
            even += 1
        elif  i%2 != 0:
            odd += 1

    d['odd'] = odd
    d['even'] = even
    return d

print (parse_number(123234450))

