
def fahernheit_to_celsius(f_temp):
    # (F-32)*5/9
    return round((f_temp - 32) * 5/9, 2)
    
def celsius_to_fahrenheit(c_temp):
    # (C * 9/5) + 32
    return round((c_temp * 9/5) + 32, 2)