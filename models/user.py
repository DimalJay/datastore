class User:
    ID = 'id'
    FULLNAME = 'fullname'
    NIC = 'nic'
    TELEPHONE = 'tele'
    ADDRESS = 'address'
    BIRTHDAY = 'birthday'

    def __init__(
        self, 
        id,
        fullname,
        nic,
        telephone=None,
        address=None,
        birthday=None
        ) -> None:

        self.id = id
        self.fullname = fullname
        self.nic = nic
        self.telephone = telephone
        self.address = address
        self.birthday = birthday

    def toJson(self):
        return {
            User.ID : self.id,
            User.FULLNAME : self.fullname,
            User.NIC : self.NIC,
            User.TELEPHONE : self.telephone,
            User.ADDRESS : self.address,
            User.BIRTHDAY : self.birthday
        }
    
    def fromJson(data):
        return User(
            id=data[User.ID],
            fullname=data[User.FULLNAME],
            nic=data[User.NIC],
            telephone=data[User.TELEPHONE],
            address=data[User.ADDRESS],
            birthday=data[User.BIRTHDAY],
            )

    def setTelephone(self, value):
        self.telephone = value
    
    def setAddress(self, value):
        self.address = value
    
    def setBirthDay(self, value):
        self.birthday = value
    
    
    
