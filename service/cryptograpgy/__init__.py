import base64

class CRPGService64:
    def encode( data):
        return base64.encodebytes(data.encode('UTF-8'))

    def decode( data):
        return base64.decodebytes(data).decode()

