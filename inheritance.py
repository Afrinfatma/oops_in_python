class College:
    college_name= "Vinoba Bhave University"
    college_wbsite="www.vbu.co.in"

    def get_info(self):
        print("all your information about ",self.college_name ,"present on coIlege website ",self.college_wbsite)

class Student(College):
    def __init__(self, department_name):
        self.department_name=department_name

    def department_info(self):
        print("Student is studying in",self.department_name)

if __name__=="__main__":

    student_object=Student("Mca")
    student_object.department_info()
