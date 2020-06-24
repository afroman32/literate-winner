from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.insert_routes import insert_routes
from web_app.model import db, migrate
import os
from dotenv import load_dotenv
load_dotenv()
# from web_app.routes.json_routes import json_routes\

DATABASE_URL = os.getenv("DB_URL")

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "temporary secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(insert_routes)


    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)