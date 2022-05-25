# Python Database Service - DataStore v1.0
Python Database Service

### Usage
```python
from service.datastore import DataStore
database = DataStore(path='database.db.enc64')
```

### Add New Document
```python
user = {
  'name':'Jone',
  'age':16,
}

database.collection('users').add(user)
```

### Get Collection
```python
users = database.collection('users').get()
print(users)
```

### Update Document
```python
nUser = {
  'address':'Sri Lanka',
  'age': 20,
}
database.collection('users').doc('DOCUMENT_ID').update(nUser)
```

### Delete Document
```python
database.collection('users').doc('DOCUMENT_ID').delete()
```

### Delete Collection
```python
database.collection('users').delete()
```

### Delete Database
```python
database.delete()
```
