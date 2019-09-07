##############################################################
##Playing with Lists
##############################################################

##Creating a list

got_chars = ['Jon Snow', 'Khal Drogo', 'Jamie Lannister', 'Sansa Stark']

print(got_chars)


##Pulling data from lists

print("My favorite Game of Thrones characters are:\n\t",got_chars[0],"\n\t",
    got_chars[1],"\n\t",got_chars[2],"\n\t",got_chars[3])

print("My favorite Dothraki is ",got_chars[1])

print(got_chars[0].lower())


##Pulling data from reverse

print("My favorite Game of Thrones characters are:\n\t",got_chars[-1],"\n\t",
    got_chars[-2],"\n\t",got_chars[-3],"\n\t",got_chars[-4])


##Using values from a list

print(f"I wish {got_chars[1]} was still alive to fight the men in iron suits.")


##Changing values in a list

#Change values in place

print(f"I no longer like the Game of Thrones characters {got_chars[-1]} and ",
    f"{got_chars[0]}.")

got_chars[0] = "Tyrion Lannister"

got_chars[-1] = "Arya Stark"

print(f"My new favorite Game of Thrones characters are {got_chars[0]} and ",
    f"{got_chars[-1]}.")

#Add new values to the end of a list

got_chars.append("Grey Worm")

print(got_chars)

#Shifting values in a list

got_chars.insert(0, "Varys")

print(got_chars)

got_chars.insert(1, "Robert the Strong")

print(got_chars)

#Removing items from a list

del got_chars[0]

print(got_chars)

#Popping an item from a list to use in another list

dead_got_chars = []

dead_got_chars.append(got_chars.pop(0))
dead_got_chars.append(got_chars.pop(1))
dead_got_chars.append(got_chars.pop(1))
dead_got_chars.append(got_chars.pop(2))

print(f"The Game of Thrones characters still alive are {got_chars[0]} and ",
    f"{got_chars[1]}.\nThe dead characters are:\n\t{dead_got_chars[0]}\n\t",
    f"{dead_got_chars[1]}\n\t{dead_got_chars[2]}\n\t{dead_got_chars[3]}")

#Building a new list from scratch by adding values

places_in_westeros = []

places_in_westeros.append("Kings Landing")
places_in_westeros.append("Winterfell")
places_in_westeros.append("Castle Black")

print(places_in_westeros)

#Removing an item from a list based on value, but it only removes the 
#first occurence

places_in_westeros.remove("Kings Landing")

print(places_in_westeros)


##Organizing a List

#Sorting a list permanently by alphabetical order

mystical_creatures = ["Elves", "Dwarves", "Orcs", "Hobbits", "Giants"]

mystical_creatures.sort()

print(mystical_creatures)

#Sorting a list permanently by reverse alphabetical order

mystical_creatures.sort(reverse=True)

print(mystical_creatures)

#Temporary sorting

print("Here is the original order:")
print(mystical_creatures)

print("\nHere is the list sorted alphabetically:")
print(sorted(mystical_creatures))

print("\nHere is the original order again:")
print(mystical_creatures)

#Printing a list in reverse order

mystical_creatures = ["Elves", "Dwarves", "Orcs", "Hobbits", "Giants"]

print(mystical_creatures)

mystical_creatures.reverse()

print(mystical_creatures)

#Finding the length of a list

print(len(mystical_creatures))


##############################################################
##Working with Lists
##############################################################

##Looping through lists

board_games = ["catan", "zombicide", "chess", "scythe", "gloomhaven", 
"kingdom death: monster"]

for game in board_games:
    print(game)

##Using loops

for game in board_games:

    print(f"{game.title()} is a great game to play.")
    print(f"I can't wait to play {game.title()} again!\n")

print("Thank you for showing me those great games!")

#Using loops to print a range of numbers, python stops at the last number 
#it does not print it

for value in range(1,11):
    print(value)


##Using range function to make numerical lists

numbers = list(range(1,11))

print(numbers)

#Telling range to skip numbers

even_numbers = list(range(2,11,2))

print(even_numbers)

#Using loops to create lists of numbers that skip

squares = []

for value in range(2,11,2):

    square = value ** 2
    squares.append(square)

print(squares)

#More efficient version

squares = []

for value in range(2,11,2):

    squares.append(value ** 2)

print(squares)

#Slicing a list to print the first three items in the list

authors = ["brandon sanderson", "george rr martin", "joe ambercrombie", 
"anthony ryan", "dan brown"]

print(authors[0:3])

#Slicing a list to print all values up to the third in the list

print(authors[:3])

#Slicing a list print all values from the second to the last in the list

print(authors[1:])

#Looping through a slice

print("Here are some of my favorite authors:")

for author in authors[:3]:
    print(author.title())

#Copying a list completely

favorite_authors = authors[:]

print("The names of authors I know are:")
print(sorted(authors))

print("My favorite authors are:")
print(favorite_authors)


##############################################################
##Descriptives with Number Lists
##############################################################

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0]

print(min(digits))

print(max(digits))

print(sum(digits))


##############################################################
##List Comprehension
##############################################################

squares = [value**2 for value in range(1,11)]

print(squares)


##############################################################
##Understandng Tuples
##############################################################

#Tuples are lists that cannot change, in Python terms they are immutable

dimensions = (10, 20, 40, 80, 160)

print(dimensions[0])
print(dimensions[2])
print(dimensions[-1])

#Looping through a Tuple

for value in dimensions:
    print(value)

#Writing over a Tuple

dimensions = (5, 10, 20, 40, 50)

print("\n New dimensions:")

for value in dimensions:
    print(value)

