class JSONLexer:
    """Лексер для токенизации JSON-строк."""

    def __init__(self,text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position] if self.text else None

    def advance(self):
        """Перемещает указатель на следующий символ в тексте."""
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
        else:
            self.current_char = None
    
    def skip_whitespace(self):
        """Пропускает пробельные символы."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def scan_string(self):
        """Сканирует строковый литерал JSON."""

        result = ''
        self.advance()  # Пропускаем начальную кавычку

        while self.current_char != '"':
            if self.current_char is None:
                raise JSONSyntaxError("Неожиданный конец строки при разборе строки", self.position)

            if self.current_char == '\\':
                self.advance()
                result.append(self._parse_escape_sequence())
            else:
                result.append(self.current_char)
                self.advance()
        
        self.advance()  # Пропускаем конечную кавычку
        return ''.join(result)
    
    def _parse_escape_sequence(self):
        """Парсит escape-последовательности в строках JSON."""
        escape_map = {
            '"': '"',
            '\\': '\\',
            '/': '/',
            'b': '\b',
            'f': '\f',
            'n': '\n',
            'r': '\r',
            't': '\t'
        }

        if self.current_char in escape_map:
            return escape_map[self.current_char]
        elif self.current_char == 'u':
            hex_digits = ''.join([self._next_chair() for _ in range(4)])
            try:
                return chr(int(hex_digits, 16))
            except ValueError:
                raise JSONEncodingError(f"Некорректная Unicode escape-последовательность: \\u{hex_digits}")
        raise JSONEncodingError(f"Недопустимая escape последовательность: \\{self.current_char}")

    def _next_chair(self):
        """Возвращает следующий символ и продвигает указатель."""
        self.advance()
        if self.current_char is None:
            raise JSONSyntaxError("Неожиданный конец строки при разборе escape-последовательности", self.position)
        return self.current_char 

    def scan_number(self):
        """Сканировать число"""
        start_pos = self.position
# знак
        if self.current_char == '-':
            self.advance()

        # целая часть 
        if self.current_char == '0':
            self.advance()
        elif self.current_char and self.current_char.isdigit():
            while self.current_char and self.current_char.isdigit():
                self.advance()
            else:
                return None
        
        # дробная часть
        if self.current_char == '.':
            self.advance()
            if not (self.current_char and self.current_char.isdigit()):
                raise JSONSyntaxError("Ожидалась цифра после десятичной точки", self.position)
            while self.current_char and self.current_char.isdigit():
                self.advance()
        
        # экспонента
        if self.current_char and self.current_char.lower() == 'e':
            self.advance()
            if self.current_char in ('+', '-'):
                self.advance()
            if not (self.current_char and self.current_char.isdigit()):
                raise JSONSyntaxError("Ожидалась цифра в экспоненте", self.position)
            while self.current_char and self.current_char.isdigit():
                self.advance()
        
        number_str = self.text[start_pos:self.position]
        try:
            if '.' in number_str or 'e' in number_str.lower():
                return float(number_str)
            return int(number_str)
        except ValueError:
            raise JSONSyntaxError(f"Некорректный формат числа: {number_str}", start_pos)
        
        
        
        def get_next_token(self):
            """Возвращает следующий токен из входного текста."""
            self.skip_whitespace()

            if self.current_char is None:
                return None
        
            # Строки
            if self.current_char == '"':
                return ('STRING', self.scan_string())
            
            # Числа
            number = self.scan_number()
            if number is not None:
                return ('NUMBER', number)
            
            # Ключевые слова 
            if self.current_chat.isalpha():
                start_pos = self.position
                while self.current_char and self.current_char.isaplha():
                    self.advance()
                keyword = self.text[start_pos:self.position]

                if keyword == 'true':
                    return ('TRUE', True)
                elif keyword == 'false':
                    return ('FALSE', False)
                elif keyword == 'null':
                    return ('NULL', None)
                else:
                    raise JSONSyntaxError(f"Неизвестное ключевое слово: {keyword}", start_pos)
            
            # Символы пунктуации
            char = self.current_char
            self.advance()

            single_chars = {
                '{': 'LBRACE',
                '}': 'RBRACE',
                '[': 'LBRACKET',
                ']': 'RBRACKET',
                ',': 'COMMA',
                ':': 'COLON'
            }
            if char in single_chars:
                return (single_chars[char], char)
            
            raise JSONSyntaxError(f"Недопустимый символ: '{char}'", self.position - 1, char)    