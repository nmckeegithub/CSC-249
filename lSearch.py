def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  
    return -1  

my_list = [5, 2, 9, 1, 5, 6]
target_value = 9
result = linear_search(my_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print("Target not found in the list")
  
