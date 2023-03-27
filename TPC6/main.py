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
    'NUM',
    'IN'
)

t_COMENT=r'/\*(\n|.)*\*/|//.*'
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

t_ignore = ' \t\n'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value == 'int':
        t.type = 'INT'
    elif t.value == 'function':
        t.type = 'FUNCAO'
    elif t.value == 'while':
        t.type = 'WHILE'
    elif t.value == 'program':
        t.type = 'PROGRAMA'
    elif t.value == 'for':
        t.type = 'FOR'
    elif t.value == 'in':
        t.type = 'IN'
    elif t.value == 'print':
        t.type = 'PRINT'
    elif t.value == 'if':
        t.type = 'IF'
    return t

def t_error(t):
    print(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

with open(sys.argv[1], 'r') as file:
    data = file.read()
    lexer.input(data)

    while tok := lexer.token():
        print(tok)