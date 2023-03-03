#Create a class MCAS1 using the get method and enter their name roll number . Create a subclass Test, enter the mark details, calculate the percentage and also display their grades
class MCAS1:
    def getting(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self):
        print("Name ::",self.name)
        print("Roll no ::",self.roll)
class tester(MCAS1):
    def readMark(self):
        m1 = int(input("Enter ADS Mark"))
        m2 = int(input("Enter ASE Mark"))
        m3 = int(input("Enter DFCA Mark"))
        m4 = int(input("Enter MFC Mark"))
        total = m1+m2+m3+m4
        self.pec = total/400*100
    def dismark(self):
         print("Percentage of ",self.pec)
        
obj = tester()
obj.getting("jk",101)
obj.readMark()
obj.display()
obj.dismark()
