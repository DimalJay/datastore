from helpers.random_gen import generateRandom
from service.datastore.database_abstract import Database
from service.datastore.exceptions import *


class DocumentReference(Database):
    def __init__(self, collectionref, id=generateRandom()) -> None:
        self.collectionRef = collectionref
        self.id = id
        super().__init__(self.collectionRef.dbpath)
    
    def add(self, jsonData):
        data = self.read()
        try:
            collection = data[self.collectionRef.collectionPath]
        except KeyError:
            data[self.collectionRef.collectionPath] = {}

        try:
            collection = data[self.collectionRef.collectionPath]
            collection[self.id] = jsonData
            data[self.collectionRef.collectionPath] = collection
            self.write(data)
        except KeyError:
            raise DocumentWritingError

    def update(self, jsonData):
        data = self.read()
        try:
            collection = data[self.collectionRef.collectionPath]
            try:
                doc = collection[self.id]
                for feild,value in jsonData.items():
                    doc[feild]=value
                collection[self.id] = doc
                data[self.collectionRef.collectionPath] = collection
                self.write(data) 
            except KeyError:
                raise DocumentNotFoundError
        except KeyError:
            raise CollectionNotFoundError

    def get(self):
        data = self.read()
        try:
            return data[self.collectionRef.collectionPath][self.id]
        except:
            raise DocumentNotFoundError
    
    def delete(self):
        data = self.read()
        try:
            collection = data[self.collectionRef.collectionPath]
            collection.pop(self.id)
            data[self.collectionRef.collectionPath] = collection
            self.write(data)
        except:
            raise DocumentNotFoundError
