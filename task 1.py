# #Task 1
import random
randomno = random.randint(1,10)
name = input("Hello, What's your name?")
guess = int(input(f'hello ' + name + ' guess between 1-10? '))
if guess == randomno:
     print("That's correct")
else:
     print(f'that is incorrect the number was ' + str(randomno))
