def zero_fuel(distance_to_pump, mpg, fuel_left):
    way = distance_to_pump - (mpg * fuel_left)
    if way >= 0:
        return True
    else:
        return False

