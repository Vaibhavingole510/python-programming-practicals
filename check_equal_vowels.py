def check_equal_vowels(s):
    # Initialize a dictionary to count occurrences of each vowel
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Traverse through the string and count vowels
    for char in s.lower():  # Convert string to lowercase to handle case insensitivity
        if char in vowel_count:
            vowel_count[char] += 1
    
    # Filter out vowels that have a count of 0 (i.e., vowels not present in the string)
    non_zero_vowel_counts = [count for count in vowel_count.values() if count != 0]
    
    # If there are no vowels in the string, consider it a valid string
    if not non_zero_vowel_counts:
        return "Valid String"
    
    # Get the first vowel count to compare with others
    first_vowel_count = non_zero_vowel_counts[0]
    
    # Check if all non-zero vowel counts are the same
    if all(count == first_vowel_count for count in non_zero_vowel_counts):
        return "Valid String"
    else:
        return "Invalid String"

# Test the function
input_string = input("Enter a string: ")
print(check_equal_vowels(input_string))
