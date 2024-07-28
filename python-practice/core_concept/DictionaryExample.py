# Dictionaries is also known as mapping or hash tables. 
# They are key values pairs the are guaranteed to retain order of insertion starting from python 3.7


my_dict = {'name': 'Ahmad Reza', 'age': 24, 'city': 'Noida'}
print(my_dict)
print(my_dict['name'])
print(len(my_dict))

print(list(my_dict.keys()))
print(list(my_dict.values()))
print(f'dictionary value - {list(my_dict.items())}')

my_dict['education'] = 'Bachelor degree'
print(f'updated dictionary - {my_dict}')

print(my_dict.get('age')) # or my_dict['age']

# Return None if the key doesn't exist 
print(my_dict.get('hobbies'))

# Return default (2nd param) if the key is not exist
print(my_dict.get('hobbies', "coding"))

# Remove key
del my_dict['education']
my_dict.pop('age')

print(f'New Dictionary - {my_dict}')

# Update the value
my_dict.update({'education': 'bachelor'})
my_dict.update({'Cool': True})
print(f'updated values - {my_dict}')

# Create a dictionary from a collection of key value pairs.
new_dict = dict([['name', 'Nishant'], ['age', 44], ['favourite dish', 'chicken']])
print(f'New Dictionary - {new_dict}')

# Create a dictionary from two collection
new_dict = dict(zip(['name','age','magic_power'],['Andrei',32, False]))
print(f'Another Dictionary - {new_dict}')

# Comprehension - concise way to create a new dictionary from an existing dictionary or other iterable.
# syntax - {key: value for variable in iterable}

compre_dict = {key: value for key, value in new_dict.items() if key == 'name'
                      or key == 'age'}
print(f'Comprehension Dict - {compre_dict}')

