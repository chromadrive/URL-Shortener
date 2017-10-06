import string

charmap = string.digits +\
		  string.ascii_lowercase +\
		  string.ascii_uppercase

def convert_num_to_alpha(n, base = 62):
	# Technically just converting base 10 to base 62
	if base <= 0 or base > 62:
		return 0
	result = ""
	while n > 0:
		remainder = n % base
		result = charmap[int(remainder)] + result
		n = n // base
	return result

def convert_alpha_to_num(n, base = 62):
	# Technically converting base 62 to base 10
	length = len(n)
	result = 0
	for i in range(length):
		result =  result * base + charmap.find(n[i])
	return result