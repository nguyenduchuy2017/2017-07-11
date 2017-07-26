
def char_replace(file_source = 'simple_game.py'):

	with open(file_source, 'r') as input_file:
		file_target = input_file.read()
		max_car_count = file_target.count(file_target[0]) # set a count of the first symbol in file is as "maximum".
		max_char = ""                                      # symbol which has the maximum count

		for char in file_target:
			if file_target.count(char) > max_car_count:   # compare and set "a count" of symsol to "maximum"
				max_car_count = file_target.count(char)
				max_char = char

	if max_char == ' ':             # in order to see symbol ' '  replace it by words ( "white space" )
		print('\nThe symbol, which is most often being seen is :  "white space" ')
	print('and it is repeated :',max_car_count, ' times')        # show the time that the symbol is repeated

	file_destination = file_target.replace(max_char, '$')      # replace "max_count_symbol" by '$'

	with open('file_destination.txt', 'r+') as output_file_1:  # create a new file on disk
		output_file_1.write(file_destination)                  # and write data into it

	with open('file_destination.txt', 'r') as output_file_2:   # open file and output the result
		result_file = output_file_2.read()
		print('\nThe result is:\n"\n',result_file)
		print('"')

char_replace()
