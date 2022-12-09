f = float(input("Enter Fahranheit"))
c = float(input("Enter Celsius"))
def fehranheit(x):
    a = x
    ca = (a - 32)*0.5556
    print("Celsius is ", ca,"C")

def celsius(x):
    a = x
    fa = (30 * 1.8)+32
    print("Fahranheit is", fa, "F")
celsius(c)    
fehranheit(f)
