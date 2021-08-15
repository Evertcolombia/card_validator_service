# Card payment validation
------------

# Installing
------------

# Docker-Compose

```
docker-compose up -d
```

This command will sintall the docker env for our service
and will be run on 0.0.0.0:8000



## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `cards`, so we will use the following URLS - `/cards/` and `/cards/<card_num>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`cards/` | GET | READ | Get all cards
`card`| POST | CREATE | Create a new card

## Use

There are the docs based in openApi and swagger, where you can test the endpoints

- openAPi: http://127.0.0.1:8000/cards/
- swagger: http://127.0.0.1:8000/docs/

    in swagger you muts pass a dictionary as parameter if want to use the POST endpoints instead
    example:

        {
        "card_num": "6799990100000000019",
        }

Also. We can test the API using [curl](https://curl.haxx.se/) 

    $ curl -X 'GET' \
    'http://127.0.0.1:8000/cards/' \
    -H 'accept: application/json'

or [httpie](https://github.com/jakubroztocil/httpie#installation)


Httpie is a user-friendly http client  Let's try and install that.

http  http://127.0.0.1:8000/cards/


we get:

    {
        "count": 22,
        "next": "http://127.0.0.1:8000/cards/?limit=10&offset=10",
        "previous": null,
        "results": {
            "id": 22,
            "card_num": "3607 0500 0010 20",
            "supplier": "Dinners club"
            },
            {
            "id": 21,
            "card_num": "5306917016520335",
            "supplier": "Master card"
            }, ...
    }

http POST http://127.0.0.1:8000/cards/ card_num="6243 0300 0000 0001"

we get the card created if was correct

    {
        "card_num": "6243 0300 0000 0001",
        "supplier": "Unionpay"
    }


## Pagination
The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}
```
http http://127.0.0.1:8000/cards/?page=1
http http://127.0.0.1:8000/cards/?page=3
http http://127.0.0.1:8000/cards/?page=3&page_size=15
```

# AUTHOR
* **Evert Escalante** ([@evertcolombia](https://github.com/evertcolombia))

# License
## MIT Free Software, Hell Yeah!