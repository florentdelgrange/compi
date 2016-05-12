import ply.lex as lex

tokens = ('TXT', 'VARIABLE', 'STRING', 'PIPE', 'HOOK_OPEN', 'HOOK_CLOSE', 'SEMICOLON', 'PRINT', 'FOR', 'IN', 'DO', 'ENDFOR', 'EQUALS', 'DOT', 'COMMA', 'PARENTHESIS_OPEN', 'PARENTHESIS_CLOSE')

t_PARENTHESIS_CLOSE = r'\)'
t_PARENTHESIS_OPEN = r'\('
t_COMMA = r'\,'
t_DOT = r'\.'
t_EQUALS = r':='
t_ENDFOR = r'endfor'
t_DO = r'do'
t_IN = r'in'
t_FOR = r'for'
t_PRINT = r'print'
t_SEMICOLON = r';'
t_HOOK_CLOSE = r'\{'
t_HOOK_OPEN = r'\}'
t_PIPE = r'\|'

def t_STRING(t):
    r'\'[a-z | A-Z | 0-9 | ; | & | < | > | " | _ | \s | \- | \. | \\ | \/ | \\n | \\p | : | , | =]+\''
    t.value = str(t.value)
    return t

def t_VARIABLE(t):
    r'[a-z | A-Z | 0-9]+'
    return t

def t_TXT(t)
    r'[a-z | A-Z | 0-9 | ; | & | < | > | " | _ | \- | \. | \\ | \/ | \\n | \\p | : | , | =]+'
    return t

lexer = lex.lex()
if __name__ == "__main__":
    import sys
    lexer.input(sys.stdin.read())
    for token in lexer:
        print "line %d : %s (%s)" %(token.lineo, token.type, token.value)
