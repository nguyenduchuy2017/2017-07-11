import itertools

#
# def my_max_funct(seq):
# 	elements = iter(seq)
#
# 	# print(next(elements))
#
# 	for i in elements:
# 		print(i)
# 		# print(next(elements))
# 	return
#
# print(my_max_funct((100, 33, 4, 'hello')))
# # print(my_max_funct((100, 33, 4, 'hello')))
# # print(my_max_funct((100, 33, 4, 'hello')))
# # print(my_max_funct((100, 33, 4, 'hello')))

# import itertools
#
# def minmax(data):
# 	'Computes the minimum and maximum values in one-pass using only 1.5*len(data) comparisons'
# 	it = iter(data)
# 	try:
# 		lo = hi = next(it)
# 	except StopIteration:
# 		raise ValueError('minmax() arg is an empty sequence')
# 	for x, y in itertools.zip_longest(it, it, fillvalue=lo):
# 		if x > y:
# 			x, y = y, x
# 		if x < lo:
# 			lo = x
# 		if y > hi:
# 			hi = y
# 	return lo, hi
#
# if __name__ == '__main__':
# 	# import random
# 	# data = [random.random() for i in range(1000)]
# 	# print (minmax(data))
#
# 	print(minmax(([2, -54, 888, -5], [55, 858, 98], [2222, 6988, 65], [-985, 6, 8, -32456])))


def length(obj):
	leng = len(obj)
	return leng


def my_max_funct(seq, key=lambda x: x):

	min_elem = max_elem = None

	for elem in seq:
		if min_elem is None or key(min_elem) > key(elem):
			min_elem = elem

		if max_elem is None or key(max_elem) < key(elem):
			max_elem = elem
	return min_elem, max_elem

print(my_max_funct(['foodname', 'hghyr', 'ty', 'tzhgjtuywmdcv', 'z', 's']))
