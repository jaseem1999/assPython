list_num = []
size = int(input("How many size you want enter"))
for i in range(0,size,1):
    num=int(input("Enter the number"))
    list_num.append(num)
print("Your List is ",list_num)
list_sum = []
sum = 0
for i in list_num:
    sum = sum + i
print("Sum of list ",sum)
