import requests
import json

"""
Ниже описано получение всех id категорий для более точного (узкого) поиска товара
"""

#  ссылка с категориями
url = 'https://lalafo.kg/api/proxy/catalog/categories/fullname'

#  нужные заголовки для получения данной страницы
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "device": "pc",
    "country-id": "12",
    "language": "ru_RU"
}

# сам запрос
r = requests.get(url, headers=headers)

data = r.json()

with open('all_categories.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'Данные сохранены в all_categories.json')

for d in data:
    print(f"Категория: {d[1]} | id: {d[0]}")
