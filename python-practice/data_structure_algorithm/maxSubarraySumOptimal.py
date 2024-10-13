import sys

# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) 
# which has the largest sum and returns its sum and prints the subarray.

def max__subarray_number(arr: list[int])-> int:
    max_sum = -sys.maxsize - 1
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
       
        if current_sum < 0:
            current_sum = 0    
            
    return max_sum

# input
input_array = [-2,1,-3,4,-1,2,1,-5,4]

output = max__subarray_number(input_array)
print(f'Output - {output}')