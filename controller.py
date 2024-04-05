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