from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'Elderly Monitoring',
        View('Home', 'index'),
        View('Camera', 'camera'),
        View('Basisunit', 'rpi'),
        View('C4YLO', 'c4ylo'),
        View('Smartphone', 'smartphone'),
        View('Kids', 'kids'),
        View('Prijzen', 'prices'),
        View('Contact', 'contact'),
    )

from app import routes

nav.init_app(app)

