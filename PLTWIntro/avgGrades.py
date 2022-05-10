'''
Ben Cambell
3rd period
Average grades
User inputs grade and program returns their average
'''
#List of grades from user
grades = []

#Loop for grades to be inputed
while(True):
  #Get input as int
  userIn = int(input("Input a grade or -1 to stop:"))
  #Break condition for -1
  if userIn == -1: break
  #Add grade to list
  grades.append(userIn)
  #Print current grades
  print("Current grades:", *grades)

#After loop is broken print the average of the grades
print("Average grade is: ", sum(grades)/len(grades))
