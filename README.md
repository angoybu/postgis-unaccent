## Django Postgis Unaccent

In your settings file change the database engine to `postgis_unaccent`.

```
DATABASES = {
    "default": {
        "ENGINE": "postgis_unaccent",
        ...
    }
}
```
