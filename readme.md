# Supermarket Checkout
Simple app to add Items, Offers and handle Billing


## Environment Variables

Pleas add this environment variables to your .env file in project root directory.
Also Add values accordingly


`DB_ENGINE=django.db.backends.postgresql` #Use according to desired engine and db service

`DB_NAME=`

`DB_USER=`

`DB_PASSWORD=`

`DB_HOST=`

`DB_PORT=`




## Installation

Install Checkout Kata App with Docker

```bash
  docker-compose up --build -d
  docker exec -it kata-web python manage.py migrate
```
Load Data/Fixtures
```
docker exec -it kata-web python manage.py loaddata fixtures/items_data.json
docker exec -it kata-web python manage.py loaddata fixtures/offers_data.json
```
    