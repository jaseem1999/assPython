class company:
    name = input("Enter your name:: ")
    emCode= int(input("Enter the employee id"))
    salary = int(input("Enter your salary"))
    total = 0
    if salary < 20000:
        total = salary+ (salary*10/100)+1000
    elif(salary > 20000 and salary < 30000):
        total = salary+ (salary*12/100)+1000
    else:
        total = salary+ (salary*15/100)+1000
    print("total salary ::",total)
obj = company()
