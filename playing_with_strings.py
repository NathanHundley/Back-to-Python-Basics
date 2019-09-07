####Playing with Strings

##############################################################
##Creating text string
##############################################################

message = "Hello World! My name is Bobby the AI, and I don't like brussel sprouts."
print(message)

##Changing strings

#Capitalize the first letter of each word

print(message.title())

#Print all letters as uppercase

print(message.upper())

#Print all letters as lowercase

print(message.lower())


##############################################################
##Using variables in strings
##############################################################

#Create variables with strings

first_name = "Bobby"
last_name = "Joe"
full_name = f"{first_name} {last_name}"
print(full_name)

#Further combinations to play with

print(f"Hello, {full_name}!")

print(f"Hello, {full_name.upper()}!")

message_2 = f"Hello, {full_name.lower()}!"

print(message_2)

#Adding tabs

message_3 = "\tHello!"

print(message_3)

#Adding new lines

message_4 = "I know three programming languages:\nPython\nR\nSQL"

print(message_4)

#Combining tabs and new lines

message_5 = "I know three programming languages:\n\tPython\n\tR\n\tSQL"

print(message_5)

#Stripping whitespace from right side

message_6 ="Game of Thrones  "

print(message_6)

print(message_6.rstrip())

#Stripping whitespace from left side

message_7 ="  Game of Thrones"

print(message_7)

print(message_7.lstrip())

#Stripping whitespace from both sides

message_8 ="   Game of Thrones   "

print(message_8)

print(message_8.strip())