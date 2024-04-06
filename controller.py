import re


def get_all_farms(sqlConnector):
    all_farms = []
    farms_raw_data = sqlConnector.search("farms", {})
    print(farms_raw_data)
    for row in farms_raw_data:
        position_of_id = 0
        position_of_name = 2
        position_of_description = 3
        position_of_image = 7
        object = {"id": row[position_of_id],
                  "name": row[position_of_name],
                  "description": row[position_of_description],
                  "image": row[position_of_image]}

        all_farms.append(object)
    return all_farms


def get_farm(requestData, sqlConnector):
    id = requestData["id"]
    matching_farm = {}
    farms_raw_data = sqlConnector.search("farms", {"farm_id": id})
    print(farms_raw_data)
    for row in farms_raw_data:
        print(row)
        position_of_id = 0
        position_of_owner = 1
        position_of_name = 2
        position_of_description = 3
        position_of_latitude = 4
        position_of_longitude = 5
        position_of_orders = 6
        position_of_image = 7

        matching_farm["id"] = row[position_of_id]
        matching_farm["owner"] = row[position_of_owner]
        matching_farm["name"] = row[position_of_name]
        matching_farm["description"] = row[position_of_description]
        matching_farm["latitude"] = row[position_of_latitude]
        matching_farm["longitude"] = row[position_of_longitude]
        matching_farm["orders"] = row[position_of_orders]
        matching_farm["image"] = row[position_of_image]
    return matching_farm

def get_farms(requestData, sqlConnector):
    id = requestData["id"]
    farms_raw_data = sqlConnector.search("farms", {"user_id": id})
    print(farms_raw_data)
    good_data = []
    for row in farms_raw_data:
        print(row)
        position_of_id = 0
        position_of_owner = 1
        position_of_name = 2
        position_of_description = 3
        position_of_latitude = 4
        position_of_longitude = 5
        position_of_orders = 6
        position_of_image = 7

        matching_farm = {}
        matching_farm["id"] = row[position_of_id]
        matching_farm["owner"] = row[position_of_owner]
        matching_farm["name"] = row[position_of_name]
        matching_farm["description"] = row[position_of_description]
        matching_farm["latitude"] = row[position_of_latitude]
        matching_farm["longitude"] = row[position_of_longitude]
        matching_farm["orders"] = row[position_of_orders]
        matching_farm["image"] = row[position_of_image]
        good_data.append(matching_farm)
    return good_data

def get_user(requestData, sqlConnector):
    id = requestData["id"]
    matching_user = {}
    farms_raw_data = sqlConnector.search("users", {"user_id": id})
    print(farms_raw_data)
    for row in farms_raw_data:
        print(row)
        position_of_id = 0
        position_of_is_farmer = 1
        position_of_name = 2
        position_of_email = 3
        position_of_subscription = 4

        matching_user["id"] = row[position_of_id]
        matching_user["is_farmer"] = row[position_of_is_farmer]
        matching_user["name"] = row[position_of_name]
        matching_user["email"] = row[position_of_email]
        matching_user["subscription_type"] = row[position_of_subscription]
    return matching_user

def add_user(requestData, sqlConnector):
    id = requestData["id"]
    is_farmer = requestData["is_farmer"]
    name = requestData["name"]
    email = requestData["email"]
    # re.match(email, "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,}$")
    # T0DO when having time do this

    userData = {"user_id": id, "is_farmer": is_farmer, "name": name, "email": email}
    try:
        sqlConnector.insert("users", userData)
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding user"}


def add_farm(requestData, sqlConnector):
    owner = requestData["owner"]
    name = requestData["name"]
    description = requestData["description"]
    latitude = requestData["latitude"]
    longitude = requestData["longitude"]
    image = requestData["image"]

    farmData = {"user_id": owner, "farm_name": name, "description": description, "latitude": latitude, "longitude": longitude, "image": image}
    print(farmData)
    try:
        sqlConnector.insert("farms", farmData)
        userData = get_user({"id": owner}, sqlConnector)
        if userData["is_farmer"] == 0:
            update_user({"id": owner, "is_farmer": 1}, sqlConnector)
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding farm"}


def update_user(requestData, sqlConnector):
    id = requestData["id"]
    requestData.pop("id")
    userDataToUpdate = requestData
    try:
        sqlConnector.update("users", userDataToUpdate, {"user_id": id})
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding user"}

def update_farm(requestData, sqlConnector):
    farm_id = requestData["id"]
    requestData.pop("id")
    userDataToUpdate = requestData
    try:
        sqlConnector.update("farms", userDataToUpdate, {"farm_id": farm_id})
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding user"}

