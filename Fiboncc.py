n = int(input("Enter the number"))

for i in range(0,n,1):
    if i == 0 or i == 1:
        print(i)
    else:
        for x in range(i+1,n-1,1):
            a=i*x
            print
            print(a)
    
    
