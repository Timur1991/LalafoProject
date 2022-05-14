import requests
import json
import pandas as pd
from datetime import datetime

"""
Просто тестировал API через постановку в ссылку переменных
"""

# создадим переменные с некоторыми параметрами для примера
per_page = 100  # количество записей на странице
city_id = 103184  # id города "Бишкек"(можно составить список)
category_id = 1357  # id категории "Мобильные телефоны и аксессуары"(можно стаставить список)
price_from = 20000  # цена от указанного значения
price_to = 30000  # цена до указанного значения
currency = "KGS"  # валюта. Доступны: KGS, USD
sort_by = "newest"  # сортировка. Доступна: newest - сначало новые, price - цена по возрастанию, -price - цена по убыванию

# теперь подставим их в наш ссылку
url = f"https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page={per_page}&city_id={city_id}&category_id={category_id}&parameters[29][0]=2757&price[from]={price_from}&price[to]={price_to}&sort_by={sort_by}&parameters[425][0]=27240&parameters[425][1]=27241&parameters[425][2]=27236&currency={currency}"

# добавим свои заголовки
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept": "application/json, text/plain, */*",
    "device": "pc"
}

# получаем наш ответ в json формате
response = requests.get(url, headers=headers)
data = response.json()


# # сохраним ответ в файл для наглядного просмотра
# with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
#     json.dump(data, file, indent=2, ensure_ascii=False)
#     print(f'Данные сохранены в test_lalafo_data.json')


domen_photo = 'https://img5.lalafo.com/i/posters/api'
domen = 'https://lalafo.kg'

# проходимся по данным и собираем в список то, что нам нужно
result = []
for d in data['items']:
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
    print(f'id поста: {post_id}\nНазвание поста: {title}\nНомер продавца: phone\nЦена: {price}\nОписание товара:'
          f'\n{description}\nСсылка на фото товара:{image}\nСсылка на товар: {domen + url_goods}\n')
    result.append({
        'post_id': post_id,
        'created_time': datetime.fromtimestamp(created_time).strftime('%d-%m-%Y %H:%M:%S'),
        'title': title,
        'phone': phone,
        'price': price,
        'description': description,
        'image': image,
        'url': domen + url_goods
    })

df = pd.DataFrame(result)
writer = pd.ExcelWriter('lalafo_result.xlsx')
df.to_excel(writer, 'data')
writer.save()
print('Все сохранено в lalafo_result.xlsx')

print(len(data['items']))


