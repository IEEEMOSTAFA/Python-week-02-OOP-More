# class Student:
#     def __init__(self,name,current_class,id):
#         self.name = name
#         self.current_class = current_class
#         self.id = id

#     def __repr__(self) -> str:
#         return f'Student with name: {self.name}, class: {self.current_class},id: {self.id}'    

# class Teacher:
#     def __init__(self,name,subject,id):
#         self.name = name 
#         self.subject = subject
#         self.id = id

#     def __repr__(self) -> str:
#         return f'Teacher : {self.name}, subject:{self.subject}, id :{self.id}'    
# class School:
#     def __init__(self,name) -> None:
#         self.name = name
#         self.teachers = []
#         self.students = []

#     def add_teacher(self,name,subject): 
#         id = len(self.teachers) + 100
#         teacher = Teacher(name,subject,id)
#         self.teachers.append(teacher)

#     def enroll(self,name,fee):
#         if fee < 6500:
#             return 'not enough fee'
#         else:
#             id = len(self.students) + 1
#             student = Student(name,'c',id)
#             self.students.append(student)
#             return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

#     def __repr__(self) -> str:
#         print('welcome to ',self.name)
#         print('---------OUR Teachers-----------')
#         for teacher in self.teachers:
#             print(teacher)
#         print('-----------OUR STUDENTS---------')
#         for student in self.students:
#             print(student)
#         return 'All Done for now'    



# phitron = School('Phitron')
# phitron.enroll('alia',5200)
# phitron.enroll('rani',8000)
# phitron.enroll('Somapti',7000)
# phitron.enroll('vaijaan',9000)


# phitron.add_teacher('Tom Cruise', 'Algo')
# phitron.add_teacher('Decap', 'DS')
# phitron.add_teacher('AJ', 'Database')
# print(phitron)
#-------------------------------------------
class Stuedent:
    def __init__(self,name,current_class,id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return  f'Student name: {self.name},Class : {self.current_class},Id : {self.id}'
class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, Subject: {self.subject},id: {self.id}'    

class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []       
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
        
    def enroll(self,name,fee):
        if fee < 6500:
            return 'return not enough fee'
        else:
         id = len(self.students) + 1
        stuedent = Stuedent(name,'C',id)
        self.students.append(stuedent)

        return f'{name} is enroll with id {id},extra money {fee - 6500}'
    
    def __repr__(self) -> str:
        print('welcome to ',self.name)
        print('------------Our Teachers-----------')
        for teacher in self.teachers:
            print(teacher)
        print('-------------our Students------------')
        for student in self.students:
            print(student)
        return 'All Done For Now'
    

Phitron = School('Phitron')
Phitron.enroll('Jafir',7000)
Phitron.enroll('Mehraj',6500)
Phitron.enroll('Rafe',9000)

Phitron.add_teacher('Farhan Firoj','Basic C')
Phitron.add_teacher('Mahir Shahrier','Algo')
Phitron.add_teacher('Jankar','Python')

print(Phitron)


