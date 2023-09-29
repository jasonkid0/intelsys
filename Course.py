import Student

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    
s1 = Student("Jason", 19, 95)
s1 = Student("Jisun", 19, 75)
s1 = Student("Japong", 19, 65)