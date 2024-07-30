# Modules
import mathUtils as mu
result = mu.add(6, 8)
print(result) # 14

"""
import <module_name>
from <module_name> import <function_name>
import <module_name> as m
from <module_name> import <function_name> as m_function
from <module_name> import *

"""

# Generators - Convenient way to implement the iterator protocol.
def count(start, step):
    while True:
        yield start
        start += step
        
counter = count(10, 2)
print(next(counter), next(counter), next(counter), next(counter))

# Yield - yield is a keyword that allows a function to produce a sequence of values over time, 
# rather than computing them all at once and returning them in a list,


# Debugger
# Decorator that prints function's name every time it gets called.
from functools import wraps

def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out

@debug
def add(x, y):
    return x + y

# Wraps is a helper decorator that copies metadata of function add() to function out().
# Without it 'add.__name__' would return 'out'.

print(add(10, 17))