def add_produce(requestData, sqlConnector):
    farm_id = requestData["farm_id"]
    produce = requestData["produce"]
    stock = requestData["stock"]
    price = requestData["price"]

    userData = {"farm_id": farm_id, "produce": produce, "stock": stock, "price": price}
    try:
        sqlConnector.insert("farm_produce", userData)
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding farm"}


def get_produce_data(requestData, sqlConnector):
    try:
        farm_id = requestData["farm_id"]
        produce_raw_data = sqlConnector.search("farm_produce", {"farm_id": farm_id})
    except KeyError:
        produce_id = requestData["produce_id"]
        produce_raw_data = sqlConnector.search("farm_produce", {"id": produce_id})
    return produce_raw_data


def get_produce(requestData, sqlConnector):
    produce_raw_data = get_produce_data(requestData, sqlConnector)
    allProduces = []
    print("\n\n\n\n\n\nAICI\n\n\n")
    print(produce_raw_data)
    import pdb; pdb.set_trace()
    for row in produce_raw_data:
        print(f"ROW FOUND: {row}")
        position_of_id = 0
        position_of_farm_id = 1
        position_of_produce = 2
        position_of_stock = 3
        position_of_price = 4

        matching_produce = {}
        matching_produce["id"] = row[position_of_id]
        matching_produce["produce"] = row[position_of_produce]
        matching_produce["stock"] = row[position_of_stock]
        matching_produce["price"] = row[position_of_price]
        allProduces.append(matching_produce)
        print(f"ADDED TO ALLPRODUCES: {allProduces}")
    return allProduces

def increase_orders_to_farm(requestData, sqlConnector):
    update_farm(requestData, sqlConnector)

def add_order(requestData, sqlConnector):
    user_id = requestData["user_id"]
    produce_id = requestData["produce_id"]
    amount = requestData["amount"]

    position_of_farm_id = 1
    position_of_stock = 3

    produce = get_produce_data({"produce_id": produce_id}, sqlConnector)[0]
    if produce[position_of_stock] < amount:
        return {"code": 2, "message": "not enough stock"}
    orderData = {"user_id": user_id, "produce_id": produce_id, "amount": amount}
    farm_id = produce[position_of_farm_id]
    print(farm_id)
    farm_data = get_farm({"id": farm_id}, sqlConnector)
    print(farm_data)
    farm_orders = int(farm_data["orders"]) + 1
    try:
        sqlConnector.insert("order_list", orderData)
        increase_orders_to_farm({"id": farm_id, "order_number": farm_orders}, sqlConnector)
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding farm"}


def get_farm_orders(requestData, sqlConnector):
    farm_id = requestData["farm_id"]
    farm_produce = get_produce_data({"farm_id": farm_id}, sqlConnector)
    farm_orders = []
    for produce in farm_produce:
        produce_id = produce[0]
        newData = sqlConnector.search("order_list", {"produce_id": produce_id})
        farm_orders += newData
    return farm_orders

def get_orders(requestData, sqlConnector):
    try:
        id = requestData["user_id"]
        orders_raw_data = sqlConnector.search("order_list", {"user_id": id})
    except KeyError:
        id = requestData["farm_id"]
        orders_raw_data = get_farm_orders({"farm_id": id}, sqlConnector)
    print(orders_raw_data)
    good_data = []
    for row in orders_raw_data:
        print(row)
        position_of_order_id = 0
        position_of_produce_id = 2
        position_of_amount = 3
        produce = get_produce_data({"produce_id": row[position_of_produce_id]}, sqlConnector)[0]
        position_of_user_id = 1

        matching_order = {}
        matching_order["order_id"] = row[position_of_order_id]
        matching_order["produce_id"] = row[position_of_produce_id]
        matching_order["produce_name"] = produce[2]
        matching_order["amount"] = row[position_of_amount]
        matching_order["user_id"] = row[position_of_user_id]

        good_data.append(matching_order)
    return good_data

def delete_produce(requestData, sqlConnector):
    id = requestData["produce_id"]
    where_condition = {"id": id}
    try:
        sqlConnector.delete("farm_produce", where_condition)
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding farm"}

def update_produce(requestData, sqlConnector):
    id = requestData["id"]
    requestData.pop("id")
    userDataToUpdate = requestData
    try:
        sqlConnector.update("farm_produce", userDataToUpdate, {"id": id})
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error editing produce"}


def complete_order(requestData, sqlConnector):
    id = requestData["id"]
    farm_id = requestData["farm_id"]
    farm_data = get_farm({"id": farm_id}, sqlConnector)
    print(farm_data)
    farm_orders = int(farm_data["orders"]) - 1
    try:
        sqlConnector.delete("farm_produce", {"id": id})
        increase_orders_to_farm({"id": farm_id, "farm_orders": farm_orders}, sqlConnector)
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error editing produce"}