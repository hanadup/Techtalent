# #Task 1
import random
randomno = random.randint(1,10)
name = input("Hello, What's your name?")
guess = int(input(f'hello ' + name + ' guess between 1-10? '))
if guess == randomno:
     print("That's correct")
else:
     print(f'that is incorrect the number was ' + str(randomno))

#Task 2
number = str(input("Hello, What's your favourite number between 1-100? "))
if number == str(1):
    print("How do you mmake number 1 disappear? You flush")
elif number == str(2):
    print("We should give number 2 credit as it became a prime number against all odds")
elif number == str(8):
    print("What did zer say to eight? Nice belt")
else:
    print("What is odd? Every alternate number!")

#Task 3

starter = input(("What is you favourite starter? "))
main_course = input(("What is you favourite main course? "))
dessert = input(("What is you favourite dessert? "))
drink = input(("What is you favourite drink? "))

print(f'Your favourite meal is {starter}, {main_course}, {dessert} and with a glass of {drink}.')

#Task 4
print ("Welcome to the depreciation calculator ")
Bike_price = 2000
age = int(input("How many years has it been since the bike was purchased? "))

def bike_loss():
    depreciation = Bike_price - (age * 200)
    while depreciation > 1000:
        if depreciation > 1000:
            depreciation -= 200
            print(str(depreciation))
        else:
            print(str(depreciation))
bike_loss()

#Task 5
