# List Sort()
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']

guests.sort()
print(f'Names in Sorted Order: {guests}')

guests.sort(reverse=True)
print(f'Names in Sorted Order: {guests} \n')


# Sort() method to sort a list of touple
companies = [('Google', 2019, 134.81), ('Apple', 2019, 260.2), ('Facebook', 2019, 70.7)]

def sort_key(company):
    return company[2]

companies.sort(key= sort_key, reverse=True)
print(companies)

# Sort using Lambda expression
companies.sort(key=lambda company: company[2], reverse=True)
print(f'Sort Using LE - {companies}')

# sorted() function : its return new soeted list from the original list

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests)

print(guests)
print(sorted_guests, end='\n\n')

sorted_guests = sorted(guests, reverse=True)
print(sorted_guests)

