subjects = ['English', 'Maths', 'IT']
marks = {}

# Input marks for each subject, modified code from lab3_task4_get_int
for subject in subjects:
    while True:
        mark_input = input(f"Please enter {subject} mark (between 0 and 100): ")
        mark = mark_input.isdigit() and 0 <= int(mark_input) <= 100

        if mark:
            marks[subject] = int(mark_input)
            break
        else:
            print("Invalid input. Please enter a valid integer between 0 and 100.")

average_mark = sum(marks.values()) / len(marks)

print("\nIndividual Marks:")
for subject, mark in marks.items():
    print(f"{subject}: {mark}")
    
print("\nAverage Mark: " + str(round(average_mark, 2)))
print("Overall Result: Pass" if average_mark >= 65 else "Overall Result: Fail")
