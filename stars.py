

# функция построения линии
def f_Line(begin, count): 
    return " "*begin + "*"*count

# функция построения треугольника 1
def TriangleUp(count):
    triangle = ""        
    for i in range(count+1):
        triangle = triangle + f_Line(0, i) + "\n"
    return triangle
        
# функция построения треугольника 2
def TriangleDown(count):
    triangle = ""        
    for i in list(range(count+1))[::-1]:
        triangle = triangle + f_Line(0, i) + "\n"
    return triangle

# функция построения треугольника 3
def TriangleBig(count):
    triangle = "" 
    for i in range(count):
        triangle = triangle + f_Line(count - i + 1, i * 2 + 1) + "\n"
    return triangle


# функция построения звезды Давида
def Star(count):
    top = round(count / 3, 0)   
    ii = count
    i = 1
    star = ""

    star = star + f_Line(count + 1, 1) + "\n"
    
    while i <= count or ii >= 1:    
        if i >= top:
            if len(f_Line(count - i + 1, i * 2 + 1)) > len(f_Line(count - ii, ii * 2 + 1)) and i <= count: 
                star = star + f_Line(count - i + 1, i * 2 + 1) + "\n"   
            else:
                star = star + f_Line(count - ii + 1, ii * 2 + 1) + "\n"                  
            
            ii = ii - 1 
        else:
            star = star + f_Line(count - i + 1, i * 2 + 1) + "\n"
        i = i + 1
    star = star + f_Line(count + 1, 1) + "\n"
    return star
    
  

count = int(input("What number? (from 10 to 20)"))
print(TriangleUp(count))
print(TriangleDown(count))
print(TriangleBig(count))
print(Star(count))
