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