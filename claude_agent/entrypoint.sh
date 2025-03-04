#!/bin/bash

# Применяем миграции
echo "Applying database migrations..."
python manage.py migrate

# Собираем статические файлы
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Создаем суперпользователя, если его нет
echo "Checking for superuser..."
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(is_superuser=True).exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

# Запускаем сервер
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000 