class Student:
    a =10
    def __init__(self):
        print(self.a)
        print(Student.a)
        Student.c = 50
    
    # @classmethod
    # def clas_mat(cls):
    #     cls.a=30
    #     Student.b=20
    #     print(cls.a)
    #     print(Student.a)
        
    # @staticmethod
    # def sts_mat(x,y):
    #     z= x+y
    #     print(z)
    #     Student.f=90
        
# print(Student.__dict__)
s1= Student()
# print(Student.__dict__)

# Student.e=60
# s1.clas_mat()
# Student.clas_mat()
# print(Student.__dict__)
# s1.sts_mat(2,3)
# print(Student.__dict__)


# s1= Student()
# s1.clas_mat()
# print(Student.__dict__)
# Student.sts_mat(2,3)

print(s1.a)

