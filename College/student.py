class Student:
    def __init__(self,std_id,std_name):
        self.std_id = std_id
        self.std_name = std_name
    def studentDisplay(self):
        print("Student ID ::",self.std_id)
        print("Student Name ::",self.std_name)
class Grade(Student):
    def __init__(self,std_id,std_name):
        Student.__init__(self,std_id,std_name)
    def mark(self,m1,m2,m3,m4):
        total = m1+m2+m3+m4
        pr = total/400*100
        if pr> 40:
            print("PASS ::",pr,"%")
            print("PASS :: Mark :: ",total)
        else:
            print("FAILED ::",pr,"%")
            print("FAILED :: Mark :: ",total)
obj = Grade(1010,"jk")
obj.studentDisplay()
obj.mark(40,40,40,38)
