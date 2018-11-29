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
