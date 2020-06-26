from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas
import os

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


class UserData(db.Model):
    User_id = db.Column(db.Integer, primary_key=True)
    User = db.Column(db.String(128))
    strain_id = db.Column(db.Integer)

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "cannabis.csv")
df = pandas.read_csv(DB_FILEPATH)
df['Description'] = df['Description'].fillna('Desciption Unavailable')
df['Flavor'] = df['Flavor'].fillna('Flavor Unavailable')

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

def db_to_leafly():
    # DB_FILEPATH = os.path.join(os.path.dirname(__file__), "cannabis.csv")
    # df = pandas.read_csv(DB_FILEPATH)
    strains = df.iloc[0]
    return strains

def get_recommendations(items):
    # DB_FILEPATH = os.path.join(os.path.dirname(__file__), "cannabis.csv")
    # df = pandas.read_csv(DB_FILEPATH)

    strains = []
    
    for i in items:
        strains.append(dict(df.iloc[int(i)]))
    return strains

def parser(list_of_db_records):
    # list_of_db_records is a list of lists

    parsed_records = []
    for record in list_of_db_records:
        new_record = {}
        new_record['id'] = record[0]
        new_record['Strain'] = record[1]
        new_record['Type'] = record[2]
        new_record['Rating'] = record[3]
        new_record['Effects'] = record[4]
        new_record['Flavor'] = record[5]
        new_record['Description'] = record[6]

        parsed_records.append(new_record)

    pprint.pprint(parsed_records)

    return parsed_records
