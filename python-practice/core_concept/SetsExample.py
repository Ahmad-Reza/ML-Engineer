# Sets - unordered collection of unique elements.
my_set = set()
my_set.add(1)
my_set.add(100)
my_set.add(100) # no duplicate

print(f'set - {my_set}')

new_list = [1, 1, 3, 4, 3, 2, 0, 0, 7, 8]
new_set = set(new_list)
print(f'new set {new_set}')

new_set.remove(8) # Raises keyError if element not found.
new_set.discard(0) # Doesn't raise an error if element not found.
print(new_set)

new_set.clear() # {}
new_set = {1, 2, 3}.copy() # {1, 2, 3}

set1 = {2, 3, 4}
set2 = {7, 0, 9, 2}

print(f'Union - {set1.union(set2)}') # {0, 2, 3, 4, 7, 9}
print(f'Intersection - {set1.intersection(set2)}') # {2}
print(f'Difference - {set1.difference(set2)}') # {3, 4}
print(f'Symmetric difference - {set1.symmetric_difference(set2)}') # {0, 3, 4, 7, 9}

set1.issubset(set2) # False
set1.issuperset(set2) # False
set1.isdisjoint(set2) # False --> return true if two sets have a null intersection.

# Frozenset
# Hashable --> it can be used as a key in dictionary or as an element in a set.
# <frozenset> = frozenset(<collection>)


# None - used to absence of a value and can be used to show nothing has been assigned to an object.
type(None) # NoneType
a = None