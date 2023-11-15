from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://GUSTAVO\SQLEXPRESS/MY_LIB_FILMES?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
    db.init_app(app)

    #from auth import app
    from .auth import auth
    from .view import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models.users import Users
    
    #with app.app_context():
        #db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app