from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from redis import Redis
from .cache import redis_client
from .errors import register_error_handlers

db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    from . import models 

    migrate.init_app(app, db)
    swagger.init_app(app)

    redis_client.init_app(app)  
    register_error_handlers(app)

    from .routes.books import books_bp
    from .routes.reviews import reviews_bp
    app.register_blueprint(books_bp, url_prefix="/books")
    app.register_blueprint(reviews_bp, url_prefix="/books")

    return app
