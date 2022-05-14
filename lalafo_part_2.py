import requests
import json
import pandas as pd
# from pandas import ExcelWriter
from datetime import datetime

"""
Вторая часть статьи: Парсер lalafo. Работа с API на сайте.
По всем возникшим вопросам, можете писать в группу https://vk.com/happython
Ссылка на статью: https://vk.com/@happython-parser-lalafo-rabota-s-api-saita
"""


def get_json(params):
    """получаем json с данными по заданным запросам"""
    url = f"https://lalafo.kg/api/search/v3/feed/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Accept": "application/json, text/plain, */*",
        "device": "pc"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def save_json(data):
    """сохрание ответа в файл для наглядного просмотра"""
    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_data.json')


def get_data_from_json(json_file):
    """собераем нужные нам данные из json"""
    domen_photo = 'https://img5.lalafo.com/i/posters/api'
    domen = 'https://lalafo.kg'
    # проходимся по данным и собираем в список то, что нам нужно
    result = []
    for d in json_file['items']:
        post_id = d['id']
        created_time = d['created_time']
        title = d['title']
        phone = d['mobile']
        description = d['description'].replace('\n', ' ')
        price = d['price']
        url_goods = d['url']
        try:
            image = domen_photo + d['image']
        except TypeError:
            image = 'без изображения'
        vip_post = d['is_vip']
        city = d['city']
        try:
            nameseller = d['user']['username']
        except:
            nameseller = ''

        result.append({
            'post_id': post_id,
            'created_time': datetime.fromtimestamp(created_time).strftime('%d-%m-%Y %H:%M:%S'),
            'city': city,
            'name_seller': nameseller,
            'phone': phone,
            'vip_status': vip_post,
            'title': title,
            'price': price,
            'description': description,
            'image': image,
            'url': domen + url_goods
        })
    return result


def save_excel(data):
    """сохранение результата в excel файл"""
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('lalafo_result.xlsx')
    df.to_excel(writer, 'data')
    writer.save()
    print('Все сохранено в lalafo_result.xlsx')


if __name__ == '__main__':
    params = {
        "expand": "url",
        'city_id': 103184,  # id города (пример: 103184 - Бишкек, 103209 - Джалал-Абад, 103218 - Ош и тд)
        'category_id': 1317,  # категория товара (пример: 1317 - Электроника, 1501 - Транспорт, 1484 - Животные и тд)
        'q': 'Xiaomi',  # поисковый запрос
        'price[from]': 10000,  # цена от указанного значения
        'price[to]': 30000,  # цена до указанного значения
        'currency': 'KGS',  # валюта. Доступны: KGS, USD
        'per-page': 500,  # количество результатов на странице
        'page': 1,  # номер страницы
        'sort_by': "price"
        # сортировка. Доступна: newest - сначало новые, price - цена по возрастанию, -price - цена по убыванию
    }
    data_json = get_json(params)
    # save_json(data)  # сохраняем в json файл
    result = get_data_from_json(data_json)
    save_excel(result)

    print(len(data_json['items']))  # выводим количество полученных записей
    # print(data_json['items'][0])

