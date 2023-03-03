# Create a class number and enter the list of n numbers in list1.Using the list comprehension
# concept create another list2 of even numbers, then create list3 of numbers not divisible by 3.

class Number:
    def __init__(self):
        self.list1 = [1,2,3,4,5,6,7,8,9,10]
        self.list2 = [i for i in self.list1 if i%2==0]
        self.list3 = [i for i in self.list1 if i%3!=0]
    def display(self):
        print("List1:",self.list1)
        print("List2:",self.list2)
        print("List3:",self.list3)
    
obj = Number()
obj.display()
