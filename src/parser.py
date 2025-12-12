from typing import Any, Dict, List, Union
from .exceptions import JSONSyntaxError, JSONDepthError
from .lexer import JSONLexer

class JSONParser:
    """Парсер JSON с поддержкой потокового чтения"""

    MAX_DEPTH = 1000

    def __init__(self,max_depth: int = None):
        self.max_depth = max_depth or self.MAX_DEPTH
        self.current_depth = 0

    def parse(self, json_string: str) -> Union[Dict,list]:
        """Основной метод парсинга JSON-строки."""
        lexer = JSONLexer(json_string)
        self.current_depth = 0

        token = lexer.get_next_token()
        if token is None:
            raise JSONSyntaxError("Пустая JSON-строка")
        
        result = self._parse_value(lexer, token)

        # проверка на лишние токены 
        next_token = lexer.get_next_token()
        if next_token is not None:
            raise JSONSyntaxError(f"Лишние символы в конце: {next_token[1]}")
        
        return result
    
    def _parse_value(self,lexer: JSONLexer, token: tuple):
        """Парсинг значений JSON"""
        token_type, token_value = token

        if token_type == 'LBRACE':
            return self._parse_object(lexer)
        elif token_type == 'LBRACKET':
            return self._parse_array(lexer)
        elif token_type in ('STRING', 'NUMBER', 'TRUE', 'FALSE', 'NULL'):
            return token_value
        else:
            raise JSONSyntaxError(f"Ожидалось значение, получено: {token_type}")
        
    
    def _parse_object(self,lexer: JSONLexer) -> Dict:
        pass