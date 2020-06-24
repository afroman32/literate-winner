from flask import Flask, Blueprint, jsonify, render_template, request
from web_app.models.nlp_model import Predictor
from web_app.model import parse_records, db, db_to_leafly, get_recommendations, UserData


insert_routes = Blueprint("insert_routes", __name__)

@insert_routes.route("/insert_leafly")
def insert_leafly():
    strain = dict(db_to_leafly())
    
    return jsonify(strain)

@insert_routes.route("/get_leafly")
def get_leafly():

    return jsonify(parser(query_result))

@insert_routes.route("/user_data")
def get_data():
    return render_template('effects_flavors.html')

@insert_routes.route("/recommend", methods=["POST"])
def display_data():
    # Select data from dictionary

    # data = request.get_json()
    # user_data = request_json.get('Flavors/Effects')
    # value2           = request_json.get('Last_Name')

    user_data = request.form['Flavors/Effects']
    print("RAW USER DATA TYPE:", type(user_data))
    print("RAW USER DATA:", user_data)

    # Pass user_data into NLP model
    predictor = Predictor()
    results = predictor.predict(user_data, size=5)
    print("NLP RESULTS DATA:", results)
    print("NLP RESULTS DATA TYPE:", type(results))


    recommend = get_recommendations(results)
    print(type(recommend))

    return jsonify(recommend)
