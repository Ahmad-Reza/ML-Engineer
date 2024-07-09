language = ['Python', 'Type Script', 'kotlin', 'java']
print(f'Prgraming Language - {language}')

numbers = [1, 2, 3, 6, 8, 9]
coordinates = [[0, 0], [100, 100], [200, 200]]

print(coordinates)
print(f'First index value - {coordinates[0]}')
print(f'Last index value - {coordinates[-1]}')

print(f'Numbers - {numbers}')
print(f'Modify Value - {numbers[1]*12}')

numbers.append(11)
print(f'Numbers with new added Value - {numbers}')

numbers.insert(2, 77)
print(f'Numbers with insert value - {numbers}')

del numbers[2]
print(f'Numbers after 2 index deleted - {numbers}')

last = numbers.pop()
print(f'pop value - {last}')
print(numbers)

second = numbers.pop(1)
print(f'pop value - {second}')
print(numbers)

numbers.remove(9)
print(f'Numbers after remove 9 - {numbers}')




