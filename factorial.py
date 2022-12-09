num = int(input("Enter the number "))
list_n = []
fa = 0
for i in range(1,num,1):
    list_n.append(i)
for i in list_n:
    fa = i * i
print(fa)
