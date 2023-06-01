######################### HOMEWORK #################################
def Exponent(base,exponent):
    if type(base)!= int and type(exponent)!= int:
        raise TypeError("The argument must be Integer")
    elif base <0 or exponent <0 :
        raise ValueError("The argument must be positive")
    else:
        result = base ** exponent
        return result
    
a = Exponent(10,2)
print(a)


######################### Class Example ############################
def PowerOfTwo(number):
    if type(number)!= int:
        raise TypeError("The argument must be Integer")
    elif number <0 :
        raise ValueError("The argument must be positive")
    else:
        return number*number

while True:
    try:
        a = int(input("Enter square side = "))
        try:
             area = PowerOfTwo(a)
             print(f'The sq ({a}) --> area {area}')
        except ValueError:
            print("You must enter only positive values!")
    except TypeError:
        print("You must enter only integer values!")



