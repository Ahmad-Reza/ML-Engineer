# Function definition
def greet():
    """ Display a greeting to users """
    print('Hi, Good Morning') 

def sum(a, b):
    return a + b

# Function call
greet()
print(sum(10, 15))

# Default parameters
def greeting(name='there', message='Hi'):
    return f"{message} {name}"

print(greeting())

# Keyword arguments
returnValue = greeting('Ahmad', message='Hello')
print(returnValue)

def getNetPrice(price, tax = 0.07, discount = 0.05) :
    return price * (1 + tax - discount)

result = getNetPrice(12)
print(f'Result = {result}')

result1 = getNetPrice(15, discount = 0.5)
print(f'Result1 = {result1}')

result2 = getNetPrice(12, tax= 0.8, discount= 0.2)
print(f'Result2 = {result2}')

# Recursive Method
def sum(number) :
    if number > 0 : 
        return number + sum(number - 1)
    
    return 0 

result3 = sum(number=100)
print(f'Sum of 100 is = {result3}')

# Closures
# A nested function references a value of its enclosing function and then
# the enclosing function returns the nested function.

def get_multiplier(a):
    def out(b):
        return a * b
    return out

multiply_by_3 = get_multiplier(3)
print(multiply_by_3(10))

# If multiple nested functions within enclosing function reference the same value, that value gets shared.
# To dynamically access function's first free variable use 
# '<function>.__closure__[0].cell_contents'.

# Scope
# If variable is being assigned to anywhere in the scope, 
# it is regarded as a local variable, unless it is declared as a 'global' or a 'nonlocal'.

def get_counter():
    i = 0
    def out():
        nonlocal i
        i += 1
        return i
    return out

counter = get_counter()
print(f'{counter()}, {counter()}, {counter()}')