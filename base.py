def base(text, textbase, output_base):
    def getsum(text, textbase):
        if text.isdigit() and textbase.isdigit():
            num = []
            for i in range(len(text)-1, -1, -1):
                elem = text[i]
                num.append(elem)
            
            val_j = []
            for j in range(len(text)):
                val_j.append(j)
            
            sum_value = 0
            for i in range(len(num)):
                sum_value += int(num[i]) * (pow(int(textbase), val_j[i]))
            print("After conversion, the value is -->", sum_value)
            return sum_value
        
        elif not textbase.isdigit():
            raise ValueError("Invalid textbase")
    
    def base_answer(text, textbase, output_base):
        sum_value = getsum(text, textbase)
        val = list(range(10, 37))
        symbol = list(chr(i) for i in range(65, 91))
        val_sym = {val[i]: symbol[i] for i in range(26)}

        outputbase = int(output_base)
        
        if not (2 <= outputbase <= 36):
            raise ValueError("Invalid output_base")
        elif sum_value < outputbase:
            return str(sum_value)
        elif sum_value == outputbase:
            return "1"
        else:
            result = ""
            while sum_value > 0:
                rem = sum_value % outputbase
                if rem >= 10:
                    result += val_sym[rem]  # Get the corresponding letter for rem if rem >= 10
                else:
                    result += str(rem)
                sum_value = sum_value // outputbase
            return result[::-1]  # Reverse the result since remainders are generated in reverse order
    
    return base_answer(text, textbase, output_base)

res = base("10111100111", "10", "32")
print("Result:", res)