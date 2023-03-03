def prime1(n):
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
def feb(n):
    a,b = 0,1
    while a < n:
        print(a)
        a,b = b,a+b
    print()

while True:
    print("1. Prime number")
    print("2. Fabinnoc series")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter the number : "))
        prime1(num)
    elif choice == 2:
        num = int(input("Enter the number : "))
        feb(num)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
