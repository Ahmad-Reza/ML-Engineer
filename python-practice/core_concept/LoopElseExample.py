# For loop with else
people = [{'name': 'John', 'age': 25},
          {'name': 'Jane', 'age': 22},
          {'name': 'Peter', 'age': 30},
          {'name': 'Jenifer', 'age': 28}]

print(f'People: {people}')

name = input('Enter search name: ')
for person in people:
    if person['name'] == name:
        print(f'{person}')
        break
else :
    print(f'{name} is not found')

# While loop with else
basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10}
]

fruit_name = input('Enter the fruit name: ')

index = 0
while index < len(basket) :
    fruit = basket[index]
    if (fruit['fruit'] == fruit_name) :
        print(f"The basket has {fruit['qty']} {fruit_name}(s)")
        break

    index += 1
else :
    qty = int(input(f'Enter the {fruit_name} quantity: '))
    basket.append({'fruit': fruit_name, 'qty': qty})
    print(f'Basket: {basket}')