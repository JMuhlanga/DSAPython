# Hash Tables in Python

my_empty_dictionary = {}

my_menu = {
    'lasagna': 14.75,
    'moussaka': 21.15,
    'sushi':16.05
}

print(my_menu['sushi'])

# Response if key does not exist, using the get method
print(my_menu.get('paella'))

# To get all items of a dictionary we use the items method
print(my_menu.items())

# To get all keys
print(my_menu.keys())

# To add a new key value pair to our dictionary
my_menu['samosas'] = 13
print(my_menu.items())

# To modify the value of a particular key
print(my_menu.get('sushi'))
my_menu['sushi'] = 20
print(my_menu.get('sushi'))

# To delete a dictionary completely
 # del my_menu

# To delete a specific item
del my_menu['lasagna']
print(my_menu.items())

# Iterating items in a dictionary
for key, value in my_menu.items():
    print(f"\nkey:{key} ")
    print(f"value:{value} ")

# Iterating over the keys or the values
## Iterating over the keys
for dish in my_menu:
    print(dish)

## Iterating over the values
for prices in my_menu.values():
    print(prices)

# Clearing a dictionary
my_menu.clear()
print(my_menu.items())

# Nested dictionary
my_menu = {
    'sushi':{
        'price':19.25,
        'best_served': 'cold'
    },
    'paella':{
        'price':15,
        'best_served': 'hot'
    }
}

print(my_menu.items())