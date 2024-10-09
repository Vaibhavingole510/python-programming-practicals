def get_even_odd_count(lst):
    even_count = 0
    odd_count = 0

    for item in lst:
        
        if isinstance(item, int):
            if item % 2 == 0:
                even_count += 1  
            else:
                odd_count += 1   
    
    return even_count, odd_count


lst = [4, 'a', 2, 8, 'b', 1, 5, 8, 3]
even_count, odd_count = get_even_odd_count(lst)
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
