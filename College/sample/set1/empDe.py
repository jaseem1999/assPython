# Create a class employee use the concept dictionary.-
# A. display the empid and name
# B. insert an employee
# C. delete an employee
# D. sort the order
# E. search for an employee
class employee:
    emp = {}
    def __init__(self):
        self.emp = {1:"adil",2:"arjun",3:"ajay"}
    def insert(self):
        self.emp[int(input("Enter the empid:"))] = input("Enter the name of the employee:")
    def delete(self):
        del self.emp[int(input("Enter the empid:"))]
    def sort(self):
        self.emp = sorted(self.emp.items())
    def search(self):
        if int(input("Enter the empid:")) in self.emp:
            print("Employee found")
        else:
            print("Employee not found")
    def display(self):
        print("Employee:",self.emp)
    
obj = employee()

while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Sort")
    print("4. Search")
    print("5. Display")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.insert()
    elif choice == 2:
        obj.delete()
    elif choice == 3:
        obj.sort()
    elif choice == 4:
        obj.search()
    elif choice == 5:
        obj.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice")

