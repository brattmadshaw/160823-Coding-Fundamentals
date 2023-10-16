## level 1
#Less than 50 Fail 
#between 50..60 (inclusive) Pass 
#between 61..70 (inclusive) Merit 
#between 71..100 (inclusive) Distinction

## level 2
#Less than 40 Fail 
#between 40..50 (inclusive) Pass 
#between 51..65 (inclusive) Merit 
#between 66..100 (inclusive) Distinction

# create grades as dictionary 
grading_criteria = {
    1: {
        'Fail': (0, 49),
        'Pass': (50, 60),
        'Merit': (61, 70),
        'Distinction': (71, 100)
    },
    2: {
        'Fail': (0, 39),
        'Pass': (40, 50),
        'Merit': (51, 65),
        'Distinction': (66, 100)
    }
}

# create level_input as an array
level_array = [1, 2]

level_input = input("""please select your level:
      [1] Level 1:
      [2] Level 2:
""")

print(level_input)