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

#numpy Task 1

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(array)

#numpy Task 2

import numpy as np
array = np.ones((3, 3, 3))

print(array)

#numpy Task 3

import numpy as np
array = np.arange(10)
print(array[1::2])

#numpy Task 4

import numpy as np
array = np.arange(10)
array[1::2] = -1
print(array)

#numpy Task 5

import numpy as np
array = np.arange(8)
a = np.reshape(array,(2,4))
print(a)

#numpy Task 6

a = np.arrange(1, 5).reshape(2,2)
b = np.arrange(6, 10).reshape(2,2)
c = np.dot(a, b)
print(c)
d = np.sum(c, axis = 1)
print(d)

