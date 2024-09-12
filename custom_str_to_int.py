def custom_str_to_int(num_str: str):
    """Convert a string number to an integer without using the built-in int()"""
    num_str = num_str.strip()  # Remove any surrounding whitespace
    sign = -1 if num_str[0] == '-' else 1  # Check for negative sign
    if num_str[0] in ['-', '+']:  # Remove sign if present
        num_str = num_str[1:]

    integer_value = 0
    for char in num_str:
        # Calculate the integer value by using ASCII values of digits
        integer_value = integer_value * 10 + (ord(char) - ord('0'))

    return sign * integer_value


def subtract_decimal_strings(num1: str, num2: str):
    # Check if the numbers are negative and adjust signs accordingly
    if num1[0] == '-' and num2[0] != '-':
        return '-' + subtract_decimal_strings(num1[1:], num2)
    elif num2[0] == '-' and num1[0] != '-':
        return subtract_decimal_strings(num1, num2[1:])
    elif num1[0] == '-' and num2[0] == '-':
        return subtract_decimal_strings(num2[1:], num1[1:])

    # Ensure both numbers have a decimal point (for uniform processing)
    if '.' not in num1:
        num1 += '.0'
    if '.' not in num2:
        num2 += '.0'

    # Split the numbers into whole and decimal parts
    whole1, dec1 = num1.split('.')
    whole2, dec2 = num2.split('.')

    # Normalize the decimal parts to the same length by padding with zeros
    max_len = max(len(dec1), len(dec2))
    dec1 = dec1.ljust(max_len, '0')
    dec2 = dec2.ljust(max_len, '0')

    # Convert decimal parts to integers for subtraction
    decimal_diff = custom_str_to_int(dec1) - custom_str_to_int(dec2)

    # Handle borrowing if necessary for the decimal part
    if decimal_diff < 0:
        decimal_diff += 10 ** max_len
        whole1 = str(custom_str_to_int(whole1) - 1)  # Borrow from the whole part

    # Convert whole parts to integers and subtract
    whole_diff = custom_str_to_int(whole1) - custom_str_to_int(whole2)

    # Handle the case where the result is negative
    negative_result = whole_diff < 0
    if negative_result:
        whole_diff = abs(whole_diff)

    # Format the result properly
    decimal_diff_str = str(decimal_diff).rjust(max_len, '0').rstrip('0')  # Remove trailing zeros
    if decimal_diff_str == '':
        result = str(whole_diff)
    else:
        result = f"{whole_diff}.{decimal_diff_str}"

    # Handle the negative result case
    if negative_result:
        result = '-' + result

    return result


# Example usage:
num1 = "123.45"
num2 = "23.12"
result = subtract_decimal_strings(num1, num2)
print(f"{num1} - {num2} = {result}")

# More test cases
print(subtract_decimal_strings("23.12", "123.45"))  # Negative result
print(subtract_decimal_strings("-23.12", "-123.45"))  # Subtracting two negative numbers
print(subtract_decimal_strings("100.00", "99.99"))  # Borrowing from whole part
print(subtract_decimal_strings("123", "23.99"))  # Mixed whole and decimal
