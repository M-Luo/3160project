import ply.yacc as yacc
from lexer import tokens

def expr_plus(p):
  'expression : expression PLUS term'
  p[0] = p[1] + p[3]

def expr_minus(p):
  'expression : expression MINUS term'
  p[0] = p[1] - p[3]

def expr_mul(p):
  'expression : expression MUL term'
  p[0] = p[1] * p[3]
