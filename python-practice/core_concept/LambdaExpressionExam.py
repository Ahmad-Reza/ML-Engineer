# Syntax:
# lambda parameters: expression

# Without Lambda Expression 
def getFullName(firstName, lastName, formatter):
    return formatter(firstName, lastName)

def firstLast(firstName, lastName):
    return f"{firstName} {lastName}"

def lastFirst(firstName, lastName):
    return f"{lastName} {firstName}"

fullName = getFullName('Ahmad', 'Reza', firstLast) 
print(f'First and last name is {fullName}')

fullName = getFullName('Shahid', 'Reza', lastFirst)
print(f'First and last name is {fullName}')


# With Lambda Expression
firstLastName = getFullName('Ahmad', 'Reza', lambda firstName, lastName: f'{firstName} {lastName}')
print(f'Using LE : {firstLastName}')

lastFirstName = getFullName('Ahmad', 'Reza', lambda fn, ln: f"{ln} {fn}")
print(f"Last and first name is {lastFirstName}")

# Lambda in a Loop
callables = []
for index in (1, 2, 3):
    callables.append(lambda a= index: a)

for f in callables:
    print(f())


# Docstring example - used to create documentation and multiline comments
help(print)

def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns: 
        The sum of the two arguments
    """

    return a + b

help(add)
print(add(12, 55))

print(add.__doc__) # only print docstrring value
