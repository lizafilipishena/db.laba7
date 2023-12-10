import components.sellers as seller
import components.category as category
import components.place as place
import components.shops as shop

"""""
Sellers commands:
1. Sellers.id - Получить id сотрудника по имени. (read)
2. Sellers.dismiss - Уволить сотрудника по id. (delete)
3. Sellers.employ - Нанять сотрудника. (create)
4. Sellers.update - обновление информации. (update)
"""""

while True:
    command = str(input('Введите команду: '))

    # Sellers.id
    if command == 'Sellers.id':
        name = str(input('Введите имя сотрудника: '))
        print(f'id сотрудника {name}: ', seller.sellers_get_one_by_name(name))

    # Sellers.dismiss
    if command == 'Sellers.dismiss':
        id = int(input('Введите id сотрудника: '))
        seller.sellers_delete_one_by_id(id)

    # Sellers.employ
    if command == 'Sellers.employ':
        name = str(input('Введите имя нового сотрудника: '))
        shop_id = int(input('id магазина, где работает сотрудник: '))
        email = str(input('Введите email сотрудника: '))
        phone = str(input('Введите телефон сотрудника: '))
        seller.sellers_create_one({
              "name": f"{name}",
              "shop_id": f'{shop_id}',
              "contacts": {
                  "email": f"{email}",
                  "phone": f"{phone}"
        }})

    # Sellers.update
    if command == 'Sellers.update':
        id = int(input('Введите id сотрудника для обновления информации: '))
        name = str(input('Введите имя нового сотрудника: '))
        shop_id = int(input('id магазина, где работает сотрудник: '))
        email = str(input('Введите email сотрудника: '))
        phone = str(input('Введите телефон сотрудника: '))
        seller.sellers_update_one_by_id(id, {
            "name": f"{name}",
            "shop_id": f'{shop_id}',
            "contacts": {
                "email": f"{email}",
                "phone": f"{phone}"
            }})

    """""
    Category commands:
    1. Category.id - Получить id категории товаров.
    2. Category.del - Удалить категорию товаров.
    3. Category.add - Добавить категорию товаров.
    """""

    # Category.id
    if command == 'Category.id':
        name = str(input('Введите название категории: '))
        print(f'id категории {name}: ', category.category_get_one_by_name(name))

    # Удалить категорию товаров
    if command == 'Category.del':
        id = int(input('Введите id категории: '))
        category.category_delete_one_by_id(id)

    # Добавить категорию товаров
    if command == 'Category.add':
        name = str(input('Введите новую категорию товаров: '))
        category.category_create_one({
              "name": f"{name}"
        })


    """""
    Place commands:
    1. Place.cnt - количество мест.
    2. Place.not.used - id всех свободных мест.
    3. Place.taken - Место заняли.
    4. Place.vacated - Место освободилось.
    """""
    if command == 'Place.cnt':
        print(place.place_cnt())

    if command == 'Place.not.used':
        print(place.place_not_used())

    if command == 'Place.taken':
        id = int(input('Введите id места: '))
        shop_id = int(input('Введите id магазина-арендатора: '))
        place.place_taken(id, shop_id)

    if command == 'Place.vacated':
        id = int(input('Введите id места: '))
        place.place_vacated(id)


    """""
    Shops commands:
    1. Shop.id - Получить id магазина.
    2. Shop.add - Добавить магазин.
    3. Shop.del - Удалить магазин.
    """""

    # Shop.id
    if command == 'Shop.id':
        name = str(input('Введите название магазина: '))
        print(f'id магазина {name}: ', shop.shop_get_one_by_name(name))

    # Shop.add
    if command == 'Shop.add':
        name = str(input('Введите название нового магазина: '))
        category_id = int(input('id категории товаров: '))
        shop.shop_create_one({
            "name": f"{name}",
            "category_id": f'{category_id}',
        })

    # Shop.del
    if command == 'Shop.del':
        id = int(input('Введите id магазина: '))
        shop.shops_delete_one_by_id(id)