FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /app

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Создание директории для медиа-файлов
RUN mkdir -p /app/media

# Делаем entrypoint скрипт исполняемым
RUN chmod +x /app/entrypoint.sh

# Открытие порта
EXPOSE 8000

# Запуск через entrypoint
ENTRYPOINT ["/app/entrypoint.sh"] 