##############################################################
##Playing with Functions
##############################################################

##Defining a Basic Function

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('Nathan')

#Positional arguments

def pizza_order(pizza, name):
    """Display information about a pizza order"""
    print(f"\n{name.title()} placed an order for a {pizza} pizza.")

pizza_order('cheese','nathan')

#Keyword arguments

pizza_order(name='nathan', pizza='chicken')

#Default values

def pizza_order(pizza, name="nathan"):
    """Display information about a pizza order"""
    print(f"\n{name.title()} placed an order for a {pizza} pizza.")

pizza_order('cheese')

#Returning values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

president = get_formatted_name('donald', 'trump')
print(president)

#Making an argument optional

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name('nathan', 'hundley')
print(name)

name2 = get_formatted_name('nathan', 'hundley', 'andrew')
print(name2)

#Returning a dictionary

def build_enemy(race, health, type=None):
    """Return a dictionary of information about an enemy."""
    enemy = {'race': race, 'health': int(health)}
    if type:
        enemy['class'] = type
    return enemy

monster = build_enemy('orc', 50, 'paladin')
print(monster)

monster2 = build_enemy('goblin', 20)
print(monster2)

#Using a function with a loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#Passing a list

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['nathan', 'sondos', 'franklin']

greet_users(usernames)

#Modifying a list in a function

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Preventing a function from modifying a list


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

#Passing an arbitrary number of arguments

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('cheese', 'chicken', 'onion')

#Mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(24, 'onion', 'chicken', 'olives', 'extra cheese')

#Using arbitrary keyword arguments

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
    location='princeton', field='physics')

print(user_profile)


##############################################################
##Storing Your Functions in Modules
##############################################################

##Importing an Entire Module

import pizza

pizza.make_pizza(16, 'sausage')
pizza.make_pizza(24, 'onion', 'jalapeno', 'tomato')

#pizza modeule is based on the make_pizza function created above and saved
#in the same directory as this file

#Importing specific functions
#follow the format, 'from module_name import function_name', or if you want
#to import multiple functions, 'from module_name import function_0, function_1,'

from pizza import make_pizza

#Using as to give a function an alias, 
#'from module_name import function_name as fn'

from pizza import make_pizza as mp

mp(18, 'extra cheese')
mp(24, 'chicken', 'extra cheese')

#Using as to give a module an alias

import pizza as president

p.make_pizza(18, 'plain')
p.make_pizza(16, 'chicken')

#Importing all functions in a module using an *

from pizza import *