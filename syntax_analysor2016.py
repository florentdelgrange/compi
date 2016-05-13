import ply.yacc as yacc
from dumbo_interpreter import tokens

def p_programme_txt(p):
	'''programme : txt'''
	p[0] = p[1]

def p_programme_text_programme(p):
	'''programme : txt programme'''
	p[0] = p[1]+p[2]

def txt(p):
	'''txt : TXT'''
	p[0] = p[1]

def dumbo_bloc(p):
	'''dumbo_bloc : HOOK_OPEN HOOK_OPEN expression_list HOOK_CLOSE HOOK_CLOSE'''
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def expression_list(p):
	'''expression_list : expression SEMICOLON expression_list'''
	p[0] = p[1] + p[2] + p[3]

def expression_list_expression(p):
	'''expression_list : expression SEMICOLON'''
	p[0] = p[1] + p[2]

def expression_print(p):
	'''expression : PRINT string_expression'''
	p[0] = p[1] + p[2]

def expression_string_list(p):
	'''expression : FOR variable IN string_list DO expression_list ENDFOR'''
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]



