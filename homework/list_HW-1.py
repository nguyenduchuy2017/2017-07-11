lst_1 = [1, 2, 3, [1, 2], 2, [1, [1, 3]], 20]
print(lst_1)
str_1 = str(lst_1)                # Convert to String
str_2 = str_1.replace('[', '')    # Delete all unneeded symbols
str_3 = str_2.replace(']', '')
str_4 = str_3.replace(',', '')
str_5 = str_4.replace(' ', '')

lst_3 = []                        # Convert "string" chars to int and and fill the new emty list
for elem in str_5:
	elem = int(elem)
	lst_3.append(elem)

print(lst_3)

