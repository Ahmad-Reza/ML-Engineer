from collections import Counter


# Enumerate 
for i, ele in enumerate('hello'):
    print(f'{i} - {ele}')
    
# Counter
colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
counter = Counter(colors)

print(counter)  # Output: Counter({'blue': 3, 'red': 2, 'yellow': 1})
print(f'most common - {counter.most_common()[0]}') # ('blue', 3)

# Named tuple
# Tuple is an immutable and hashable list.
# Named tuple is its subclass with named elements.
from collections import namedtuple

Point = namedtuple('Point', 'x y')
p = Point(1, y=2)# Point(x=1, y=2)
p[0]             # 1
p.x              # 1
getattr(p, 'y')  # 2
p._fields        # Or: Point._fields #('x', 'y')

# another example...
Person = namedtuple('Person', 'name height')
person = Person('Jean-Luc', 187)
f'{person.height}'           # '187'
'{p.height}'.format(p=person)# '187'

# OrderedDict - Maintains order of insertion
from collections import OrderedDict
# Store each person's languages, keeping # track of who responded first. 
programmers = OrderedDict()
programmers['Tim'] = ['python', 'javascript']
programmers['Sarah'] = ['C++']
programmers['Bia'] = ['Ruby', 'Python', 'Go']

for name, langs in programmers.items():
    print(name + '-->')
    for lang in langs:
      print('\t' + lang)


# Comprehensions 
list1 = [i+1 for i in range(10)]         # [1, 2, ..., 10]
set1  = {i for i in range(10) if i > 5}  # {6, 7, 8, 9}
iter1 = (i+5 for i in range(10))         # (5, 6, ..., 14)
dict1 = {i: i*2 for i in range(10)}      # {0: 0, 1: 2, ..., 9: 18}

output = [i+j for i in range(3) for j in range(3)] # [0, 1, 2, 1, 2, 3, 2, 3, 4]

# Is the same as:
output = []
for i in range(3):
  for j in range(3):
    output.append(i+j)
    
# Ternary Condition
# <expression_if_true> if <condition> else <expression_if_false>

ternaryList = [a if a else 'zero' for a in [0, 1, 0, 3]] # ['zero', 1, 'zero', 3]
print(f'ternary example - {ternaryList}')

# Map Filter Reduce
from functools import reduce
list(map(lambda x: x + 1, range(10)))            # [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
list(filter(lambda x: x > 5, range(10)))         # (6, 7, 8, 9)
reduce(lambda acc, x: acc + x, range(10))        # 45


# Any All
any([False, True, False]) # True if at least one item in collection is truthy, False if empty.
all([True,1,3,True])      # True if all items in collection are true
