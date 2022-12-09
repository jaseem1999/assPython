x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
def addition(num1,num2):
    a1 = num1
    a2 = num2
    ans = a1+a2
    print (a1,"+",a2,"=",ans)
def subs(num1,num2):
    a1 = num1
    a2 = num2
    ans = a1-a2
    print (a1,"-",a2,"=",ans)
def multi(num1,num2):
    a1 = num1
    a2 = num2
    ans = a1*a2
    print (a1,"X",a2,"=",ans)
def div(num1,num2):
    a1 = num1
    a2 = num2
    ans = a1/a2
    print (a1,"/",a2,"=",ans)
addition(x,y)
subs(x,y)
multi(x,y)
div(x,y)

