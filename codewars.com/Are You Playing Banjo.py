# Are You Playing Banjo?

def areYouPlayingBanjo(name):
    if name[0].upper() == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name
    
        
    # 2
    # name = name + '{}'.format(' plays banjo' if name[0].upper() == 'r' else " does not play banjo")    
    # return name