def factorial(num):
    fact = 1
    if num == 0:
        print("Number is 0 is 1 factorial")
    elif num<0:
        print("-ve Number")
    else:
        for i in range(1,num+1):
            fact = fact * i
        print("Factorial Number is ::",fact)


def countStr(str1):
    for i in str1:
        print("Character",i, "count of character", str1.count(i) )

while True:
    print("1. factorial Number::")
    print("2. Character Count::")
    print("3. Exit::")
    choise = int(input("Enter the choise ::"))
    if choise == 1:
        num =int(input("Enter a number"))
        factorial(num)
    elif choise == 2:
        str1= input("Enter a string")
        countStr(str1)
    elif choise == 3:
        break
    else:
        print("wrong choise")
