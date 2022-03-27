#Task 1
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    elif extra_cheese == "Y":
        bill += 1
    else:
        bill += 0
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    elif extra_cheese == "Y":
        bill += 1
    else:
        bill += 0
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    elif extra_cheese == "Y":
        bill += 1
    else:
         bill += 0

print(f"your final bill £{bill}. ")

#Task 2
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


#Task 3

number1 = int(input("Pick a number? "))
number2 = int(input("Pick a second number? "))
operation = input("Select a operation (plus, minus, times or divide)? ")

def operation1():
    if operation == "plus":
        print(number1 + number2)
    elif operation == "minus":
        print(number1 - number2)
    elif operation == "times":
        print(number1 * number2)
    elif operation == "divide":
        print(number1 / number2)
    else:
        print("Invalid input, please try again")

operation1()
