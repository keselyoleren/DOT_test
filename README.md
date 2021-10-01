# DOT-test

# struktur folder
```
├── dump.rdb
├── media
├── src
│   ├── app
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── admin.cpython-36.pyc
│   │   │   ├── apps.cpython-36.pyc
│   │   │   ├── models.cpython-36.pyc
│   │   │   ├── router.cpython-36.pyc
│   │   │   └── views.cpython-36.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-36.pyc
│   │   │       └── __init__.cpython-36.pyc
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── serializers
│   │   │   ├── __pycache__
│   │   │   │   ├── comment.cpython-36.pyc
│   │   │   │   ├── replies.cpython-36.pyc
│   │   │   │   └── user.cpython-36.pyc
│   │   │   ├── comment.py
│   │   │   ├── replies.py
│   │   │   └── user.py
│   │   ├── tests.py
│   │   └── views
│   │       ├── __pycache__
│   │       │   ├── comment.cpython-36.pyc
│   │       │   └── replies.cpython-36.pyc
│   │       ├── comment.py
│   │       └── replies.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── settings.cpython-36.pyc
│   │   │   ├── urls.cpython-36.pyc
│   │   │   └── wsgi.cpython-36.pyc
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── helper
│   │   ├── __pycache__
│   │   │   └── pagination.cpython-36.pyc
│   │   └── pagination.py
│   ├── manage.py
│   └── middleware
│       ├── __pycache__
│       │   └── middleware_response.cpython-36.pyc
│       └── middleware_response.py
├── static
└── templates
└── .env

```

## keterangan
### ** ```src``` smua app dimasukkan ke dalam folder ini
### ** ```helper``` berisi smua file pembantu
### ** ```middleware``` berisi file untuk mnyamakan format reponse api
### ** ```.env``` file untuk enviroment agar lebih mudah di gunakan oleh beberapa dev

## format api yang biasa saya gunakan
```

  [1] success 
      {
        "data": {
          "results": [
          ],
          "meta": {
            "current_page": 1,
            "next_page": null,
            "previous_page": null,
            "count": 1
          }
        },
        "message": "Success",
        "status": 200,
        "success": true
      }

  [2] failed
      {
        "data":{
           "status": 400,
           "success": false,
           "message": "The failed message",
           "result": {}
        }        
      }
```


