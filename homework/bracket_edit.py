def correct_string(expression) :
	left_bracket_counter = expression.count("(")         # quantity of the left brackets
	right_bracket_counter = expression.count(")")        # quantity of the right brackets
	right_bracket_to_add = left_bracket_counter - right_bracket_counter    # different beetween left and right brackets
	left_bracket_to_add = - right_bracket_to_add         # different beetween right and left brackets

	if right_bracket_to_add:
		expression =  expression + " )"*right_bracket_to_add
	if left_bracket_to_add:
		expression = "( "*left_bracket_to_add + expression

	return expression

print(correct_string("c/d - (a + b) * 6)))"))