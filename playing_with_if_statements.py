##############################################################
##Playing with IF Statements
##############################################################

##Conditional IF example

cars = ["audi", "bmw", "toyota", "ford", "chevy"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# double = signs (==) check whether the value is True or False
# a not equal sign is !=

foods = ["cheeseburger", "pizza", "pasta salad", "grilled cheese"]

for food in foods:

    if food != "pizza":
        print(f"I would rather have pizza, not {food}!")

    else:
        print(f"Thank you for providing {food}. I am famished.")

#Numerical comparisons

answer = 13

if answer != 27:
    print(f"I am sorry, {answer} is not the correct answer. Please try again.")

#Other numericla comparisons

print(answer == 19)
print(answer < 15)
print(answer > 10)
print(answer <= 11)

#Checking multiple conditions

age = 18
gender = "male"

print(age >= 18 and gender == "female")
print(age >= 18 and gender == "male")

print(age > 21 or gender =="female")
print(age > 21 or gender == "male")


##Checking whether a value is in a list

ingredients = ["cheese", "bacon", "lettuce", "bread", "pickle", "mayo"]

print("bacon" in ingredients)
print("pork" in ingredients)

##Checking whether a vlue is not in a list

ingredient = "onion"

if ingredient not in ingredients:
    print(f"Please add {ingredient} to my order.")


##Boolean Expressions

status = True

if status == True:
    print("Changes cannot currently be made.") 


##IF/ELSE Statements

participant_ages = list(range(12,24))

for age in participant_ages:
    if age >= 18:
        print(f"The participant is {age} years old, they are approved.\n")
    else:
        print(f"The participant is {age} years old, they are not approved.\n")


##IF/ELIF/ELSE Statements
#You can omit the last else and use another elif for more specifcity if needed

for age in participant_ages:
    if age < 16:
        print(f"You are only {age} years old. I am sorry you are too young.\n")
    elif age < 18:
        print(f"You are {age} years old. You can come compete.\n")
    else:
        print(f"You are {age} years old. You are too old to compete, sorry.\n")


##Testing multiple conditions

order = ["fries", "salad", "hamburger"]

if "fries" in order:
    print("Fries are being cooked.")
if "hamburger" in order:
    print("Hamburger is being cooked.")
if "chili" in order:
    print("Chili being made.")
if "salad" in order:
    print("Salad being made.")
if "milkshake" in order:
    print("Milkshake being made.")

print("\nOrder complete and ready for pickup.")


##Using IF statements with lists to check for special items

personality_scales = ["openness", "conscientiousness", "extraversion", 
"agreeableness", "neuroticism"]

for scale in personality_scales:
    print(f"{scale.title()} is part of the 'Big Five'.\n")

for scale in personality_scales:
    if scale == "neuroticism":
        print(f"{scale.title()} is not part of the profile. Do not use.\n")
    else:
        print(f"{scale.title()} is part of the profile. Please use.\n")

#Check that a list is not empty

toppings = []

if toppings:
    for topping in toppings:
        print(f"{topping.title()} being included in the order.")
else:
    print("Are you sure you would like to add nothing extra to the order?")

#Checking multiple lists

stark_members = ["jon snow", "bran", "sansa", "ghost", "arya"]

lannister_members = ["cersei", "tyrion", "jaime"]

other_members = ['grey worm', 'sir jorah', 'podrick', 'jon snow', 'tyrion']

for member in other_members:
    if member in stark_members:
        print(f"{member.title()} is part of House Stark.\n")
    elif member in lannister_members:
        print(f"{member.title()} is part of House Lannister.\n")
    else:
        print(f"{member.title()} is not part of House Stark or Lannister.\n")