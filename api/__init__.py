from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .utilities import db
from .models.orders import Order
from .models.users import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


def create_app(config = config_dict['dev']):
    app = Flask(__name__)
    
    app.config.from_object(config)

    api = Api(app)
    
    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(order_namespace, path ='/orders')
    
    db.init_app(app)
    
    jwt = JWTManager(app)
    
    
    @app.shell_context_processor
    def make_shell_context():
        return{
            'db': db,
            'User': User,
            'Order': Order
        }
    
    return app