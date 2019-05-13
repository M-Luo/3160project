import ply.lex as lex

# list of tokens
#class Lexer:
tokens = (
  'ID',
  'ASSIGN',
  'NUMBER',
  'PLUS',
  'MINUS',
  'MUL',
  'LPAREN',
  'RPAREN',
  'EOS',
  )


#regular expression rules
t_ASSIGN = r'='
#t_NUMBER = r'0|[1-9][0-9]*'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_MUL    = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EOS    = r';'


  
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  return t

def t_NUMBER(t):
    r'0|[1-9][0-9]* '
    return t

# ignore spaces and tabs
t_ignore = ' \t'


# error handling
def t_error(t):
  print("error")
  t.lexer.skip(1)

# build the lexer
lexer = lex.lex()


data = '''
x = 0;
'''
lexer.input(data)
while True:
  tok = lexer.token()
  if not tok:break
  print (tok)


