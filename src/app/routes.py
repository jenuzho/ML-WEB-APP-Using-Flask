from flask import Blueprint

# Crear un Blueprint para las rutas
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Actor Relevance Prediction App ^_^!"
