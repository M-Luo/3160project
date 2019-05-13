import lexer
import parser

def main():
  # read source file
  source=""
  with open('source_file','r') as file:
    source = file.read()
  
  # Lexer
  # call lexer class and initialize it with source code
  lex = lexer.Lexer(source)
  # call tokenizer
  tokens = lex.tokenize()

  # Paser
  parse = parser.Parser(tokens)
  parse.parse()
  
main()
