class Employee:
    name = ''
    salary = 0
    def display_name(self, name, salary):
        self.name = name
        self.salary = salary
        print(name)
        print(salary)


e = Employee()

e.display_name("John", 1000)
e.display_name("Mary", 2000)
e.display_name("David", 3000)
