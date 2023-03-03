lis1 =[]
list2 =[]
list3 =[]
num = int(input("Enter the number :: "));
list1= [i for i in range(1,num)]
list2 = [i for i in list1 if i % 2 == 1]
list3 = [i for i in list1 if i % 7 != 0]
print("List :: ",list1)
print("List Odd :: ",list2)
print("List not divisble by 7 :: ",list3)
