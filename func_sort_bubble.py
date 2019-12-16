from random import randint

def func_sort_bubble(args):    
    sort_list = []
    #  перебираємо весь список
    for z in range(len(args)):
                
        # знаходимо найменьше число в списку
        min = args[0]
        for i in range(len(args)):
            if args[i] <= min:         
                min = args[i]
                min_index = i
        args.pop(min_index)
        sort_list.append(min)        
    return sort_list

# формуємо список для сортування
chaos = []
for i in range(10):
    chaos.append(randint(0, 100)) 

print('previous list: {}'.format(chaos))
print('result of bubble sort: {}'.format(func_sort_bubble(chaos)))

