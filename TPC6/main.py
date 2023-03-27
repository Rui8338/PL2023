import ply.lex as lex
import sys

tokens = (
    'COMENT',
    'FUNCAO',
    'PROGRAMA',
    'IDENTIFICADOR',
    'INT',
    'WHILE',
    'FOR',
    'PRINT',
    'IF',
    'APR',
    'FPR',
    'AP',
    'FP',
    'APB',
    'FPB',
    'EQUIV',
    'IGUAL',
    'DIFERENTE',
    'MENOR',
    'MAIOR',
    'MODULO',
    'MULT',
    'DIV',
    'PVIRG',
    'DPONTOS',
    'VIRGULA',
    'MENOS',
    'MAIS',
    'MENORIGUAL',
    'MAIORIAGUAL',
    'NUM'
)

t_COMENT=r'/\*(\n|.)*\*/|//.*'
t_FUNCAO=r'function'
t_PROGRAMA=r'program'
t_IDENTIFICADOR=r'[a-zA-Z][a-zA-Z0-9]*'
t_WHILE=r'while'
t_FOR=r'for'
t_PRINT=r'print'
t_IF=r'if'
t_APR=r'\['
t_FPR=r'\]'
t_AP=r'\('
t_FP=r'\)'
t_APB=r'{'
t_FPB=r'}'
t_EQUIV=r'=='
t_IGUAL=r'='
t_DIFERENTE=r'!='
t_MENOR=r'<'
t_MAIOR=r'>'
t_MODULO=r'%'
t_MULT=r'\*'
t_DIV=r'/'
t_PVIRG=r';'
t_DPONTOS=r'\.\.'
t_VIRGULA=r','
t_MENOS=r'-'
t_MAIS=r'\+'
t_MENORIGUAL=r'<='
t_MAIORIAGUAL=r'>='
t_INT=r'int'

t_ignore = ' \t\n'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

with open(sys.argv[1], 'r') as file:
    data = file.read()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)