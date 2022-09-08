class College:
    def __init__(self):
        self.college_name="St.Columba's college"
        self.college_website="www.columba's.co.in"
    def get_info(self):
        print("The college name is ",self.college_name,"and website is :",self.college_website)

class Department:
    def __init__(self):
        self.department_name="MCA"

    def get_dept_info(self):
        print("The department name is ",self.department_name)

class Student(College,Department):
    def __init__(self):

        College.__init__(self)
        Department.__init__(self)

    def get_student_info(self):
        print("The student is studying in : ", self.college_name)
        print("The student is in department ", self.department_name)
        print("The student can search on this link ", self.college_website)

student_object=Student()
print(student_object.get_student_info())
print(student_object.department_name)
