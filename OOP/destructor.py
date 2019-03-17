class Class1:
    def __init__(self):  # Конструктор класу
        print("Called the method __init__()")
    def __del__(self):  # Деструктор классу
        print("Called the method __del__()")
################################################################        
# c1 = Class1()          # Виведе: Called the method __init__()
# del c1                 # Виведе: Called the method __del__()
# c2 = Class1()          # Виведе: Called the method __init__()
# c3 = c2                # Створюємо посилання на екземпляр класу
# del c2                 # Ничого не виведе, так як існує посилання
# del c3                 # Виведе: Called the method __del__()