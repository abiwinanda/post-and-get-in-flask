# POST and GET Request in Flask

In this example, you'll see how to use Flask to build simple real life API. This API will implement two main request, POST and GET requests.

From a server perspective (who host your api):
- POST - used to received data
- GET - used to send data back only

### Setup

Before you could run the api on your local computer, install the flask on your computer with the following command
```
pip install Flask
```
or you could use the provided env in the repo
```
source venv/bin/activate
```

### API's Resource

To keep the API simple, the app use in memory database therefore every data you add to the API's resource will be gone once you reset the app or web server. Below is the created resource
```python
students = [
    {
        'name': 'Abi',
        'region': 'Bali',
        'subjects': [
            'SKD',
            'PCD',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Tafwida',
        'region': 'Bandung',
        'subjects': [
            'VLSI',
            'DSKC',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Hanif',
        'region': 'Bogor',
        'subjects': [
            'Robotik',
            'PCD',
            'DSKC'
        ]
    }
]
```

### API's End Points

Return all students (GET):
```
/students
```
Example response:
```
[
    {
        'name': 'Abi',
        'region': 'Bali',
        'subjects': [
            'SKD',
            'PCD',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Tafwida',
        'region': 'Bandung',
        'subjects': [
            'VLSI',
            'DSKC',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Hanif',
        'region': 'Bogor',
        'subjects': [
            'Robotik',
            'PCD',
            'DSKC'
        ]
    }
]
```


Return a student with specified name (GET):
```
/students/<string:name>
```
Example response:
```
{
    'name': 'Abi',
    'region': 'Bali',
    'subjects': [
        'SKD',
        'PCD',
        'ARSIKOMPAR'
    ]
}
```


Return all subjects from specified a student (GET):
```
/students/<string:name>/subjects
```
Example response:
```
[
    'SKD',
    'PCD',
    'ARSIKOMPAR'
]
```


Create a new student (POST):
```
/students/create
```


Add subjects to a student (POST):
```
/students/<string:name>/subjects
```
