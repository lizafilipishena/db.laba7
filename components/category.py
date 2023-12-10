import utils.json_service as json_service

# Полный список
def category_get_all():
    db = json_service.get_database()
    return db["category"]

# Получить id категории товаров
def category_get_one_by_name(name):
    db = json_service.get_database() #Чтение базы данных
    for elem in db["category"]:
        if elem["name"] == name:
            return elem['id']
    return {"message": f"Элемент с {name} не найден"}

# Удалить категорию товаров
def category_delete_one_by_id(id):
    db = json_service.get_database() # Чтение базы данных
    for i, elem in enumerate(db["category"]):
        if elem["id"] == id:
            candidate = db["category"].pop(i)
            json_service.set_database(db) # Перезапись базы данных
            return candidate
    return {"message": f"Элемент с {id} не найден"}

# Добавить категорию товаров
def category_create_one(category):
    db = json_service.get_database() # Чтение базы данных
    last_category_id = category_get_all()[-1]["id"]
    db["category"].append({"id": last_category_id + 1, **category})
    json_service.set_database(db) # Перезапись базы данных