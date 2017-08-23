def seleted_number(min_number):
	def decor(func):
		def wrapper(num):
			# return [x**2 for x in func(num)]
			return list(filter(lambda x: x>min_number, [x**2 for x in func(num)]))
		return wrapper
	return decor

@seleted_number(25)
def num_list(num):
	return [x for x in range(num)]

print(num_list(10))