# Create a class and insert 10 vegetables and fruits in a list. Sort the list , search for a particular fruit. Update the dictionary with the total number of vowels found in each item of the list

class veg:
    def __init__(self):
        self.list1 = ["apple","orange","banana","mango","grapes","pineapple","watermelon","guava","kiwi","papaya"]
        self.list2 = dict()
        self.list2 = {0 : 'a'} 
    def sort(self):
        self.list1.sort()
    def search(self):
        if input("Enter the name of the fruit:") in self.list1:
            print("Fruit found")
        else:
            print("Fruit not found")
    def update(self):
        vowels = 0
        n= 1
        for i in self.list1:
            for j in i:
                if j in "aeiou":
                    self.list2[n] = j
                    n+1
                   
                    
    def display(self):
        print("List:",self.list1)
        print("Dictionary vowels :",self.list2)

obj = veg()

while True:
    print("1. Sort")
    print("2. Search")
    print("3. Update")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.sort()
    elif choice == 2:
        obj.search()
    elif choice == 3:
        obj.update()
    elif choice == 4:
        obj.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

