#With your Student class, make modifications for the class to accept the student’s current class (as in a classroom) on creation.
#Then add a method that takes 3 test scores and calculates the student’s average test score

class Student:
    def __init__(self, first, last, age, classroom):
        self.first = first
        self.last = last
        self.age = age
        self.classroom = classroom
        self.grade_scores = []

    def fullName(self):
        return(self.first + " " + self.last)

    def fullDescription(self):
        return("Name: " + self.first + " " + self.last + "\nAge: " + self.age + "\nClassroom: Year " + self.classroom)

    def average_grades(self):
        return



student_1_first_name_input = input("[Student 1] What is your first name?: ")
student_1_last_name_input = input("[Student 1] What is your last name?: ")
student_1_age_input = input("[Student 1] How old are you?: ")
student_1_clasroom_input = input ("What is your clasroom year?: ")


student_1 = Student(student_1_first_name_input, student_1_last_name_input, student_1_age_input, student_1_clasroom_input)

print(f"{student_1.fullDescription()}\nHas been added to the system.")

