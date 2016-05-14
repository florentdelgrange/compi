import ply.yacc as yacc
from lexical_analysor2016 import tokens

variables = {}

#This will be a leaf (a terminal symbol)
class TextNode():
    def __init__(self, text):
        self.text = text
         
    def ex(self):
        return str(self.text)

class StringNode():
    def __init__(self, text):
        self.text = text
         
    def ex(self):
        return str(self.text[1:])

class AssignNode():
    def __init__(self, *args):
        self.var_name = args[0]
        self.rhs = args[1]

    def ex(self):
    	print "debug"+str(self.var_name)
        variables[str(self.var_name)] = self.rhs.ex()
        return ""

class VariableNode():
    def __init__(self, *args):
        self.name = args[0]
         
    def ex(self):
    	return variables.get(str(self.name),"ERROR : UNDEFINED VARIABLE")

    def __repr__(self):
        return str(self.name)

class RegularNode():
	def __init__(self, *args):
		self.sons = args
         
	def ex(self):
		to_print = ""
		for son in self.sons:
			to_print+=str(son.ex())
		return to_print

class List():
	def __init__(self, *args):
		self.sons = args
         
	def ex(self):
		#cdb, on a juste une string
		if(len(self.sons) < 2):
			return [str(self.sons[0].ex())]
		else:
			return [str(self.sons[0].ex())] + self.sons[1].ex()

class PassNode():
	def __init__(self, son):
		self.son = son
         
	def ex(self):
		return self.son.ex()

class OperationNode():
	def __init__(self, *args):
		self.left_op = args[0]
		self.operator = str(args[1])
		self.right_op = args[2]
                self.operations = {
                    '+' : lambda x,y: x+y,
                    '-' : lambda x,y: x-y,
                    '/' : lambda x,y: x/y,
                    '*' : lambda x,y: x*y,
		}
         
	def ex(self):
		return self.operations[self.operator](self.left_op.ex(),self.right_op.ex())


class ForNode():
	def __init__(self, *args):
		self.sons = args
         
	def ex(self):
		var_name = str(self.sons[0]) #nom de la var

		initial_value = ""

		if var_name in variables:
			initial_value = variables[var_name]

		list_or_var = self.sons[1].ex() #liste (ou rec liste dans une var)
		action = self.sons[2]
		res = ""
		for var in list_or_var:
			variables[var_name] = var
			res+=action.ex()

		if initial_value != "":
			variables[var_name] = initial_value

		return res

class IfNode():
	def __init__(self, *args):
		self.sons = args
         
	def ex(self):
		condition = self.sons[0]
		action = self.sons[1]

		res = ""
		if(condition.ex()):
			res += str(action.ex())
		return res

class IntegerNode():
    def __init__(self, value):
        self.value = int(value)
         
    def ex(self):
    	return self.value

class BooleanNode():
    def __init__(self, value):
        self.value = str(value)
         
    def ex(self):
    	if(self.value == "true"):
    		return True
    	else:
    		return False

class AndOrNode():
    def __init__(self, *args):
        self.lhs = args[0]
        self.op = str(args[1])
        self.rhs = args[2]
         
    def ex(self):
    	if(self.op == "and"):
    		return self.rhs.ex() and self.lhs.ex()
    	else:
    		return self.rhs.ex() or self.lhs.ex()

class IntegerBooleanNode():
    def __init__(self, *args):
        self.lhs = args[0]
        self.op = str(args[1])
        self.rhs = args[2]
         
    def ex(self):
		operations = {
		'<' : lambda x,y: x<y,
		'>' : lambda x,y: x>y,
		'=' : lambda x,y: x==y,
		'!=' : lambda x,y: x!=y,
		}
		return operations[self.op](self.lhs.ex(),self.rhs.ex())

def p_programme_txt(p):
	'''programme : txt'''
	p[0] = RegularNode(p[1])

def p_programme_text_programme(p):
	'''programme : txt programme'''
	p[0] = RegularNode(p[1],p[2])


def p_programme_dumbo(p):
	'''programme : dumbo_bloc'''
	p[0] = RegularNode(p[1])

def p_programme_dumbo_rec(p):
	'''programme : dumbo_bloc programme'''
	p[0] = RegularNode(p[1],p[2])

#TextNode
def p_txt(p):
	'''txt : TXT'''
	p[0] = TextNode(p[1])

