def fahr_to_celsius(temp):
    celcius = ((temp - 32) * (5/9))
    return celcius
    
print('100 degree Fahrenheit are ' + str(fahr_to_celsius(100)) + ' degree Celsius.' )