	# We don't need to determine all the addition and subtraction, just one
	# check for addition, subtraction, multiplication, division, exponents, parentheses
	# https://math.stackexchange.com/questions/1588166/derivative-of-functions-of-the-form-fxgx
	#
	# add the direct rules up here:
	# constant rule
	# power rule?
	# All these rules should probably get their own method
	# 
	# structural rules
	# addition and subtraction

def remove_outer_parens(func_str):
	outer_parens = False
	if func_str[0] == "(":
		outer_parens = True
		level = 0
		for idx in range(len(func_str)):
			char = func_str[idx]
			if char == "(":
				level += 1
			if char == ")":
				level -= 1
			if idx != len(func_str)-1 and level == 0:
				outer_parens = False
	if outer_parens == False:
		return func_str
	else:
		return remove_outer_parens(func_str[1:-1])

def multiply(str1, str2):
	if str1 == "0" or str2 == "0":
		return "0"
	if str1 == "1":
		return str2
	if str2 == "1":
		return str1
	return f"{str1}*{str2}"

def add_rule(func_str, plus_idx):
	idx = plus_idx
	left = func_str[:idx]
	right = func_str[idx+1:]
	dleft = d(left)
	dright = d(right)
	dleft = remove_outer_parens(dleft)
	dright = remove_outer_parens(dright)
	if dleft == "0":
		return dright
	if dright == "0":
		return dleft
	return f"{dleft}+{dright}"

def sub_rule(func_str, sub_idx):
	idx = sub_idx
	left = func_str[:idx]
	right = func_str[idx+1:]
	dleft = d(left)
	dright = d(right)
	dleft = remove_outer_parens(dleft)
	dright = remove_outer_parens(dright)
	if dleft == "0":
		return f"-{dright}"
	if dright == "0":
		return dleft
	return f"{dleft}-({dright})"

def product_rule(func_str,  mult_idx):
	idx = mult_idx
	left = func_str[:idx]
	right = func_str[idx+1:]
	dleft = d(left)
	dright = d(right)
	final_str = ""
	if dleft == "0":
		final_str += ""
	elif dleft == "1":
		final_str += f"{right}"
	else:
		final_str += f"({dleft})*{right}"
	if final_str and dright != "0":
		final_str += "+"
	if dright == "0":
		final_str += ""
	elif dright == "1":
		final_str += f"{left}"
	else:
		final_str += f"{left}*({dright})"
	if not final_str:
		return "0"
	return final_str

def quotient_rule(func_str, div_idx):
	idx = div_idx
	top = func_str[:idx]
	bottom = func_str[idx+1:]
	dtop = d(top)
	dbottom = d(bottom)
	final_str = "("
	if dtop == "0":
		final_str += ""
	elif dtop == "1":
		final_str += f"{bottom}"
	else:
		final_str += f"({dtop})*{bottom}"
	if dbottom != "0":
		final_str += "-"
	if dbottom == "0":
		final_str += ""
	elif dbottom == "1":
		final_str += f"{top}"
	else:
		final_str += f"({dbottom})*{top}"
	if final_str == "(":
		return "0"
	else:
		final_str += f")/({bottom})^(2)"
	return final_str

def is_constant(func_str):
	try:
		num = float(func_str)
		return True
	except ValueError:
		return False


def d(func_str):
	# if func_str has matched parens on the outside, take them out
	func_str = remove_outer_parens(func_str)
	# check for top-level add or sub
	level = 0
	for idx in range(len(func_str)):
		char = func_str[idx]
		if level == 0 and char == "+":
			return add_rule(func_str, idx)
		if level == 0 and char == "-":
			return sub_rule(func_str, idx)
		if char == "(":
			level += 1
		if char == ")":
			level -= 1
	# no top-level add or sub, check for top-level mult or div
	level = 0
	for idx in range(len(func_str)):
		char = func_str[idx]
		if level == 0 and char == "*":
			return product_rule(func_str, idx)
		if level == 0 and char == "/":
			return quotient_rule(func_str, idx)
		if char == "(":
			level += 1
		if char == ")":
			level -= 1
	# no top-level add, sub, mult, div
	if func_str == "x":
		return "1"
	if is_constant(func_str):
		return "0"
	return func_str




	# first, create a list of the indices of outer pluses and minuses
	# 		by going through the string with a value indicating how many levels deep into parentheses 
	#		a character is and adding the indices of all pluses at level 0 to a list and the indices
	#  		of all minuses to another list. Or have one list and a negative index implies subtraction.
	# 		then return d(string[:pluses[0]]) + d(string[pluses[0]+1:pluses[1]]) + ...
	# second, if no pluses are present, make a similar list of multiplication and division at the
	#		outermost level and return using the chain rule
	# third, if no multiplication is present, check for exponents on the outermost level and return accordingly
	# 		(make sure to check the base and exponent for variables)
	# fourth, if there are none of the usual binary operation symbols on the outermost level, check for 
	#		unary operations like trig functions
	# lastly, if there are no operations on the outermost level, take d of the inside of the parentheses
	#		maybe throw an error if the first and last characters are not matching parentheses

def d(func_str):
	# requires expressions that: are fully parenthesised, have no spaces, have explicit multiplication
	val = 0
	idx = 0
	while val > 1 or idx < 2:
		if func_str[idx] == "(":
			val += 1
		if func_str[idx] == ")":
			val -= 1
		idx += 1
	# if there are no operators
	if idx == 2:
		if func_str[1] == "x":
			return "(1)"
		else:
			return "(0)"
	# now we have the index of the operator between the two outermost parenthesis groups inside the outside parentheses
	if idx == len(func_str):
			
		return func_str
	left = func_str[1:idx]
	right = func_str[idx+1:]
	if func_str[idx] == "+":
		return f"({d(left)}+{d(right)})"
	if func_str[idx] == "-":
		return f"({d(left)}-{d(left)})"
	if func_str[idx] == "*":
		return f"(({d(left)}*{right})+({left}*{d(right)}))"
	if func_str[idx] == "/":
		top = left
		bottom = right
		return f"(((({d(top)})*({bottom}))+(({top})*({d(bottom)}))/(({bottom})*({bottom})))"



# TODO: build a parser which implements PEMDAS to create a tree structure to evaluate expressions
# maybe the tree has non-leaf nodes with operator identifiers where leaf-nodes have values
# ex: "(2+3)*4" first parses the multiplication to create a "*" node with "2+3" and "4" as children. 
# 		4 becomes a value / leaf-node but 2+3 becomes a "+" node with leaf-node children of 2 and 3.
# 		Then this tree gets evaluated from the leaf to the root.
#		Maybe every node gets a value and an identifier but leafs get a trivial identifier?
#		This way the node values can be assigned as the nodes are created. But then why create the tree at all if we only need the top value?