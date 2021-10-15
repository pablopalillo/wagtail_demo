# wagtail_demo
My first Wagtail Demo

## Install Instructions

### Requirements
install requirements with pip

```
pip install -r requirements.txt
```

### Database
This project use postgresql Database.
Configure the database in environment

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "name_database",
        "USER": "user_database",
        "PASSWORD": "password_database",
        "HOST": "localhost",
        "PORT": 5432,
        "CONN_MAX_AGE": 600,
        "DISABLE_SERVER_SIDE_CURSORS": True,
    },
}
```

### Cache performance
For cache site's is used redis cache. Configure the redis server configuration.

```
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://ip:port/db', # server redis server
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'renditions': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://ip:port/db',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}
```

### For dumping Wagtail data

```
python manage.py dumpdata --natural-foreign --natural-primary -o fixtures/mydata.json
```

## Done
Run the local server for test purposes

```
python manage.py runserver
```
