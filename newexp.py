import math

def newexp(value):

    result = 0

    power = 0
    
    for i in range(100):
    
        result += (math.pow(value, power) / math.factorial(power))
        
        power += 1
        
    return result

v = float(input("Enter a value: "))
print(math.exp(v))
print(newexp(v))