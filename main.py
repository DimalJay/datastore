import json
from models.user import User
from service.datastore import DataStore

user = User(id=None, fullname="Dimal jay", nic="123456789", telephone="123456789")

database = DataStore(path='database.db.enc64')

database.collection('users').add(user.toJson())
with open('database.json','w') as f:
    json.dump(database.read(),f)
