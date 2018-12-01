from app import db
from sqlalchemy import func
from passlib.hash import sha256_crypt

class UserModel(db.Model):
    """
    User Model
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    
    #class constructor

    def __init__(self, data):
        """
        Class Constructor
        """
        self.name = data.get('name')
        self.surname = data.get('surname')
        self.birthdate = data.get('birthdate',None)
        self.password = self.generate_hash(data.get('password'))
        
    def __repr__(self):
        return "<User {} {}>".format(self.name, self.surname)

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.generate_hash(item)
            setattr(self, key, item)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def generate_hash(self, password):
        return sha256_crypt.hash(password)

    def check_hash(self, password):
        return sha256_crypt.verify(self.password, password)
    
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
           'surname'  : self.surname,
           'birthdate' : self.birthdate,
           'password_hash': self.password
       }


class AssetModel(db.Model):
    """
    Asset Model
    """

    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    rooms = db.relationship('RoomModel',backref='assets', lazy=True)
    owner = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.String(128), nullable=False)
    
    def __init__(self, data, user_id):
        """
        Class Constructor
        """
        self.name = data.get('name')
        self.description = data.get('description')
        self.type = data.get('type')
        self.city = data.get('city')
        self.owner = data.get('owner')
        self.user_id = user_id

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

    @staticmethod
    def get_by_city(city):
        """
        Case-insensitive search by city
        """
        return AssetModel.query.filter(AssetModel.city.ilike('%{}%'.format(city))).all()

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type' : self.type,
            'city' : self.city,
            'owner' : self.owner,
            'user_id': self.user_id,
            'rooms': [room.serialize for room in self.rooms]
       }

class RoomModel(db.Model):
    """
    Room Model
    """

    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'), nullable = False)
    name = db.Column(db.String(128), nullable = False)
    details = db.Column(db.String(1024), nullable =False)
    
    def __init__(self, asset_id, name, details):
        """
        Class Constructor
        """
        self.asset_id = asset_id
        self.name = name
        self.details = details


    def __repr__(self):
        return "<Room {} : {}. Asset_id : {}>".format(self.name, self.details, self.asset_id)

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
    def get_all_rooms():
        return RoomModel.query.all()

    @staticmethod
    def get_one_room(id):
        return RoomModel.query.get(id)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'id': self.id,
            'name': self.name,
            'details': self.details
       }