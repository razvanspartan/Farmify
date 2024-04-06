# Farmify API documentation

### Base url:
```
https://domain.com/api/
```

## Endpoints


### /test
Method: GET, POST
Description: Test endpoint to check if the API is working.
Request: N/A (GET), JSON data (POST)
Response: JSON data

```
json
{
    "test": "test2"
}
```


### /add_farm
Method: POST
Description: Add a new farm to the system.

Request: JSON data

```
{
  owner: User ID of the farm owner
  name: Name of the farm
  description: Description of the farm
  latitude: Latitude of the farm location
  longitude: Longitude of the farm location
}
```
Response: JSON data

```
{
code: 0 for success, 1 for failure
message: Success or failure message
}
```


### /get_all_farms
Method: GET
Description: Get information about all farms.
Request: N/A
Response: JSON array of farm objects
```
[
    {
        "description": farm descripton,
        "id": the id of the farm,
        "name": the farm name
    },
    {...}
]
```


### /get_farm
Method: POST
Description: Get information about a specific farm.
Request: JSON data
```
{
  id: ID of the farm
}
```
Response: JSON data of the farm
```
{
    "description": farm descripton,
    "id": the id of the farm,
    "name": the farm name
    "latitude": coordinate,
    "longitude": coordinate,
    "owner": farm owner,
    "orders": number of active orders
}
```


### /add_user
Method: POST
Description: Add a new user to the system.
Request: JSON data
```
{
  id: User ID
  is_farmer: Boolean indicating if the user is a farmer
  name: Name of the user
  email: Email of the user
}
```
Response: JSON data
```
{
  code: 0 for success, 1 for failure
  message: Success or failure message
}
```

### /get_user
Method: POST
Description: Get information about a specific user.
Request: JSON data
```
{
  id: ID of the user
}
```
Response: JSON data of the user
```
{
    "email": "user@example.com",
    "id": "User123",
    "is_farmer": true,
    "name": "John Doe"
}
```

### /update_user
Method: POST
Description: Update information about a user.
Request: JSON data
```
{
  id: ID of the user
(Optional) is_farmer: Updated value for the is_farmer field
(Optional) name: Updated value for the name field
(Optional) email: Updated value for the email field
}
```
Response: JSON data
```
{
  code: 0 for success, 1 for failure
  message: Success or failure message
}
```

### /update_farm
Method: POST
Description: Update information about a farm.
Request: JSON data
```
{
  id: ID of the farm
(Optional) user_id: Updated value for the user_id field
(Optional) farm_name: Updated value for the farm_name field
(Optional) description: Updated value for the description field
(Optional) latitude: Updated value for the latitude field
(Optional) longitude: Updated value for the longitude field
}
```
Response: JSON data
```
{
  code: 0 for success, 1 for failure
  message: Success or failure message
}
```

### /add_produce
Method: POST
Description: Add produce to a farm.
Request: JSON data
```
{
  farm_id: ID of the farm
  produce: Name of the produce
  stock: Stock of the produce
}
```
Response: JSON data
```
{
code: 0 for success, 1 for failure
message: Success or failure message
}
```

### /get_produce
Method: POST
Description: Get produce details of a farm.
Request: JSON data
```
{
  farm_id: ID of the farm
}
```
Response: JSON array of produce objects
```
[
    {
        "id:: the id of the produce
        "produce": name of the produce,
        "stock": quantity available (float)
        "price": the price of the produce
    },
    {
        ...
    }
]
```

### /get_farms
Method: POST
Description: Get farms owned by a user.
Request: JSON data
```
{
  id: User ID
}
```
Response: JSON array of farm objects
```
[
    {
        "description": farm descripton,
        "id": the id of the farm,
        "name": the farm name
        "latitude": coordinate,
        "longitude": coordinate,
        "owner": farm owner,
        "orders": number of active orders
    },
    {...}
]
```

### /add_order
Method: POST
Description: Add an order to the system.
Request: JSON data
```
{
  user_id: ID of the user placing the order
  produce_id: ID of the produce being ordered
  amount: Amount of produce ordered
}
```
Response: JSON data
```
{
  code: 0 for success, 1 for failure, 2 for insufficient amount  
  message: Success or failure message
}
```

### /get_orders
Method: POST
Description: Get orders placed by a user or received by a farm.
Request: JSON data
Either:
```
{
  user_id: User ID (for personal account)
}
```
or
```
{
  farm_id: Farm ID (for business use)
}
```
Response: JSON array
```
[
  {
    user_id: ID of the user placing the order
    produce_id: ID of the produce being ordered
    amount: Amount of produce ordered
  },
  {...}
]
```

### /delete_produce
Method: POST
Description: Delete produces by given data
Request: JSON data
```
{
  product_id: product ID
}
```
Response: JSON data
```
{
  code: 0 for success, 1 for failure
  message: Success or failure message
}
```
