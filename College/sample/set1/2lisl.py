# Create a class Checker in this class enter 2 lists of integers.
# A. Whether list are of same length
# B. Whether list sums to same value
# C. Whether any value occur in both

class Checker:
    def __init__(self):
        self.list1 = [ 1, 2, 3, 4, 5]
        self.list2 = [ 1, 2, 3, 4, 5]
    def length(self):
        if len(self.list1) == len(self.list2):
            print("Both lists are of same length")
        else:
            print("Both lists are not of same length")
    def sum(self):
        if sum(self.list1) == sum(self.list2):
            print("Both lists sums to same value")
        else:
            print("Both lists sums to different value")
    def value(self):
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    print("The value",i,"occurs in both lists")
                    break
                else:
                    print("The value",i,"does not occur in both lists")
                    break
    def display(self):
        print("List1:",self.list1)
        print("List2:",self.list2)

obj = Checker()

while True:
    print("1. Length")
    print("2. Sum")
    print("3. Value")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.length()
    elif choice == 2:
        obj.sum()
    elif choice == 3:
        obj.value()
    elif choice == 4:
        obj.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

