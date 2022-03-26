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
