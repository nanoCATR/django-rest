# CRUD API with django

## Installation
After you cloned the repository, you want to create a virtual environment with all the required dependencies.
You can do this by running the command

```
pipenv install -r requirements.txt
```

## Structure

### Product
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`product` | GET | READ | Get all product
`product/:id` | GET | READ | Get a single product
`product`| POST | CREATE | Create a new product
`product/:id` | PUT | UPDATE | Update a product
`product/:id` | DELETE | DELETE | Delete a product
`product_amount_descrease/:id` | PATCH | PATCH | Descrease amount of a product

### ProductType
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`product` | GET | READ | Get all product
`product/:id` | GET | READ | Get a single product
`product`| POST | CREATE | Create a new product
`product/:id` | PUT | UPDATE | Update a product
`product/:id` | DELETE | DELETE | Delete a product

### Price
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`product` | GET | READ | Get all product
`product/:id` | GET | READ | Get a single product
`product`| POST | CREATE | Create a new product
`product/:id` | PUT | UPDATE | Update a product
`product/:id` | DELETE | DELETE | Delete a product