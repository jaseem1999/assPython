class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display1(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
class student(person):
    def __init__(self, name, age, rollno, marks):
        person.__init__(self, name, age)
        self.rollno = rollno
        self.marks = marks
    def display(self):
        print("Rollno: ", self.rollno)
        print("Marks: ", self.marks)

object1 = student("Arjun", 20, 1, 100)
object1.display()
object1.display1()
