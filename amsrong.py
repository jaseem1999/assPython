#amstrong
def amstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if n==sum:
        print("Amstrong number")
    else:
        print("Not an Amstrong number")
n=int(input("Enter a number:"))
amstrong(n)