# Используйте официальный образ Python
FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы в контейнер
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY weather_bot.py ./

# Установите переменные окружения для токенов
ENV TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
ENV YANDEX_API_KEY=YOUR_YANDEX_API_KEY

# Запустите бота
CMD ["python", "weather_bot.py"]