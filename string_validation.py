# Question to check wheather the string is valid or not it contains the parenthesis where it check if the parenthesis is properly closed.


def string_validation(text):
	length = len(text)
	check = ['(','[','<','{',')',']','>','}']
	result =[]
	if length ==0:
		return "Valid !"
	
	if  length%2!=0 or text[0] in check[4:]:
		return "Invalid !"
		
	for i in text:
		if i not in check:
			return "Invalid ! String contian incorrect symbol"
	
	for i in text:
		if i in check[0:4]:
			result.append(i)
		else:
			t = check.index(i)
			r = check.index(result.pop())
			if t - r != 4 :
				print(i,)
				return "Invalid ! Parenthesis are not closed properly "
			
	
	
	
	
	if result == []:
		return "Valid.."
	
	
	return "Invalid ! No proper closing of the brackets"
	
	
	
	
	
	
	
	
	
print(string_validation(("<<<>>>")))