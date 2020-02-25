just_len = 60
import re
import collections

NUM     = r'(?P<NUM>\d+)'
PLUS    = r'(?P<PLUS>\+)'
TIMES   = r'(?P<TIMES>\*)'
LPAREN  = r'(?P<LPAREN>\()'
RPAREN  = r'(?P<RPAREN>\))'
WS      = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join((NUM, PLUS, TIMES, LPAREN, RPAREN, WS)))
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(pattern, text):
    scanner = pattern.scanner(text)
    for m in iter(scanner.match, None):
        token = Token(m.lastgroup, m.group())

        if token.type != 'WS':
            yield token

class ExpressionEvaluator:
    

    def parse(self, text):
        self.tokens = generate_tokens(master_pattern, text)
        self.current_token = None
        self.next_token = None
        self._advance()

        
        return self.expr()

    def _advance(self):
        self.current_token, self.next_token = self.next_token, next(self.tokens, None)

    def _accept(self, token_type):
        
        if self.next_token and self.next_token.type == token_type:
            self._advance()
            return True
        else:
            return False

    def _expect(self, token_type):
        if not self._accept(token_type):
            raise SyntaxError('Expected ' + token_type)

    def expr(self):
       

       
        expr_value = self.term()

        
        while self._accept('PLUS'):
           
            op = self.current_token.type

            right = self.term()
            if op == 'PLUS':
                expr_value += right
            else:
                raise SyntaxError('Should not arrive here ' + op)

        return expr_value

    def term(self):
        
        term_value = self.factor()

        
        while self._accept('TIMES'):
            op = self.current_token.type

            if op == 'TIMES':
                term_value *= self.factor()
            else:
                raise SyntaxError('Should not arrive here ' + op)

        return term_value

    def factor(self):
       
        if self._accept('NUM'):
            return int(self.current_token.value)
       
        elif self._accept('LPAREN'):
           
            expr_value = self.expr()

            
            self._expect('RPAREN')

            
            return expr_value
        else:
            raise SyntaxError('Expect NUMBER or LPAREN')


e = ExpressionEvaluator()

a = input("Enter the expression:")
print('answer ',
      e.parse(a))
