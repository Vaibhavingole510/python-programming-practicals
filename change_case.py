def change_case(input_str, style):
    if style == "c":
        return input_str.upper()
    elif style == "s":
        return input_str.lower()
    elif style == "r":
        return input_str.swapcase()
    elif style == "u":
        result = []
        # Determine the starting case based on the first character
        is_upper = input_str[0].isupper()
        
        for i, char in enumerate(input_str):
            if char.isalpha():
                if (i % 2 == 0 and is_upper) or (i % 2 == 1 and not is_upper):
                    result.append(char.upper())
                else:
                    result.append(char.lower())
            else:
                result.append(char)  # Non-alphabetic characters remain unchanged
        
        return ''.join(result)
    else:
        return input_str  # If the style is not recognized, return the original string

# Example usage:
print(change_case("Hello World", "c"))  # Output: "HELLO WORLD"
print(change_case("Hello World", "s"))  # Output: "hello world"
print(change_case("Hello World", "r"))  # Output: "hELLO wORLD"
print(change_case("Hello World", "u"))  # Output: "HeLlO WoRlD"
