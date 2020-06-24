import pandas
import os

def db_to_leafly():
    DB_FILEPATH = os.path.join(os.path.dirname(__file__), "cannabis.csv")
    df = pandas.read_csv(DB_FILEPATH)
    
    strains = df.iloc[0]
    return strains

def get_recommendations(items):
    DB_FILEPATH = os.path.join(os.path.dirname(__file__), "cannabis.csv")
    df = pandas.read_csv(DB_FILEPATH)

    strains = []
    
    for i in items:
        strains.append(dict(df.iloc[int(i)]))
    return strains