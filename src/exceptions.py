class JSONValidationError(Exception):
    """Базовые исключения для ошибок валидации JSON."""
    pass
    
class JSONSyntaxError(JSONValidationError):
    ''''Исключение для ошибок синтаксиса JSON.'''
    def __init__(self, message, position = None,char = None):
        self.postion = position
        self.char = char
        super().__init__(f"{message} на позиции {position} (символ: '{char}')"
                         if position else message)

class JSONEncodingError(JSONValidationError):
    """Ошибка кодировки/escape последовательностей в JSON"""
    pass

class JSONDepthError(JSONValidationError):
    """Ошибка превышения максимальной глубины вложенности JSON."""
    pass