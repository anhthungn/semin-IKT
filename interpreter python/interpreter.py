class Token:
    # Constructor method that initializes a new Token object
    def __init__(self, type, value=None): 
        self.type = type  # The type of the token (e.g., "number," "operator," "keyword")
        self.value = value # The value or content of the token (e.g., the actual number, operator, or keyword)

    def __repr__(self): # Representation method that returns a string representation of the Token object
        if self.value:
            return f'{self.type}: {self.value}'
        return f'{self.type}'

class Error(Exception):
    def __init__(self, error_name, details):
        super().__init__(f'{error_name}: {details}')
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

class BasicLexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def tokenize(self):
        tokens = []
        error = None

        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                tokens.extend(self.make_number())
            elif self.current_char.isalpha():
                tokens.append(self.make_identifier())
            elif self.current_char == '+':
                tokens.append(Token('PLUS'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token('MINUS'))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token('MULTI'))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token('DIV'))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token('LPAREN'))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token('RPAREN'))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token('EQUALS'))
                self.advance()
            elif self.current_char == '>':
                tokens.append(Token('GREATER_THAN'))
                self.advance()
            elif self.current_char == '<':
                tokens.append(Token('LESS_THAN'))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                error = IllegalCharError("'" + char + "'")

        tokens.append(Token('EOF'))
        return tokens, error
    
    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                dot_count += 1
                if dot_count > 1:
                    raise IllegalCharError("Invalid number format")
                num_str += '.'
            else:
                num_str += self.current_char

            self.advance()

        if dot_count == 0:
            return [Token('NUM', int(num_str))]
        else:
            return [Token('NUM', float(num_str))]

    def make_identifier(self):
        identifier = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            identifier += self.current_char
            self.advance()

        # Check if the identifier is a keyword
        keywords = {
            'IF': 'IF',
            'THEN': 'THEN',
            'ENDIF': 'ENDIF',
            'FOR': 'FOR',
            'NEXT': 'NEXT',
            'PRINT': 'PRINT',
            'ELSE': 'ELSE'
        }

        token_type = keywords.get(identifier.upper(), 'VAR')
        return Token(token_type, identifier)

class BasicParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = self.tokens.pop(0)

    def parse(self):
        result = self.statements()
        if self.current_token.type != 'EOF':
            raise Exception(f"Unexpected token: {self.current_token}")
        return result

    def advance(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = Token('EOF')

    def statements(self):
        while self.current_token.type != 'EOF':
            self.statement()

    def statement(self):
        if self.current_token.type == 'VAR':
            var_name = self.current_token.value
            self.match('VAR')
            if self.current_token.type == 'EQUALS':
                self.match('EQUALS')
                value = self.expr()
                env[var_name] = value
                print(f"OmenScript: {var_name} = {value}")
            else:
                raise Exception(f"Expected '=', but got {self.current_token.type}")
        elif self.current_token.type == 'PRINT':
            self.match('PRINT')
            value = self.expr()
            print(f"OmenScript: PRINT {value}")
        else:
            result = self.expr()
            print(f"OmenScript: {result}")

    def expr(self):
        return self.term()

    def term(self):
        result = self.factor()

        while self.current_token.type in ('MULTI', 'DIV'):
            token = self.current_token

            if token.type == 'MULTI':
                self.match('MULTI')
                result *= self.factor()
            elif token.type == 'DIV':
                self.match('DIV')
                divisor = self.factor()
                if divisor != 0:
                    result /= divisor
                else:
                    raise Exception("Division by zero")

        return result

    def factor(self):
        result = self.atom()

        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token

            if token.type == 'PLUS':
                self.match('PLUS')
                result += self.atom()
            elif token.type == 'MINUS':
                self.match('MINUS')
                result -= self.atom()

        return result

    def atom(self):
        token = self.current_token

        if token.type == 'NUM':
            self.match('NUM')
            return token.value
        elif token.type == 'VAR':
            var_name = token.value
            self.match('VAR')
            return env.get(var_name, 0)
        elif token.type == 'LPAREN':
            self.match('LPAREN')
            result = self.expr()
            self.match('RPAREN')
            return result

    def match(self, expected_type):
        if self.current_token.type == expected_type:
            self.current_token = self.tokens.pop(0)
        else:
            raise Exception(f"Expected {expected_type}, but got {self.current_token.type}")
        
env = {}

def run(text):
    lexer = BasicLexer(text)
    result = lexer.tokenize()
    tokens, error = result if isinstance(result, tuple) else (result, None)

    if error:
        return None, error.as_string()

    parser = BasicParser(tokens)
    try:
        parser_result = parser.parse()
        return parser_result, None
    except IllegalCharError as e:
        return None, f"Invalid Character: {e.details}"
    except Error as e:
        return None, f"Error: {e.as_string()}"
