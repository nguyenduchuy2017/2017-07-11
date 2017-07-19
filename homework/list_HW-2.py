lst_1 = [1, 2, 3, [1, 2], 2, [1, [1, 3]], 20]
print(lst_1)# Convert to String and elete all unneeded symbols :

string = ((((str(lst_1)).replace('[', '')).replace(']', '')).replace(',', '')).replace(' ', '')

lst_3 = []                        # Convert "string" chars to int and and fill the new emty list
for elem in string:
	elem = int(elem)
	lst_3.append(elem)

print(lst_3)

