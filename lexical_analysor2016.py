import ply.lex as lex

tokens = ('LT','BT','EQ','NE','IF','ENDIF','TRUE','FALSE','OR','AND','ADDOP','MULOP','INTEGER','TXT', 'VARIABLE', 'STRING', 'HOOK_OPEN', 'HOOK_CLOSE', 'SEMICOLON', 'PRINT', 'FOR', 'IN', 'DO', 'ENDFOR', 'EQUALS', 'DOT', 'COMMA', 'PARENTHESIS_OPEN', 'PARENTHESIS_CLOSE')

states = (
( 'inBlock' , 'inclusive' ) ,
)

def t_HOOK_OPEN(t):
    r'\{\{(\n)*'
    t.lexer.begin('inBlock')
    return t

def t_inBlock_HOOK_CLOSE(t):
    r'\}\}(\n)*'
    t.lexer.begin('INITIAL')
    return t

def t_inBlock_PARENTHESIS_CLOSE(t):
    r'\)'
    return t

def t_inBlock_PARENTHESIS_OPEN(t):
    r'\('
    return t

def t_inBlock_COMMA(t):
    r'\,'
    return t

def t_inBlock_DOT(t):
    r'\.'
    return t

def t_inBlock_ENDFOR(t):
    r'endfor'
    return t

def t_inBlock_DO(t):
    r'do(\n)*'
    return t

def t_inBlock_IN(t):
    r'in'
    return t

def t_inBlock_FOR(t):
    r'for'
    return t

def t_inBlock_PRINT(t):
    r'print'
    return t

def t_inBlock_SEMICOLON(t):
    r';(\n)*'
    return t

def t_inBlock_EQUALS(t):
    r':='
    return t

def t_inBlock_ADDOP(t):
    r'\+|\-'
    return t

def t_inBlock_MULOP(t):
    r'\*|\/'
    return t

def t_inBlock_TRUE(t):
    r'true'
    return t

def t_inBlock_FALSE(t):
    r'false'
    return t

def t_inBlock_AND(t):
    r'and'
    return t

def t_inBlock_OR(t):
    r'or'
    return t

def t_inBlock_IF(t):
    r'if'
    return t

def t_inBlock_ENDIF(t):
    r'endif'
    return t

def t_TXT(t):
    r'[a-z|A-Z|0-9|;|&|<|>|"|_|\-|\.|\\|\/|\n|\p|:|,|=]+'
    return t

def t_inBlock_LT(t):
    r'<'
    return t

def t_inBlock_BT(t):
    r'>'
    return t

def t_inBlock_EQ(t):
    r'='
    return t

def t_inBlock_NE(t):
    r'!='
    return t

def t_inBlock_STRING(t):
    r'\'[a-z|A-Z|0-9|;|&|<|>|"|_|\s|\-|\.|\\|\/|\n|\p|:|,|=]+\''
    t.value = str(t.value)
    return t

def t_inBlock_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_inBlock_VARIABLE(t):
    r'[a-z|A-Z|0-9_]+'
    return t

t_ignore = ' \t'
t_inBlock_ignore = ' |\n|\t'

def t_error(t):
    print "Illegal character '%s'" %t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()
if __name__ == "__main__":
    import sys
    lexer.input(sys.stdin.read())
    for token in lexer:
        print "line %d : %s (%s)" %(token.lineno, token.type, token.value)
