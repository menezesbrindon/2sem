import ply.lex as lex
import ply.yacc as yacc
import sys
tokens = ['LT','GT','GE','LE','EQUAL']

t_LT = r'<'
t_GT = r'>'
t_GE = r'>='
t_LE= r'<='
t_EQUAL = r'=='
t_ignore = r' '


    
def t_error(t):
	
	t.lexer.skip(1)
  	
lexer = lex.lex()
#lexer.input("1+2")
#lexer.input("abc=123"
fh=open('regex.py','r').read()
#for i in fh:
lexer.input(fh)
while True:
        tok = lexer.token()
        if not tok:
                break
        print(tok)

