grade = int(input("Enter your grade: "))

if grade >= 71:
    print("You have scored", grade, "and achieved a distinction")
elif grade >= 61:
    print("You have scored", grade, "and achieved a merit")
elif grade >= 50:
    print("You have scored", grade, "and achieved a pass")
else:
    print("You have scored a total score of", grade,"this is", 50 - grade, "below the pass rate and you unfortunotely failed the test")
