# module----------------------------------------------------------------
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#DB instance------------------------------------------------------------
db = SQLAlchemy()
migrate = Migrate()

#Application Factory ---------------------------------------------------
def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('config.py')

    #ORM (DB 초기화)
    db.init_app(app)
    migrate.init_app(app, db)

    #table class
    from . import models


    #blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    #flask server instance return
    return app
#----------------------------------------------------------------------