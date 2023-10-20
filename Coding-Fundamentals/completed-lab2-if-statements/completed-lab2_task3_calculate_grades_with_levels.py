# integer input variables
level_input = int(input("""please select your level:
[1] Level 1:
[2] Level 2:
Please select: """))
grade = int(input("Enter your grade: "))


## nested if statements

if level_input == 1:
    if grade >= 71:
        print("You have scored", grade, "and achieved a distinction")
    elif grade >= 61:
        print("You have scored", grade, "and achieved a merit")
    elif grade >= 50:
        print("You have scored", grade, "and achieved a pass")
    else:
        print("You have scored a total score of", grade,"this is", 50 - grade, "below the pass rate and you unfortunotely failed the test")
else:
    if grade >= 66:
        print("You have scored", grade, "and achieved a distinction")
    elif grade >= 51:
        print("You have scored", grade, "and achieved a merit")
    elif grade >= 40:
        print("You have scored", grade, "and achieved a pass")
    else:
        print("You have scored a total score of", grade,"this is", 40 - grade, "below the pass rate and you unfortunotely failed the test")