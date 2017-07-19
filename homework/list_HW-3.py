lst_1 = [1, 2, 3, [1, 2], 2, [1, [1, 3], 200]]
print(lst_1)

#  Convert to String and delete all unneeded symbols :

string = ((((str(lst_1)).replace('[', '')).replace(']', '')).replace(',', '')).split(" ")

# Convert "string" chars to int and fill the new emty list :

lst_2 = []

for elem in string:
	elem = int(elem)
	lst_2.append(elem)


print(lst_2)

