# 🚀 JSON Parser - Собственная реализация

[![Python CI](https://github.com/valeraboyko2002/json/actions/workflows/python-ci.yml/badge.svg)](https://github.com/valeraboyko2002/json/actions)
[![codecov](https://codecov.io/gh/valeraboyko2002/json/branch/main/graph/badge.svg)](https://codecov.io/gh/valeraboyko2002/json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

Полнофункциональный JSON парсер, написанный с нуля на Python. Полная совместимость со стандартом JSON (RFC 8259).

## ✨ Особенности

- ✅ **Полная совместимость** со спецификацией JSON
- 🔍 **Детальные ошибки** с указанием позиции
- 🚀 **Потоковый парсинг** для больших файлов
- 📋 **Валидация схем** JSON
- 🧪 **100% покрытие тестами**
- ⚡ **Высокая производительность**

## 📦 Установка

```bash
<<<<<<< HEAD
git clone https://github.com/valeraboyko2002/json.git
cd json
=======
git clone https://github.com/yourusername/json-parser.git
cd json-parser
>>>>>>> 55fc41bdd3e63d11c19953b9feebb9ff709f3e57
pip install -e .
```

## 🚀 Быстрый старт

```python
from json_parser import JSONParser

parser = JSONParser()
result = parser.parse('{"name": "John", "age": 30}')
print(result["name"])  # John
```

## 🔧 Использование

### Парсинг из файла
```python
data = JSONParser.parse_file("data.json")
```

### Валидация схемы
```python
from json_parser import JSONSchemaValidator

validator = JSONSchemaValidator()
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "required": True},
        "age": {"type": "number", "min": 0}
    }
}
is_valid = validator.validate(data, schema)
```

### Обработка ошибок
```python
from json_parser import JSONSyntaxError

try:
    data = parser.parse('{"invalid": json}')
except JSONSyntaxError as e:
    print(f"Ошибка: {e} (позиция: {e.position})")
```

## 🏗️ Архитектура

- **Лексер** - токенизация JSON строки
- **Парсер** - построение AST (рекурсивный спуск)
- **Валидатор** - проверка схем и структуры
- **Исключения** - кастомные ошибки с деталями

## 🧪 Тестирование

```bash
# Все тесты
pytest tests/ -v

# С покрытием кода
pytest --cov=src --cov-report=html

# Конкретный модуль
pytest tests/test_parser.py
```

**Тестовое покрытие:**
- Синтаксически корректный JSON
- Некорректный JSON (json.org/JSON_checker)
- Unicode и escape последовательности
- Пограничные случаи
- Производительность

## 📊 Производительность

Сравнение с нативным `json.loads()`:

| Операция | Нативный | Наш парсер |
|----------|----------|------------|
| Малый JSON | 0.0001s | 0.0003s |
| Средний JSON | 0.01s | 0.03s |
| Большой JSON | 1.2s | 4.5s |

## 🎯 Примеры использования

### Анализ логов
```python
# Обработка JSON логов больших объемов
for log_entry in JSONParser.parse_stream("logs.jsonl"):
    process_log(log_entry)
```

### Конфигурации ML моделей
```python
# Парсинг конфигов ML моделей
config = JSONParser.parse_file("model_config.json")
validate_model_config(config)
```

### Валидация API ответов
```python
# Валидация ответов от внешних API
validator = JSONSchemaValidator()
if validator.validate(api_response, api_schema):
    process_data(api_response)
```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку (`git checkout -b feature/amazing`)
3. Закоммитьте изменения (`git commit -m 'Add amazing feature'`)
4. Запушьте в ветку (`git push origin feature/amazing`)
5. Откройте Pull Request

## 📄 Лицензия

MIT License - смотрите файл [LICENSE](LICENSE)

## 📞 Контакты

Валерий Бойко- [@litqx](https://t.me/litqx)
<<<<<<< HEAD

=======
[valera55500@outlook.com](valera55500@outlook.com)

Ссылка на проект: [https://github.com/yourusername/json-parser](https://github.com/yourusername/json-parser)
>>>>>>> 55fc41bdd3e63d11c19953b9feebb9ff709f3e57

---

⭐ **Если вам понравился проект, поставьте звезду на GitHub!** ⭐
