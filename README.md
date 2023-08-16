# car_search-
API: Сервис поиска ближайших машин для перевозки грузов.

Сервис поддерживает следующие базовые функции:

- Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);
- Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));
- Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);\
- Редактирование машины по ID (локация (определяется по введенному zip-коду));
- Редактирование груза по ID (вес, описание);
- Удаление груза по ID.
- Фильтр списка грузов (вес, мили ближайших машин до грузов);

Список уникальных локаций представлен в прикрепленном csv файле "uszips.csv".

# Стек
Python/Django Rest Framework/PostgreSQL/Docker/docker-compose