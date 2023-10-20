#Create a Student class that takes the name and age on creation.
#Create 2 objects of your student class and get the age of one of them.
class Student:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def fullName(self):
        return(self.first + " " + self.last)
    

student_1_first_name_input = input("[Student 1] What is your first name?: ")
student_1_last_name_input = input("[Student 1] What is your last name?: ")
student_1_age_input = input("[Student 1] and finally, how old are you?: ")

student_2_first_name_input = input("[Student 2] What is your first name?: ")
student_2_last_name_input = input("[Student 2] What is your last name?: ")
student_2_age_input = input("[Student 2] and finally, how old are you?: ")


student_1 = Student(student_1_first_name_input, student_1_last_name_input, student_1_age_input)
student_2 = Student(student_2_first_name_input, student_2_last_name_input, student_2_age_input)

print(f"Welcome {student_1.fullName()}, {student_1_age_input} years of age. \n You have now been added to the system.")
print(f"Welcome {student_2.fullName()}, {student_2_age_input} years of age. \n You have now been added to the system.")

