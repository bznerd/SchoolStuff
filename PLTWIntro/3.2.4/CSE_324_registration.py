from CSE_324_course import Course
from CSE_324_student import Student

Student.echo_courses = True

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
art_hist = Course("Art History")
art = Course("Creative Art I")




test_student = Student("Jill", "Sample")

test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)


test_student2 = Student("Bill", "Sample")

test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("James", "Smith")

test_student3.add_course(art)
test_student3.add_course(art_hist)
test_student3.add_course(math)
test_student3.add_course(language)

students = [test_student, test_student2, test_student3]

print("\nStudents are:", *[student.get_first_name() + " " + student.get_last_name() for student in students], "\n")

for student in students:
    print(f"Student name: {student.get_first_name()} {student.get_last_name()}, ID: {student.get_student_id()}")
    print("Student courses: ", *student.get_courses_names(),"\n")