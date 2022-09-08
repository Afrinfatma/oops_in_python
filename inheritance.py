class College:
    def __init__(self,college_dict):
        self.college_name=college_dict.get("college_name")
        self.college_website=college_dict.get("college_website")


class Student(College):
    def __init__(self, college_dict):
        super().__init__(college_dict)
        self.department_name=college_dict.get("department_name")

    def department_info(self):
        print("Student is studying in",self.department_name)

class Shifts(Student):
    def __init__(self,college_dict):
        super().__init__(college_dict)
        self.shift_type=college_dict.get("shift_type")


if __name__=="__main__":

    # student_object=Student({"college_name":"Vbu","college_website":"www.vbu.nic.in","department_name":"MCA","shift_type":"Morning"})
    # print(student_object)
    # student_object.department_info()

    student_object=Student({"college_name":"Vbu","college_website":"www.vbu.nic.in","department_name":"MCA","shift_type":"Morning"})
    print(student_object.college_name)
    print(student_object.college_website)
    print(student_object.department_info())
    print(student_object.department_name)