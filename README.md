# word-counter
This will count the frequency of a word in a website.

### Installation
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### API
POST http://localhost:8000/api/wordcount/

Request:
```
{
    "word": "search",
    "url": "example.com"
}
```

Response:
```
{
    "count": 1
}
```

### Unit Test
```
python manage.py test
```
