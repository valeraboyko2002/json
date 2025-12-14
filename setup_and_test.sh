#!/bin/bash
# Сохраните как setup_and_test.sh

echo "=== Настройка проекта JSON Parser ==="

# 1. Создаем виртуальное окружение
echo "1. Создаю виртуальное окружение..."
python3 -m venv venv

# 2. Активируем
echo "2. Активирую окружение..."
source venv/bin/activate

# 3. Устанавливаем зависимости
echo "3. Устанавливаю pytest..."
pip install pytest

# 4. Запускаем тесты
echo "4. Запускаю тесты лексера..."
python -m pytest tests/test_lexer.py -v

echo "5. Запускаю все тесты..."
python -m pytest tests/ -v

# 5. Деактивируем
echo "6. Деактивирую окружение..."
deactivate

echo "=== Готово! ==="