# Claude Agent - Сервис для сравнения документов

Приложение для сравнительного анализа документов с использованием API Claude от Anthropic.

## Возможности

- Загрузка документов различных форматов (.txt, .docx, .pdf, .csv, .json)
- Сравнительный анализ документов с помощью Claude API
- Пользовательские запросы для анализа документов
- REST API для интеграции

## Поддерживаемые форматы

### Текстовые документы
- .txt - Текстовые файлы
- .docx - Microsoft Word
- .pdf - Adobe PDF
- .csv - Таблицы CSV
- .json - JSON-документы
- .xlsx - Microsoft Excel

## Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/ваш-username/claude-agent.git
cd claude-agent
```

2. Установить зависимости:
```bash
pip install -r requirements.txt
```

3. Создать и настроить файл .env:
```
CLAUDE_API_KEY=ваш_ключ_api_claude
MODEL_NAME=claude-3-haiku-20240307
```

4. Запустить миграции:
```bash
python manage.py migrate
```

5. Запустить сервер:
```bash
python manage.py runserver
```

## Лицензия

MIT 