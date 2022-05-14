import requests
import json


"""
Ниже описано получение json файла со всеми возможными фильтрами на сайте
Плюс из json достал все id доступных городов для более точного (узкого) поиска товара
"""

url = 'https://lalafo.kg/api/catalog/v3/params/filter?category_id=1501&'

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


with open('all_filters.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'Данные сохранены в all_filters.json')


# пример вывода всех id доступных городов
for d in data[1]['cities']['values']:
    print(f"Город: {d['value']} | id: {d['id']}")
