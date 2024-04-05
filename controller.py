import re


def get_all_farms(sqlConnector):
    all_farms = []
    farms_raw_data = sqlConnector.search("farms", {})
    print(farms_raw_data)
    for row in farms_raw_data:
        position_of_id = 0
        position_of_name = 2
        position_of_description = 3
        object = {"id": row[position_of_id],
                  "name": row[position_of_name],
                  "description": row[position_of_description]}

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

        matching_farm["id"] = row[position_of_id]
        matching_farm["owner"] = row[position_of_owner]
        matching_farm["name"] = row[position_of_name]
        matching_farm["description"] = row[position_of_description]
        matching_farm["latitude"] = row[position_of_latitude]
        matching_farm["longitude"] = row[position_of_longitude]
    return matching_farm

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

        matching_user["id"] = row[position_of_id]
        matching_user["is_farmer"] = row[position_of_is_farmer]
        matching_user["name"] = row[position_of_name]
        matching_user["email"] = row[position_of_email]
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


    userData = {"user_id": owner, "farm_name": name, "description": description, "latitude": latitude, "longitude": longitude}
    try:
        sqlConnector.insert("farms", userData)
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

    userData = {"farm_id": farm_id, "produce": produce, "stock": stock}
    try:
        sqlConnector.insert("farm_produce", userData)
        return {"code": 0, "message": "success"}
    except:
        return {"code": 1, "message": "error adding farm"}

def get_produce(requestData, sqlConnector):
    farm_id = requestData["farm_id"]
    allProduces = []
    produce_raw_data = sqlConnector.search("farm_produce", {"farm_id": farm_id})
    print(produce_raw_data)
    for row in produce_raw_data:
        print(f"ROW FOUND: {row}")
        position_of_id = 0
        position_of_farm_id = 1
        position_of_produce = 2
        position_of_stock = 3

        matching_produce = {}
        matching_produce["produce"] = row[position_of_produce]
        matching_produce["stock"] = row[position_of_stock]
        allProduces.append(matching_produce)
        print(f"ADDED TO ALLPRODUCES: {allProduces}")
    return allProduces