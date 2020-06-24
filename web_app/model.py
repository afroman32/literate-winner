from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Strains(db.Model):
    strain_id = db.Column(db.Integer, primary_key=True)
    strain = db.Column(db.String(128))
    strain_type = db.Column(db.String(128))
    rating = db.Column(db.Integer)
    effects = db.Column(db.String(128))
    flavor = db.Column(db.String(128))
    description = db.Column(db.String(128))

class Recommendations(db.Model):
    Recommendation_id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer)
    strain_id = db.Column(db.Integer)

class UserData(db.Model):
    User_id = db.Column(db.Integer, primary_key=True)
    User = db.Column(db.String(128))
    Desired_Flavor = db.Column(db.String(128))
    Desired_Effect = db.Column(db.String(128))
    
    # def __repr__(self):
        # return jsonify(UserData)

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records