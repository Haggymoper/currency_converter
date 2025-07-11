import os
import requests
from dotenv import load_dotenv


#Загружаем переменные из .env
load_dotenv()

#Читаем API-ключ
API_KEY = os.getenv("API_KEY")

#Проверяем, есть ли ключ
if not API_KEY:
    print("ОШибка: API-ключ не найден. Проверьте файл .env")
else:
    print("API-ключ найден")


#Тестовый запрос
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
responce = requests.get(url)

if responce.status_code == 200:
    print("API ключ работает")
    data = responce.json()
    print(f"Пример курса: 1 USD = {data['conversion_rates'] ['EUR']}EUR")