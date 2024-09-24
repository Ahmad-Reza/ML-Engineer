# Find the pair of two sum numbers index.
def twoSum(nums: list[int], target: int)-> list[int]:
    num_dict = {}
    
    # O(n)
    for index, num in enumerate(nums):
        complement =  target - num
        
        #  O(1)
        if complement in num_dict:
            return [num_dict[complement], index]
        
        num_dict[num] = index

nums =  [8, 2, 11, 7, 15, 1]
target = 9
print(twoSum(nums, target)) # Output: [1, 3], Time complexity is O(n)