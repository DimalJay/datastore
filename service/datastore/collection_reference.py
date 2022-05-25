from helpers.random_gen import generateRandom
from service.datastore.database_abstract import Database
from service.datastore.document_reference import DocumentReference
from service.datastore.exceptions import CollectionNotFoundError


class CollectionReference(Database):
    def __init__(self, delf , collectionPath) -> None:
        self.collectionPath = collectionPath
        self.dbpath = delf.path
        super().__init__(self.dbpath)
        
    
    def add(self, jsonData):
        data = self.read()
        ID = generateRandom()
        try:
            data[self.collectionPath]
        except:
            data[self.collectionPath] = {}
        data[self.collectionPath][ID] = jsonData
        self.write(data=data)

        print(data)
    
    def delete(self):
        data = self.read()
        list()
        try:
            data.pop(self.collectionPath)
        except KeyError:
            print('Colection Not Found')

        self.write(data=data)

        print(data)

    def doc(self, id):
        return DocumentReference(self, id)
    
    def get(self):
        try:
            data = self.read()
            return [i for i in data[self.collectionPath].keys()]
        except:
            raise CollectionNotFoundError