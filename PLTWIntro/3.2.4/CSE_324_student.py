from CSE_324_course import Course

class Student:
    
    student_id = 0
    echo_courses = False
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def __str__(self):
        courses = ""
        for course in self.courses:
            courses += str(course) + ", "
        return f"Name: {self.first_name} {self.last_name}, Courses: {courses[:-2]}, Student ID: {self.student_id}"
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id

    def get_courses_names(self):
        return [course.__str__() for course in self.courses]
    
    def add_course(self, new_course):
        self.courses.append(new_course)
        if(Student.echo_courses): print(f"{new_course.__str__()} added to {self.get_first_name()}'s registration")