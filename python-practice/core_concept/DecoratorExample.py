# Decorators -  
# Special type of function that can modify or extend the behavior of another function. 


# Syntax
"""
@decorator_name
def function_to_decorate():
    pass
"""

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def my_function(x, y):
    time.sleep(1)  # simulate some work
    return x + y

result = my_function(2, 3)
print(result)  # Output: 5

"""
In this example, the timer_decorator function takes the my_function function as an argument 
and returns a new function wrapper. The wrapper function calls the original my_function function, 
measures the execution time, and prints the result.
"""