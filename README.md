# Тесты GET-методов API Центрального Банка РФ (ЦБ РФ)

Репозиторий содержит фреймворк для автоматизированного тестирования GET-методов API ЦБ РФ с использованием **Python**, **pytest** и **requests**.

[Сайт](https://www.cbr.ru)

### Требования

1. python3.12
2. pip
3. virtualenv. Установка: `sudo apt install python3-virtualenv`

# Запуск тестов
1. Клонирование репозитория
```
git clone https://github.com/krevedka2112/cbrf_api_testing.git
cd cbrf_api_testing
```

2. Настройка виртуального окружения и установка зависимостей
```
python3.12 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

3. Запуск всех тестов с выводом детальной информации
```
pytest -v
```

4. Логирование
Каждое обращение к API и ответы фиксируются в лог-файлах в папке /logs
