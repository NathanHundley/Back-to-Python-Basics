##############################################################
##Playing with Dictionaries
##############################################################

##Creating a basic dictionary

jon_info = {'age': 27, 'gender':'male'}

print(jon_info['age'])
print(jon_info['gender'])

#Pulling data from a dictionary

participant_ages = jon_info['age']

print(f"The age of the participant is {participant_ages}.")

#Adding key:value pairs to a dictionary

jon_info['height'] = 68
jon_info['weight'] = 165

print(jon_info)


##Starting with an empty dictionary

jane_info = {}

jane_info['age'] = 26
jane_info['gender'] = "female"
jane_info['height'] = 62
jane_info['weight'] = 115

print(jane_info)

#Changing dictionary values

jon_info['height'] = 72

print(f"Jon's correct height is {jon_info['height']} inches.")

#Removing key-value pairs

del jon_info['weight']
del jane_info['weight']

print(jon_info)
print(jane_info)

#Using get() command to access data for when there is no key

participant_weight = jon_info.get('weight','No weight available.')

print(participant_weight)


##############################################################
##Looping through Dictionaries
##############################################################

##Looping through all key-value pairs

for key, value in jon_info.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

##Looping through all keys

for info in jane_info.keys():
    print(f"\n{info.title()} information available about Jane.")

#Looping through keys in specific order

for info in sorted(jane_info.keys()):
    print(f"\n{info.title()} information available about Jane.")

##Looping through all values

comments = {"Jon":"I liked the movie.", "Jane":"The movie was derivative."}

print("The following comments were made about the movie:")
for comment in comments.values():
    print(f"\n\t{comment}")


##Nesting

#List of dictionaires, creating a list of 30 dictionaries

enemies = []

for enemy_number in range(30):
    new_enemy = {'race':'human', 'str':10, 'con':8, 'dex':6, 'cha':8, 'wis':4,
    'int':7}
    enemies.append(new_enemy)

for enemy in enemies[:5]:
    print(enemy)
print("...")

print(f"Total number of enemies: {len(enemies)}.")

#Editing part of the list of dictionaries

for enemy in enemies[:5]:
    if enemy['race'] == 'human':
        enemy['race'] = 'orc'
        enemy['str'] = 12
        enemy['con'] = 10
        enemy['dex'] = 5
        enemy['cha'] = 4
        enemy['wis'] = 7
        enemy['int'] = 5

for enemy in enemies[:10]:
    print(enemy)
print("...")

print(f"Total number of enemies: {len(enemies)}.") 


##A list in a dictionary

pizza = {'crust':'thin', 'toppings':['chicken','jalapheno','onion'],}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


##Dictionary in a dictionary

users = {
'aeinstein':{'first':'albert', 'last':'einstein', 'location':'princeton',},
'mcurie':{'first':'marie', 'last':'curie', 'location':'paris'},}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    