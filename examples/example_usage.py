"""
Примеры использования моего JSON парсера
"""

from src.parser import JSONParser
from src.validator import JSONSchemaValidator

def main():
    print("=== Мой JSON Парсер ===")
    
    # Пример 1: Базовый парсинг
    parser = JSONParser()
    
    json_data = '''
    {
        "project": "My JSON Parser",
        "version": "1.0.0",
        "features": ["parsing", "validation", "streaming"],
        "author": {
            "name": "Ваше Имя",
            "email": "you@example.com"
        },
        "performance": {
            "benchmark": 95.5,
            "memory_efficient": true
        }
    }
    '''
    
    print("\n1. Парсинг сложного JSON:")
    parsed = parser.parse(json_data)
    print(f"Проект: {parsed['project']}")
    print(f"Версия: {parsed['version']}")
    print(f"Автор: {parsed['author']['name']}")
    
    # Пример 2: Валидация схемы
    print("\n2. Валидация по схеме:")
    
    schema = {
        "type": "object",
        "properties": {
            "project": {"type": "string"},
            "version": {"type": "string"},
            "author": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "required": True},
                    "email": {"type": "string"}
                }
            }
        }
    }
    
    validator = JSONSchemaValidator()
    if validator.validate_schema(parsed, schema):
        print("✓ JSON соответствует схеме")
    else:
        print("✗ Ошибка валидации схемы")
    
    # Пример 3: Обработка ошибок
    print("\n3. Обработка некорректного JSON:")
    
    invalid_json = '{"name": "Test", numbers: [1, 2, 3]}'
    
    try:
        parser.parse(invalid_json)
    except Exception as e:
        print(f"Обнаружена ошибка: {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()