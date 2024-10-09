def get_sl_ssv(lst):
    # Filter out non-integer values
    int_list = [x for x in lst if isinstance(x, int)]
    
    # If there are less than 2 integers, return None as we can't find second smallest and largest
    if len(int_list) < 2:
        return None, None
    
    # Initialize variables to store smallest and second smallest, largest and second largest
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    
    # Find the smallest and largest integers
    for num in int_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    
    return second_smallest, second_largest

# Example usage:
lst = [4, 'a', 2, 8, 'b', 1, 233, 56,8, 3]
second_smallest, second_largest = get_sl_ssv(lst)
print(f"Second smallest: {second_smallest}, Second largest: {second_largest}")
