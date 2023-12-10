import utils.json_service as json_service

# Полный список
def place_get_all():
    db = json_service.get_database()
    return db["place"]

def place_cnt():
    db = json_service.get_database()
    return len(db["place"])

def place_not_used():
    db = json_service.get_database()
    res = []
    for i, elem in enumerate(db["place"]):
        if elem["status"] == False:
            res.append(elem["id"])
    return res


def place_taken(id, shop_id):
    db = json_service.get_database()
    for i, elem in enumerate(db["place"]):
        if elem["status"] == True and elem["id"] == id:
            return print('Место уже занято!')
        if elem["status"] == False and elem["id"] == id:
            elem["status"] = True
            elem["shop_id"] = shop_id
            for i, elem in enumerate(db["shops"]):
                if elem["id"] == shop_id:
                    elem["place_id"] = id
            json_service.set_database(db)

def place_vacated(id):
    db = json_service.get_database()
    for i, elem in enumerate(db["place"]):
        if elem["status"] == False and elem["id"] == id:
            return print('Место уже свободно!')
        if elem["status"] == True and elem["id"] == id:
            elem["status"] = False
            del elem["shop_id"]
            json_service.set_database(db)