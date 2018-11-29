from app import db

class UserModel(db.Model):
    """
    User Model
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    
    #class constructor

    def __init__(self, data):
        """
        Class Constructor
        """
        self.name = data.get('name')
        self.surname = data.get('surname')
        
    def __repr__(self):
        return "<User {} {}>".format(self.name, self.surname)

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id': self.id,
           'name': self.name,
           'surname'  : self.surname
       }


class AssetModel(db.Model):
    """
    Asset Model
    """

    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    details = db.Column(db.String(2048), nullable=False)
    owner = db.Column(db.String(128), nullable=False)
    
    def __init__(self, data):
        """
        Class Constructor
        """
        self.name = data.get('name')
        self.type = data.get('type')
        self.city = data.get('city')
        self.rooms = data.get('rooms')
        self.details = data.get('details')
        self.owner = data.get('owner')

    def __repr__(self):
        return "<Asset {} : {}. Owner : {}>".format(self.name, self.type, self.owner)

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_assets():
        return AssetModel.query.all()

    @staticmethod
    def get_one_asset(id):
        return AssetModel.query.get(id)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'id': self.id,
            'name': self.name,
            'type' : self.type,
            'city' : self.city,
            'rooms' : self.rooms,
            'details' : self.details,
            'owner' : self.owner
       }