def two_sum(num_arr, target):
    for i in range(len(num_arr)):
        for j in range(i + 1, len(num_arr)):
            if num_arr[i] + num_arr[j] == target:
                print(f'Pair of sum ({i} {j})')
                
num_arr = [3, 5, 2, -4, 8, 11]
target = 7
two_sum(num_arr, target)