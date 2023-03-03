# Create a class student, display the MCA Students list(name of the students) by merging two
# lists MCAS1 and MCAS3.
# A. Insert a student in MCAS1
# B. Sort the students in MCAS1 and MCAS3
# C. Search for the student in MCAS3
class student:
    mcaS1 = []
    mcaS3 = []
    def __init__(self):
        self.mcaS1 = ["adil","arjun","ajay"]
        self.mcaS3 = ["john","Ely","jose"]
    def insert(self):
        n = int(input("How many students to be added To MCA S1 : "))
        for i in range(n):
            self.mcaS1.append(input("Enter the name of the student:"))
    def sort(self):
        self.mcaS1.sort()
        self.mcaS3.sort()
    def search(self):
        if input("Enter the name of the student:") in self.mcaS3 or self.mcaS1:
            print("Student found")
        else:
            print("Student not found")
    def display(self):
        print("MCA S1:",self.mcaS1)
        print("MCA S3:",self.mcaS3)

obj = student()

while True:
    print("1. Insert")
    print("2. Sort")
    print("3. Search")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.insert()
    elif choice == 2:
        obj.sort()
    elif choice == 3:
        obj.search()
    elif choice == 4:
        obj.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
