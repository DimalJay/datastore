from service.datastore.collection_reference import CollectionReference
from service.datastore.database_abstract import Database


class DataStore(Database):
    def __init__(self,path='db.crpg64' ) -> None:
        self.path =path
        super().__init__(self.path)
    
    def create(self,path): #books/author/address
        address = self._parseAddress(path)      
        data = self.read()
        seek = data
        for doc in address:
            seek = data[doc]
            print(seek)

    def collection(self, collectionPath):
        return CollectionReference(self, collectionPath)

    def _parseAddress(self, path, sep="/"):
        return path.split(sep)
    

