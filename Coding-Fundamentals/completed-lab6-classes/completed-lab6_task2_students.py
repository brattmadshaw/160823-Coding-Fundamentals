class Students:
    def __init__(self, name, age, class_="classroom"):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, score_1, score_2, score_3):
        x = (score_1 + score_2 + score_3) / 300 * 100
        return f"Average test score for {self.name} is {x}%"

student_1_name = input("Please enter your name: ")
student_1 = Students(student_1_name, 5)

score_result_1 = int(input("[1] Enter a score: "))
score_result_2 = int(input("[2] Enter a score: "))
score_result_3 = int(input("[3] Enter a score: "))

result = student_1.average_test_score(score_result_1, score_result_2, score_result_3)
print(result)
