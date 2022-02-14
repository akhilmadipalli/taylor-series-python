import math

def newsin(angle):

    angle = math.fmod(angle + math.pi, 2*math.pi) - math.pi
    
    result = 0
    
    sign = 1
    
    power = 1
    
    for i in range(15):
    
        result += (math.pow(angle, power) / math.factorial(power)) * sign
        
        sign *= -1
        
        power += 2
        
    return result
    
a = float(input("Enter an angle: "))
print(math.sin(a))
print(newsin(a))