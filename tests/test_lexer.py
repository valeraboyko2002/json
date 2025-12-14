# tests/test_lexer.py
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lexer import JSONLexer
from src.exceptions import JSONSyntaxError

class TestJSONLexer(unittest.TestCase):
    
    def test_tokenize_string(self):
        lexer = JSONLexer('"hello world"')
        token = lexer.get_next_token()
        self.assertEqual(token, ('STRING', 'hello world'))
    
    def test_tokenize_number(self):
        test_cases = [
            ('123', 123),
            ('-456', -456),
            ('3.14', 3.14),
            ('1.23e-10', 1.23e-10),
            ('2.5E+20', 2.5e20),
        ]
        
        for input_str, expected in test_cases:
            with self.subTest(input=input_str):
                lexer = JSONLexer(input_str)
                token = lexer.get_next_token()
                self.assertEqual(token, ('NUMBER', expected))
    
    def test_tokenize_boolean(self):
        lexer = JSONLexer('true')
        token = lexer.get_next_token()
        self.assertEqual(token, ('TRUE', True))
        
        lexer = JSONLexer('false')
        token = lexer.get_next_token()
        self.assertEqual(token, ('FALSE', False))
    
    def test_tokenize_null(self):
        lexer = JSONLexer('null')
        token = lexer.get_next_token()
        self.assertEqual(token, ('NULL', None))
    
    def test_tokenize_punctuation(self):
        lexer = JSONLexer('{}[]:,')
        expected_tokens = [
            ('LBRACE', '{'),
            ('RBRACE', '}'),
            ('LBRACKET', '['),
            ('RBRACKET', ']'),
            ('COLON', ':'),
            ('COMMA', ','),
        ]
        
        for expected in expected_tokens:
            token = lexer.get_next_token()
            self.assertEqual(token, expected)
    
    def test_whitespace_handling(self):
        lexer = JSONLexer('  \n\t{ "key" : 123 }  ')
        tokens = []
        while True:
            token = lexer.get_next_token()
            if token is None:
                break
            tokens.append(token[0])
        
        self.assertEqual(tokens, ['LBRACE', 'STRING', 'COLON', 'NUMBER', 'RBRACE'])
    
    def test_unicode_escape(self):
        lexer = JSONLexer(r'"\u041f\u0440\u0438\u0432\u0435\u0442"')
        token = lexer.get_next_token()
        self.assertEqual(token[1], 'Привет')
    
    def test_invalid_token(self):
        lexer = JSONLexer('@invalid')
        with self.assertRaises(JSONSyntaxError):
            lexer.get_next_token()

if __name__ == '__main__':
    unittest.main()