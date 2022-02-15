import math

def newcos(angle): #angle param, user selects what angle they would like to approximate cosine for

    angle %= 2*math.pi #as a means to counter large values out of taylor series window of accuracy, use mod functions to find cos of complementary angles
    
    result = 0 #initialize result value
    
    sign = 1 #cos taylor series polynomial start with positive number
    
    power = 0 
    
    for i in range(15):
    
        result += (angle**power) / math.factorial(power)) * sign
        
        sign *= -1
        
        power += 2
        
    return result

a = float(input("Enter an angle: "))

print(math.cos(a))

print(newcos(a))
