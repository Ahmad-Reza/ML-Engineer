# Print program
print('Hello World')

# Input from terminal
value = input('Enter a value:')
print(value)

# Get multiple input values
price = input('Enter the price ($): ') 
tax = input('Enter the tax (%): ')

# Error: can't multiply sequence by non-int of type 'str'
# result = price * tax / 100

# Type converstation 
result = int(price) * int(tax) / 100
print(f'The Price is ${result}')

# if, if else statement
age = input('Enter your age')

if int(age) >= 18:
    print("You are eligible to vote.")
    print("Let's go to vote")
else: 
    print("You are not eligible to vote")

yourAge = int(age)
if yourAge < 5:
    ticketPrice = 5
elif yourAge < 16:
    ticketPrice = 10
else:
    ticketPrice = 18

print(f'you will pay ${ticketPrice} for the ticket')

# Ternary operator
ticket_price = 20 if yourAge >= 18 else 10
print(f'Ticket price is - ${ticket_price}')

# For Loop example 
for index in range(5):
    print(index, end=" ")
print()

for index in range(2, 15):
    print(index, end=" ")
print()

for index in range(1, 15, 2):
    print(index, end=" ")
print()

# While Loop example 
command = ''
print(type(command))
while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")

# Break, Continue, and Pass keywords
print('-- Help: type quit to exit --')
while True:
    color = input('Enter your favorite color: ')
    if color.lower() == 'quit':
        print('-- Help: type quit to exit --')
        break

for index in  range(10):
    if index % 2 == 0:
        continue
    print(index)

counter = 1
max = 10
if counter <= max:
    counter += 1
else:
    pass # pass statement does nothing just to create a placeholder for the code that you'll implement later
