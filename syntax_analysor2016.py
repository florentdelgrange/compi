import ply.yacc as yacc
from dumbo_interpreter import tokens

def p_programme_txt(p):
	'''programme : txt'''
	p[0] = p[1]

def p_programme_text_programme(p):
	'''programme : txt programme'''
	p[0] = p[1]+p[2]

def p_txt(p):
	'''txt : TXT'''
	p[0] = p[1]

def p_programme_dumbo(p):
	'''programme : dumbo_bloc'''
	p[0] = p[1]

def p_programme_dumbo_rec(p):
	'''programme : dumbo_bloc programme'''
	p[0] = p[1] +p[2]

def p_dumbo_bloc(p):
	'''dumbo_bloc : HOOK_OPEN HOOK_OPEN expression_list HOOK_CLOSE HOOK_CLOSE'''
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_expression_list(p):
	'''expression_list : expression SEMICOLON expression_list'''
	p[0] = p[1] + p[2] + p[3]

def p_expression_list_expression(p):
	'''expression_list : expression SEMICOLON'''
	p[0] = p[1] + p[2]

def p_expression_print(p):
	'''expression : PRINT string_expression'''
	p[0] = p[1] + p[2]

def p_expression_string_list(p):
	'''expression : FOR variable IN string_list DO expression_list ENDFOR'''
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_expression_string_variable(p):
	'''expression : FOR variable IN variable DO expression_list ENDFOR'''
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_expression_var_string_expr(p):
	'''expression : variable EQUALS string_expression'''
	p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_expression_var_string_list(p):
	'''expression : variable EQUALS string_list'''
	p[0] = p[1] + p[2] + p[3]

def p_string_expression_string(p):
	'''string_expression : string'''
	p[0] = [1]

def p_string_expression_variable(p):
	'''string_expression : variable'''
	p[0] = p[1]

def p_string_expression_concat(p):
	'''string_expression : string_expression DOT string_expression'''
	p[0] = p[1] + p[3]

def p_string_list(p):
	'''string_list : PARENTHESIS_OPEN string_list_interior PARENTHESIS_CLOSE'''
	p[0] = p[1] + p[2] + p[3]

def p_string_list_interior_string(p):
	'''string_list_interior :  string'''
	p[0] = p[1]

def p_string_list_interior_rec(p):
	'''string_list_interior : string COMMA string_list_interior'''
	p[0] = p[1] + p[2] + p[3]

def p_variable(p):
	'''variable : VARIABLE'''
	p[0] = p[1]

def p_string(p):
	'''string : STRING'''
	p[0] = p[1]


def p_error(p):
	print("Syntax error in line{}".format(p.lineno))

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
	import sys
	input = file(sys.argv[1]).read()
	result = yacc.parse(input,debug=True)
	print(result)
