#Task 1
new_file = open("Number_file.txt", "w")
new_file.write("3" + "\n" + "45" + "\n" + "83" + "\n" + "21" + "\n")
new_file.close()

#Task 2
score = int(input("What was the score of the test you have taken? "))

def mark_grade():
    if 20 <= score <= 29:
        print ("Your grade is D")
    elif 30 <= score <= 49:
        print ("Your grade is C")
    elif 50 <= score <= 69:
        print("Your grade is B")
    elif 70 <= score <= 100:
        print("Your grade is A")
    elif score < 20:
        print(" Your grade is F")
    else:
        print("Please try again score inputted was incorrect.")

mark_grade()
