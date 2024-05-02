# module
from flask import Flask, render_template, Blueprint

# application factory function
def create_app():
    myapp = Flask(__name__)

    #bp
    from .views import jellyfish
    myapp.register_blueprint(jellyfish.bp)

    return myapp