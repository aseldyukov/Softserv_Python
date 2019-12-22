def getCount(inputStr):
    num_vowels = 0    
    inputStr = inputStr.lower()
    
    i = len(inputStr)
    
    while i >= 0:
        if inputStr[i:] in list('aeiou'):
            num_vowels += 1
        i -= 1
    return num_vowels

getCount("abracadabra")