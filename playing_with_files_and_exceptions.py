##############################################################
##Playing with Files
##############################################################

##Reading from a File

#Reading an entire file

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

#Reading line by line

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#Making a list of lines from a file

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#Working with a file's contents

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#Working with large files

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

#Is your birthday in the first million digits of pi?

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday=input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


##Writing to a File

#Writing to an empty file
#'w' opens the file in write mode, 'r' in read only mode, 'a' in append mode
# and 'r+' in read and write mode

filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

#Writing multiple lines

filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("Programming is cool.\n")

#Appending to a file

filename = "programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("I wish I started programming earlier in life.\n")
    file_object.write("Programming is the future.\n")


##############################################################
##Playing with Exceptions
##############################################################

#Handling ZeroDivisionError exception

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#Using exceptions to prevent crashes

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

#Handling FileNotFoundError exception

filename = 'complete_chronicles_of_bob.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

#Failing silently

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'complete_chronicles_of_bob.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)


##############################################################
##Analyzing Text
##############################################################

filename = 'alice.txt'

try:
    with open(filename, encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

#Working with multiple files

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)


##############################################################
##Storing Data
##############################################################

#Using json.dump() to store data

import json

numbers = [2, 3, 5, 6, 7, 9, 13]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

#Using json.load() to load data

import json

filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)

#Saving user-generated data

import json

username = input("What is your name? ")

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

#Reading user-generated data

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

#Saving and reading user-generated data

import json

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")


##Refactoring
#Cleaning code to make it more efficient
#Example

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()