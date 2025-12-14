import json
from typing import Dict, List
from .parser import JSONParser
from .exceptions import JSONValidationError

class JSONSchemaValidator:
    """Валидатор JSON по схеме (упрощенный)"""
    
    def __init__(self):
        self.parser = JSONParser()
    
    def validate_schema(self, json_data: Dict, schema: Dict) -> bool:
        """Проверка JSON по схеме"""
        # Простая реализация валидации
        if 'type' in schema:
            if schema['type'] == 'object':
                return self._validate_object(json_data, schema)
            elif schema['type'] == 'array':
                return self._validate_array(json_data, schema)
        return True
    
    def _validate_object(self, obj: Dict, schema: Dict) -> bool:
        """Валидация объекта"""
        if not isinstance(obj, dict):
            return False
        
        if 'properties' in schema:
            for prop, prop_schema in schema['properties'].items():
                if prop in obj:
                    if not self.validate_schema(obj[prop], prop_schema):
                        return False
                elif 'required' in prop_schema and prop_schema['required']:
                    return False
        
        return True
    
    def _validate_array(self, arr: List, schema: Dict) -> bool:
        """Валидация массива"""
        if not isinstance(arr, list):
            return False
        
        if 'items' in schema:
            for item in arr:
                if not self.validate_schema(item, schema['items']):
                    return False
        
        return True


class JSONBenchmark:
    
    @staticmethod
    def compare_performance(json_string: str, iterations: int = 1000):
        """Сравнение производительности"""
        import time
        parser = JSONParser()
        
        # ПАРСЕР
        start = time.time()
        for _ in range(iterations):
            parser.parse(json_string)
        custom_time = time.time() - start
        
        # NATIVE парсер
        start = time.time()
        for _ in range(iterations):
            json.loads(json_string)
        native_time = time.time() - start
        
        return {
            'custom_parser': custom_time,
            'native_parser': native_time,
            'ratio': custom_time / native_time
        }