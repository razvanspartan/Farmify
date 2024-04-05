def get_all_farms(sqlConnector):
    all_farms = []
    farms_raw_data = sqlConnector.search("farms", {})
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