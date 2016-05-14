import ply.lex as lex

tokens = ('LT','BT','EQ','NE','IF','ENDIF','TRUE','FALSE','OR','AND','ADDOP','MULOP','INTEGER','TXT', 'VARIABLE', 'STRING', 'HOOK_OPEN', 'HOOK_CLOSE', 'SEMICOLON', 'PRINT', 'FOR', 'IN', 'DO', 'ENDFOR', 'EQUALS', 'DOT', 'COMMA', 'PARENTHESIS_OPEN', 'PARENTHESIS_CLOSE')

t_TXT = r'[a-z|A-Z|0-9|;|&|<|>|"|_|\-|\.|\\|\/|\n|\p|:|,|=]+'

def t_HOOK_OPEN(t):
    r'\{(\n)*'
    return t

def t_HOOK_CLOSE(t):
    r'\}(\n)*'
    return t

def t_PARENTHESIS_CLOSE(t):
    r'\)'
    return t

def t_PARENTHESIS_OPEN(t):
    r'\('
    return t

def t_COMMA(t):
    r'\,'
    return t

def t_DOT(t):
    r'\.'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_DO(t):
    r'do(\n)*'
    return t

def t_IN(t):
    r'in'
    return t

def t_FOR(t):
    r'for'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_SEMICOLON(t):
    r';(\n)*'
    return t

def t_EQUALS(t):
    r':='
    return t

def t_ADDOP(t):
    r'\+|\-'
    return t

def t_MULOP(t):
    r'\*|\/'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_IF(t):
    r'if'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_LT(t):
    r'<'
    return t

def t_BT(t):
    r'>'
    return t

def t_EQ(t):
    r'='
    return t

def t_NE(t):
    r'!='
    return t

def t_STRING(t):
    r'\'[a-z|A-Z|0-9|;|&|<|>|"|_|\s|\-|\.|\\|\/|\n|\p|:|,|=]+\''
    t.value = str(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-z|A-Z|0-9_]+'
    return t

t_ignore = ' \t'

def t_error(t):
    print "Illegal character '%s'" %t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()
if __name__ == "__main__":
    import sys
    lexer.input(sys.stdin.read())
    for token in lexer:
        print "line %d : %s (%s)" %(token.lineno, token.type, token.value)
