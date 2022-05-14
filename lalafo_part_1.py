import requests
import json

"""
Первая часть статьи: Парсер lalafo. Поиск API на сайте.
По всем возникшим вопросам, можете писать в группу https://vk.com/happython
Ссылка на статью: https://vk.com/@happython-parser-lalafo-poisk-api-na-saite
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "device": "pc"
}


url = 'https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=40&category_id=1357'

r = requests.get(url, headers=headers)

data = r.json()
# print(data)

# сохраняем в json для наглядности
with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'Данные сохранены в lalafo_data.json')


# чтение с json файла
with open('lalafo_data.json', encoding='UTF-8') as file:
    data_from_json = json.load(file)


# пример информации об одном товаре и его продавце
print(data_from_json['items'][0])
