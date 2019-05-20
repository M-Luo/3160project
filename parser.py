import ply.yacc as yacc
from lexer import tokens

# precedence level and associativity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES'),
    ('right', 'UMINUS'),            # Unary minus operator
)

def expr_term(p):
  'expression : term'
  p[0] = p[1]

def expr_plus(p):
  'expression : expression PLUS term'
  p[0] = p[1] + p[3]

def expr_minus(p):
  'expression : expression MINUS term'
  p[0] = p[1] - p[3]

def expr_mul(p):
  'expression : expression MUL term'
  p[0] = p[1] * p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# unary minus
def p_expr_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

# syntax errors
def p_error(p):
    print ("error")

# handle empty production
def p_empty(p):
  'empty :'
  pass



# build parser
parser = yacc.yacc()

while True:
   try:
       s = input("x = 0;")
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print (result)

