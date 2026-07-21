class Student:
    def __init__(self, student_name, student_id, course, marks):
        self.student_name = student_name
        self.student_id = student_id
        self.course = course
        self.marks = marks

    def display_details(self):
        print("Student Details")
        print("----------------")
        print("Name:", self.student_name)
        print("ID:", self.student_id)
        print("Course:", self.course)
        print("Marks:", self.marks)

    def add_marks(self, extra_marks):
        self.marks += extra_marks
        print("Marks updated successfully!\n")

    def check_result(self):
        if self.marks >= 50:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Create Student 1
student1 = Student("Ali", "A101", "Computer Science", 75)

# Create Student 2
student2 = Student("Siti", "A102", "Software Engineering", 25)

# Display Student Details
student1.display_details()
student1.check_result()
print()

student2.display_details()
student2.check_result()

# Add marks to student2
student2.add_marks(15)

# Display updated information
student2.display_details()
student2.check_result()
