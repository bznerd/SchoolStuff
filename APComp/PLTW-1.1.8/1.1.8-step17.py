"""
Ben Campbell 9/22/22
1.1.8 Step 17
Loop through courses, request grades, display letter grade, allow redo
"""

my_courses = ["English", "Math", "CS"]

redo = "y"
#Program loop
while redo.upper() == "Y":
    #Loop over every course
    for course in my_courses:
        #Get course grade
        print()
        print("Enter your points for " + course)

        points = int(input("Points -> "))
        
        #Return letter grade
        if (points >= 90):
            print("A")
        elif (points >= 80):
            print("B")
        elif (points >= 70):
            print("C")
        elif (points >= 60):
            print("D")
        else:
            print("F")

    #Prompt for exit or go back to beginning of program
    redo = input("Do you need to re-do these grades? (y/n)")
