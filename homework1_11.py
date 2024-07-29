import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#генерируем данные

books = ['Сказки Пушкина', 'Том Сойер', 'Гарри Поттер', 'Властелин Колец', 'Чук и Гек']
regions = ['Москва', 'Санкт-Петербург', 'Казань', 'Владивосток', 'Краснодар']
platforms = ['Озон', 'Вайлдберрис', 'Литрес']

index = pd.MultiIndex.from_product([books, regions, platforms], names=['Название книги', 'Регион продажи',
                                                                       'Онлайн магазин'])
sales_data = np.random.randint(500, 1500, size=(len(index), 1))
prices = np.random.randint(700, 1000, size=(len(index), 1))
total_sales = sales_data * prices
sales_df = pd.DataFrame(np.concatenate((sales_data, prices, total_sales), axis=1), index=index,
                        columns=['Количество проданных книг', 'Цена экземпляра', 'Объем продаж'])

#настройки для вывода таблиц
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#сводная таблица продаж по регионам и онлайн магазинам
sales_by_regions_platforms = sales_df.pivot_table(values='Объем продаж', index='Регион продажи',
                                                  columns='Онлайн магазин', aggfunc=np.sum)
print(f'\nПродажи по регионам и онлайн магазинам: \n{sales_by_regions_platforms}')

#сводная таблица продаж по онлайн магазинам
sales_by_book_platforms = sales_df.pivot_table(values='Объем продаж', index='Название книги',
                                                  columns='Онлайн магазин', aggfunc=np.sum)
print(f'\nПродажи книг по онлайн магазинам: \n{sales_by_book_platforms}')

#сводная таблица продаж по регионам
sales_by_book_regions = sales_df.pivot_table(values='Объем продаж', index='Название книги',
                                                  columns='Онлайн магазин', aggfunc=np.sum)
print(f'\nСводная таблица по продажам по книгам и регионам: \n{sales_by_book_regions}')

#визуализируем продажи по регионам
sales_by_book_regions.plot(kind='barh', figsize=(13,6))
plt.title('Продажи книг по регионам')
plt.xlabel('Объем продаж')
plt.ylabel('Название книги')
plt.show()

#визуализируем продажи по регионам и онлайн магазинам
sales_by_book_platforms.plot(kind='bar')
plt.title('Продажи книг по регионам и оналайн магазинам')
plt.xlabel('Регион продажи')
plt.ylabel('Объем продаж')
plt.show()

#визуализируем вклад каждой книги в суммарные продажи
total_sales_by_book = sales_by_book_platforms.sum(axis=1)
total_sales_by_book.plot(kind='pie', figsize=(10,6))
plt.title('Вклад каждой книги в суммарные продажи по регионам и магазинам')
plt.ylabel('')
plt.axis('equal')
plt.show()



