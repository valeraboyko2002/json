from typing import Any, Dict, List, Union, Optional
from .exceptions import JSONSyntaxError, JSONDepthError
from .lexer import JSONLexer

class JSONParser:
    """Парсер JSON с поддержкой потокового чтения"""

    MAX_DEPTH = 1000

    def __init__(self, max_depth: Optional[int] = None):
        self.max_depth = max_depth or self.MAX_DEPTH
        self.current_depth = 0

    def parse(self, json_string: str) -> Union[Dict, List]:
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
    
    def _parse_value(self, lexer: JSONLexer, token: tuple) -> Any:
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
    
    def _parse_object(self, lexer: JSONLexer) -> Dict:
        """Парсинг JSON-объекта"""
        self._check_depth()
        self.current_depth += 1 

        result = {}
        first = True

        while True:
            token = lexer.get_next_token()

            if token is None:
                raise JSONSyntaxError("Незакрытый объект")
            
            if token[0] == 'RBRACE':
                break
            
            if not first:
                if token[0] != 'COMMA':
                    raise JSONSyntaxError('Ожидалась запятая между элементами')
                token = lexer.get_next_token()
            
            if token[0] != 'STRING':
                raise JSONSyntaxError(f"Ключ объекта должен быть строкой, получено: {token[0]}")
            
            key = token[1]

            colon_token = lexer.get_next_token()
            if colon_token is None or colon_token[0] != 'COLON':
                raise JSONSyntaxError('Ожидалось двоеточие после ключа')
            
            value_token = lexer.get_next_token()
            if value_token is None:
                raise JSONSyntaxError('Ожидалось значение')
            
            result[key] = self._parse_value(lexer, value_token)
            first = False
        
        self.current_depth -= 1
        return result
    
    def _parse_array(self, lexer: JSONLexer) -> List:
        """Парсинг JSON-массива (ДОБАВЬТЕ ЭТОТ МЕТОД!)"""
        self._check_depth()
        self.current_depth += 1

        result = []
        first = True

        while True:
            token = lexer.get_next_token()

            if token is None:
                raise JSONSyntaxError("Незакрытый массив")
            
            if token[0] == 'RBRACKET':
                break
            
            if not first:
                if token[0] != 'COMMA':
                    raise JSONSyntaxError('Ожидалась запятая между элементами массива')
                token = lexer.get_next_token()
            
            result.append(self._parse_value(lexer, token))
            first = False
        
        self.current_depth -= 1
        return result
    
    def _check_depth(self):
        """Проверка глубины вложенности"""
        if self.current_depth >= self.max_depth:
            raise JSONDepthError(
                f'Превышена максимальная глубина вложенности: {self.max_depth}'
            )
    
    @staticmethod
    def parse_file(filepath: str, **kwargs) -> Union[Dict, List]:
        """Парсинг JSON из файла"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        parser = JSONParser(**kwargs)
        return parser.parse(content)

    @staticmethod
    def parse_stream(stream, chunk_size: int = 8192, **kwargs):
        """Потоковый парсинг больших JSON файлов"""
        # TODO: реализовать потоковый парсинг (хахахах)
        pass