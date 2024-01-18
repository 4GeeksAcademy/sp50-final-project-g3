from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    surname = db.Column(db.Boolean(), unique=False, nullable=False)
    birthday_date = db.Column(db.date(), unique=False, nullable=False)
    creation_date = db.Column(db.date(), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    pictures = db.Column(db.String(100), unique=False, nullable=True)
    preferences = db.Column(db.String(800), unique=False, nullable=False)
    age = db.Column(db.Integer(), unique=False, nullable=False)
    gender = db.Column(db.String(), unique=False, nullable=False)
    interests = db.Column(db.String(500), unique=False, nullable=False)
    smoker = db.Column(db.Boolean(), unique=False, nullable=False)
    social_media = db.Column(db.String(), unique=True, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        # Do not serialize the password, its a security breach
        return {'id': self.id,
                'email': self.email,
                'is_active': self.is_active,
                'surname' : self.surname,
                'birthday_date' : self.birthday_date,
                'creation_date' : self.creation_date,
                'description' : self.description,
                'pictures' : self.pictures,
                'preferences' : self.preferences,
                'age' : self.age,
                'gender' : self.gender,
                'interests' : self.interests,
                'smoker' : self.smoker,
                'social_media' : self.social_media
                }

class Suitors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), unique=True, nullable=False)
    post_id = db.Column(db.Integer(), unique=True, nullable=False)
    suitor_status = db.Column(db.String(15), unique=False, nullable=True)
    leader_status = db.Column(db.String(15), unique=False, nullable=True)
    leader_observations = db.Column(db.String(500), unique=True, nullable=True)

    def serialize(self):
        return {'id' : self.id,
                'user_id' : self.user_id,
                'post_id' : self.post_id,
                'suitor_status' : self.suitor_status,
                'leader_status' : self.leader_status,
                'leader_observations' : self.leader_observations
                }




class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True) 
    pisos_id = db.Column(db.Integer(), unique=True, nullable=False)
    price = db.Column(db.Integer(), unique=False, nullable=False)
    description = db.Column(db.String(800), unique=False, nullable=False)
    publication_date = db.Column(db.Date(), unique=False, nullable=False)
    available_spots = db.Column(db.Integer(), unique=False, nullable=False)
    status = db.Column(db.Boolean(),unique=False, nullable=False)

    def serialize(self):
        return {'id' : self.id,
                'pisos_id' : self.pisos_id,
                'price' : self.price,
                'description' : self.description,
                'publication_date' : str(self.publication_date),
                'available_spots' : self.available_spots,
                'status' : bool(self.status)
                }


class Apartments(db.Model):
    id = db.Column(db.Integer(), primary_key=True) 
    address = db.Column(db.String(),unique=True, nullable=False) 
    flat_leader = db.Column(db.String(),unique=True, nullable=True) 
    rooms = db.Column(db.Integer(),unique=False, nullable=False) 
    bathrooms = db.Column(db.Integer(),unique=False, nullable=False) 
    roommates = db.Column(db.Integer(),unique=False, nullable=True) 
    property_type = db.Column(db.String(),unique=False, nullable=False) 
    preferences = db.Column(db.String(),unique=True, nullable=False)

    #  A CONSULTAR: 
    pictures = db.Column(db.String(100),unique=True, nullable=False)
    video = db.Column(db.String(100),unique=True, nullable=False) 


    furniture = db.Column(db.Bool(),unique=False, nullable=False) 
    deposit = db.Column(db.Integer(),unique=False ,nullable=True) 
    availability = db.Column(db.Integer(),unique=False, nullable=False) 
    accessibility = db.Column(db.String(),unique=False, nullable=True)


    def serialize(self):
        return{'id' : self.id,
                'address' : self.address,
                'flat_leader' : self.flat_leader,
                'rooms' : self.rooms,
                'bathrooms' : self.bathrooms,
                'roommates' : self.roommates,
                'property_type' : self.property_type,
                'preferences' : self.preferences,
                'pictures' : self.pictures,
                'video' : self.video,
                'furniture' : bool(self.furniture),
                'deposit' : self.deposit,
                'availability' : self.availability,
                'accessibility' : self.accessibility          
                }



class Questions(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    suitor_id = db.Column(db.Integer(), unique=True, nullable=False)
    question = db.Column(db.String(200), unique=False, nullable=False)
    answer = db.Column(db.String(500), unique=False, nullable=True)


    def serialize(self):
        return{'id': self.id,
                'suitor_id' : self.suitor_id,
                'question' : self.question,
                'answer' : self.answer
                }

class apartment_users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    profile_id = db.Column(db.Integer(), unique=True, nullable=False)
    apartment_id = db.Column(db.Integer(), unique=True, nullable=False)
    review = db.Column(db.String(800), unique=True, nullable=True)
    

    def serialize(self):
        return{'id' : self.id,
                'profile_id' : self.profile_id,
                'apartment_id' : self.apartment_id,
                'review' : self.review
                }

    