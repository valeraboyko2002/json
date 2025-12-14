from setuptools import setup, find_packages
import os

setup(
    name="json_parser",
    version="1.0.0",
    author="Valera Boyko",
    author_email="valera55500@outlook.com",
    description="A custom JSON parser implementation from scratch",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/valeraboyko2002/json",
    
    # Автоматически находит все пакеты
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # Зависимости
    install_requires=[],
    
    # Дополнительные зависимости для разработки
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    
    # Тесты
    test_suite="tests",
    
    # Классификаторы для PyPI
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
    
    python_requires=">=3.8",
    
    # Ключевые слова для поиска
    keywords="json parser parsing lexer validator",
    
    # Поддерживаемые команды
    # entry_points={
        # "console_scripts": [
            # "json-parser=json_parser.__main__:main",
        # ],
    # },
)

readme_path = "README.md"
if os.path.exists(readme_path):
    long_description = open(readme_path, encoding="utf-8").read()
else:
    long_description = "A custom JSON parser implementation from scratch"