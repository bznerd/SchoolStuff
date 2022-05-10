'''
Ben Campbell
3rd Period
Semester grades
Weighted semester average
'''
#store grades in dictionary and associated weights in another
grades = {"Quarter 1": 0, "Quater 2": 0, "Final": 0}
weights = {"Quarter 1": .4, "Quater 2": .4, "Final": .2}

#iterate through dictionary of grades and get user grades
for grade in grades:
  grades[grade] = float(input("What was your %s grade?" % grade))

#iterate through grades and add their weighted sums to avg variable
avg = 0
for weight in weights:
  avg += grades[weight]*weights[weight]

#print average
print("Your average grade was a %1.0f" % avg)

#print letter grade with chained conditional
if(avg >= 90):
  print("You got an A")
elif(avg >= 80):
  print("You got a B")
elif(avg >= 70):
  print("You got a C")
elif(avg >= 60):
  print("You got a D")
else:
  print("Yout got a F")
