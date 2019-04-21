#  Try..except..else..finally.py
def divide_with_except(num1, num2):
    try:
        print (num1 / num2)
    except TypeError:
        print("TypeError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print("OK!")
    finally:
        print("Thanks for you watching my code!")

# divide_with_except(2, 4)      # 0.5   OK
# divide_with_except(0, 4)      # 0.0   OK
# divide_with_except(4, 0)      # ZeroDivisionError
# divide_with_except("4", 0)    # TypeError

