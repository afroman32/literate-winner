from flask import Flask, Blueprint, jsonify, render_template, request
from web_app.models.nlp_model import Predictor
from web_app.model import parse_records, db
from web_app.add import db_to_leafly, get_recommendations


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

@insert_routes.route("/print_data", methods=["POST"])
def display_data():
    # Select data from dictionary
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
    # breakpoint()
    # breakpoint()
    # return jsonify(parser(query_result))
    return jsonify(recommend)
