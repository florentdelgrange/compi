import ply.lex as lex

tokens = ('ADDOP','MULOP','INTEGER','TXT', 'VARIABLE', 'STRING', 'HOOK_OPEN', 'HOOK_CLOSE', 'SEMICOLON', 'PRINT', 'FOR', 'IN', 'DO', 'ENDFOR', 'EQUALS', 'DOT', 'COMMA', 'PARENTHESIS_OPEN', 'PARENTHESIS_CLOSE')

t_TXT = r'[a-z|A-Z|0-9|;|&|<|>|"|_|\-|\.|\\|\/|\n|\p|:|,|=]+'
t_ADDOP = r'\+|\-|'
t_MULOP = r'\*|\/'

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
lexer = lex.lex()
if __name__ == "__main__":
    import sys
    lexer.input(sys.stdin.read())
    for token in lexer:
        print "line %d : %s (%s)" %(token.lineno, token.type, token.value)
