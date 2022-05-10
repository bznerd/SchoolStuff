userIn = input("What color is the light?").capitalize().strip().replace(' ','')
if(userIn == "Green"):
	print("Go")
elif(userIn == "Red"):
	print("Stop")
elif(userIn == "Yellow"):
	print("Slow down")
else:
	print("Not a color dumbfuck")