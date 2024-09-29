import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Установите логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Замените на ваш токен и API ключ
TELEGRAM_TOKEN = '7728937605:AAFoXtLHtn52CvTzi-qmWs-64V7q6kdeb18'
YANDEX_API_KEY = '0934f506-5f12-4d25-aa36-f39ec534e9dd'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Напиши мне название города, и я отправлю тебе погоду.')

def get_weather(city: str) -> str:
    url = f'https://api.weather.yandex.ru/v2/informers?lat={city["lat"]}&lon={city["lon"]}'
    headers = {'X-Yandex-API-Key': YANDEX_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['fact']['temp']
        condition = weather_data['fact']['condition']
        return f"Температура в {city['name']}: {temperature}°C, Состояние: {condition}."
    else:
        return "Не удалось получить данные о погоде."

def weather(update: Update, context: CallbackContext) -> None:
    city_name = ' '.join(context.args)
    if not city_name:
        update.message.reply_text('Пожалуйста, укажите название города.')
        return

    # Используем простой механизм для получения координат (можно улучшить)
    city_coords = {
        "Москва": {"lat": 55.7558, "lon": 37.6173},
        "Санкт-Петербург": {"lat": 59.9343, "lon": 30.3351},
        # Добавьте больше городов по мере необходимости
    }

    city = city_coords.get(city_name)
    if city:
        weather_info = get_weather(city)
        update.message.reply_text(weather_info)
    else:
        update.message.reply_text("Город не найден. Попробуйте другой.")

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("weather", weather))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()