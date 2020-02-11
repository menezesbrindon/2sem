from ply import lex
import ply.yacc as yacc

tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
    'NUMBER'
]

t_ignore = ' \t'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t



def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
   # ( 'nonassoc', 'UMINUS' )
)

def p_binary_operators(p):
      '''expression : term exp
          exp : PLUS term exp
              | 
         term : factor t
         t          : TIMES factor t
                    | '''
      #print(p[2])
      if p[1][0] == '+':
          print('X:',p)
          p[0] = p[1] + p[1][2]
      elif p[1] == '+':
          #print(p)
          p[0] = p[2][0] + p[3]
      elif p[2] == '*':
          p[1] = p[2] * p[3]
      elif p[2] == '/':
          p[0] = p[1] / p[3] 

#
def p_parens( p ) :
    '''factor : LPAREN expression RPAREN
                  | NUMBER '''
    if p[1] =='(':
         p[0]=p[2]
    else:
        #print(p[1])
        p[0]=p[1]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()
a=input('enter the expression')
res = parser.parse(a) # the input
print(res)
