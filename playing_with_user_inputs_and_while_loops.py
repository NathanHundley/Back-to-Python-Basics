##############################################################
##Playing with User Inputs
##############################################################

message = input("Tell me something and I will repeat it back to you: ")
print(message)

#When using input function make sure to include some form of prompt
#Writing clear prompts

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(f"\n Hello, {name}!")

#Accepting numerical inputs

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")

#Using the modulo operator that reports the remainder

print(5 % 3)
print (6 % 3)
print (7 % 3)

number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


##############################################################
##Playing with While Loops
##############################################################

#Example while loop

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Using while loop with user defined quit call

prompt = "\nTell me somehting, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#Using a flag

prompt = "\nTell me somehting, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#Using a break to exit a loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()}!")

#Using a continue in a loop for finding odd numbers from 1 through 10

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


##Using a While Loop with Lists and Dictionaries

#Moving items from one list to another

unconfirmed_users = ['bob', 'frankline', 'stephen', 'josh', 'nathan']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing all instences of specific values from a list

toppings = ['onion', 'cheese', 'chicken', 'onion', 'anchovie', 'peppers']
print(toppings)

while 'onion' in toppings:
    toppings.remove('onion')

print(toppings)

#Filling a dictionary with user input

responses = {}

active = True

while active:

    name = input("\nWhat is your name? ")
    response = input("What is your favorite type of pet? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        active = False

print("\n--- Results ---")
for name, pet in responses.items():
    print(f"{name} would like to own a {pet}.")


