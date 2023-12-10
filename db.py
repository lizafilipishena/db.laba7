db = {
    "mall_name": "Brosko Mall",
    "address": "ул. Пионерская, 2В",

    "place": [ # Места для аренды
        {
            "id": 1,
            "area": 50, # Площадь
            "status": True, # True - занята, False - не занято
            "shop_id": 1
        }, {
            "id": 2,
            "area": 30,
            "status": True,
            "shop_id": 2
        }, {
            "id": 3,
            "area": 47,
            "status": True,
            "shop_id": 3
        }, {
            "id": 4,
            "area": 20,
            "status": False
        }, {
            "id": 5,
            "area": 75,
            "status": False
        }
    ],

    "category": [ # Категория товаров
        {
            "id": 1,
            "name": 'Одежда'
        }, {
            "id": 2,
            "name": 'Бытовые товары'
        }, {
            "id": 3,
            "name": 'Техника'
        }
    ],

    "shops": [ # Магазины
        {
            "id": 1,
            "name": 'Guess',
            "category_id": 1,
            "place_id": 1
        }, {
            "id": 2,
            "name": 'MINISO',
            "category_id": 2,
            "place_id": 2
        }, {
            "id": 3,
            "name": 'DNS',
            "category_id": 3,
            "place_id": 3
        }, {
            "id": 4,
            "name": 'MVideo',
            "category_id": 3
        }
    ],

    "sellers": [ # Сотрудники (продавцы)
        {
            "id": 1,
            "name": "Екатерина Киреева",
            "shop_id": 1,
            "contacts": {
                "email": "Kireeva@example.com",
                "phone": "+1122334455"
            }
        }, {
            "id": 2,
            "name": "Варвара Волкова",
            "shop_id": 2,
            "contacts": {
                "email": "Volkova@example.com",
                "phone": "+6677889911"
            }
        }, {
            "id": 3,
            "name": "Алия Петрова",
            "shop_id": 3,
            "contacts": {
                "email": "Petrova@example.com",
                "phone": "+2233445566"
            }
        }
    ]
}

# Импортирование в файл
import json
with open('db', 'w') as outfile:
    json.dump(db, outfile, indent=3)