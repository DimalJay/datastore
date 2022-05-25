import json
import os
from service.cryptograpgy import CRPGService64

class Database:
    def __init__(self, path) -> None:
        self.path = path
        self._initialize()

    def _initialize(self):
        if(not os.path.exists(self.path)):
            self.write({})

    def read(self):
        with open(self.path, mode='rb') as f:
            return json.loads(CRPGService64.decode(f.read()))
        
    
    def write(self, data):
        with open(self.path, 'wb') as f:
            f.write(CRPGService64.encode(json.dumps(data)))

    def delete(self):
        os.remove(self.path)



            