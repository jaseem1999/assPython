#prime no
n=int(input("Enter a number:"))
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
prime(n)