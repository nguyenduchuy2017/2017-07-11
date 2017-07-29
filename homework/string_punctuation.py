
import string
import re

def punct_remove(file_source = 'test_string.txt'):

	with open('test_string.txt', 'r+') as input_file:
		input_str = input_file.read()
		output_str = re.sub('[!@#$]', '', input_str)    # use library "re" to remove uneeded symbols
		print("Output string is: \n ", output_str)

		with open('output_file.txt', 'w') as output_string:   # Create and write data into output file:
			output_string.write(output_str)
		return output_str


def word_frequence_count():

	output_str = punct_remove('test_string.txt')      # return output file
	output_str_split = output_str.split()
	print("Output str_split ", output_str_split  )
	max_word_frequence = 0
	max_word = ""

	for word in output_str_split :
		if output_str_split .count(word) > max_word_frequence : # compare and set "a count" of symbol to "maximum"
			max_word_frequence = output_str_split.count(word)
			max_word = word
	print("The most frequence is : ", max_word_frequence, "   and the word is : '",max_word,"'")


word_frequence_count()
