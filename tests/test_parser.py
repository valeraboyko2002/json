import unittest
import pytest
from src.parser import JSONParser
from src.exceptions import JSONSyntaxError, JSONDepthError

class TestJSONParser(unittest.TestCase):
    
    def setUp(self):
        self.parser = JSONParser()
    
    def test_parse_simple_object(self):
        json_str = '{"name": "John", "age": 30}'
        result = self.parser.parse(json_str)
        self.assertEqual(result, {"name": "John", "age": 30})
    
    def test_parse_nested_object(self):
        json_str = '{"user": {"name": "Alice", "settings": {"theme": "dark"}}}'
        result = self.parser.parse(json_str)
        expected = {"user": {"name": "Alice", "settings": {"theme": "dark"}}}
        self.assertEqual(result, expected)
    
    def test_parse_array(self):
        json_str = '[1, 2, 3, "four", true, null]'
        result = self.parser.parse(json_str)
        self.assertEqual(result, [1, 2, 3, "four", True, None])
    
    def test_invalid_json_missing_quote(self):
        json_str = '{"name": "John}'
        with self.assertRaises(JSONSyntaxError):
            self.parser.parse(json_str)
    
    def test_custom_max_depth(self):
        parser = JSONParser(max_depth=3)
        # Создаем глубоко вложенный JSON
        json_str = '{"a": {"b": {"c": {"d": 1}}}}'
        with self.assertRaises(JSONDepthError):
            parser.parse(json_str)
    
    def test_unicode_characters(self):
        json_str = '{"text": "Привет, мир! \u0422\u0435\u0441\u0442"}'
        result = self.parser.parse(json_str)
        self.assertEqual(result["text"], "Привет, мир! Тест")
    
    def test_scientific_notation(self):
        json_str = '{"small": 1.23e-10, "large": 2.5E+20}'
        result = self.parser.parse(json_str)
        self.assertAlmostEqual(result["small"], 1.23e-10)
        self.assertAlmostEqual(result["large"], 2.5e20)

# Запуск: python -m pytest tests/test_parser.py