def p_dumbo_bloc(p):
	'''dumbo_bloc : HOOK_OPEN HOOK_OPEN expression_list HOOK_CLOSE HOOK_CLOSE'''
	p[0] = RegularNode(p[3])

#Plusieurs instructions separees de virgules on veut print le res de chaque exp
def p_expression_list(p):
	'''expression_list : expression SEMICOLON expression_list'''
	p[0] = RegularNode(p[1],p[3])

#fin de la liste d'instructions
def p_expression_list_expression(p):
	'''expression_list : expression SEMICOLON'''
	p[0] = RegularNode(p[1])

#ici on retourne le print d'une expression donc son str
def p_expression_print(p):
	'''expression : PRINT string_expression'''
	p[0] = RegularNode(p[2])

def p_expression_string_list(p):
	'''expression : FOR variable IN string_list DO expression_list ENDFOR'''
	p[0] = ForNode(p[2],p[4],p[6])

def p_expression_string_variable(p):
	'''expression : FOR variable IN variable DO expression_list ENDFOR'''
	p[0] = ForNode(p[2],p[4],p[6])

def p_expression_if(p):
	''' expression : IF boolean_expression DO expression_list ENDIF'''
	p[0] = IfNode(p[2],p[4])

#ADDING INT SUPPORT p3 pointe vers une operation dont le ex renvera la vaeur
def p_expression_var_operation(p):
	'''expression : variable EQUALS operation'''
	p[0] = AssignNode(p[1],p[3])

def p_expression_var_string_expr(p):
	'''expression : variable EQUALS string_expression'''
	p[0] = AssignNode(p[1],p[3])

def p_expression_var_string_list(p):
	'''expression : variable EQUALS string_list'''
	p[0] = AssignNode(p[1],p[3])

#Adding recursive way to tell operaton
#variable containing integer is already handled by string_expression

def p_operation_integer(p):
	'''operation : integer'''
	p[0] = PassNode(p[1])

def p_operation_rec(p):
	'''operation : operation ADDOP operation
	 | operation MULOP operation '''
	p[0] = OperationNode(p[1],p[2],p[3])

#Cas de base : on a une chaine de caractere
def p_string_expression_string(p):
	'''string_expression : string'''
	p[0] = RegularNode(p[1])

def p_string_expression_variable(p):
	'''string_expression : variable'''
	p[0] = RegularNode(p[1])

def p_string_expression_concat(p):
	'''string_expression : string_expression DOT string_expression'''
	p[0] = RegularNode(p[1],p[3])

def p_string_list(p):
	'''string_list : PARENTHESIS_OPEN string_list_interior PARENTHESIS_CLOSE'''
	p[0] = PassNode(p[2])

def p_string_list_interior_string(p):
	'''string_list_interior : string'''
	p[0] = List(p[1])

def p_string_list_interior_rec(p):
	'''string_list_interior : string COMMA string_list_interior'''
	p[0] = List(p[1],p[3])

def p_boolean_expr(p):
	'''boolean_expression : boolean'''
	p[0] = PassNode(p[1])

def p_boolean_expr_rec(p):
	'''boolean_expression : boolean_expression AND boolean_expression
						  |	boolean_expression OR boolean_expression'''

	p[0] = AndOrNode(p[1],p[2],p[3])

def p_boolean_expr_rec_integer(p):
	'''boolean_expression : variable LT variable
						  | variable BT variable
						  | variable EQ variable
						  | variable NE variable'''
	p[0] = IntegerBooleanNode(p[1],p[2],p[3])

def p_integer(p):
	'''integer : INTEGER'''
	p[0] = IntegerNode(p[1])

def p_boolean(p):
	'''boolean : TRUE 
			   | FALSE'''
	p[0] = BooleanNode(p[1])

def p_variable(p):
	'''variable : VARIABLE'''
	p[0] = VariableNode(p[1])

def p_string(p):
	'''string : STRING'''
	p[0] = StringNode(p[1])


def p_error(p):
	print("Syntax error in line{}".format(p.lineno))


precedence = (
	("left", "ADDOP"),
	("left", "MULOP"),
	("left", "DOT"),
	("left", "AND"),
	("left", "OR"),
	)

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
	import sys
	input = file(sys.argv[1]).read()
	yacc.parse(input,debug=True)
	input = file(sys.argv[2]).read()
	result = yacc.parse(input,debug=True)
	print result.ex()
