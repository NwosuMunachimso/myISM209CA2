from main import db

class User(db.Model):
    # notice that our class extends db.Model
    __tablename__ = 'userregister'
    # this is the name we want the table in database to have.
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    surname = db.Column(db.String(20), unique=False, nullable=False)
    dateofbirth = db.Column(db.Integer,unique=False, nullable=False)
    residentialaddress = db.Column(db.String(50), unique=True, nullable=False)
    nationality = db.Column(db.String(20), unique=False, nullable=False)
    nationalidentificationnumber = db.Column(db.Integer, primary_key=True)



# represent the object when it is queried for
    def __repr__(self):
        return '<Register {}>'.format(self.id)

