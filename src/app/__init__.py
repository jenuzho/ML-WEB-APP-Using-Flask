from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar el Blueprint desde routes.py
    from .routes import main
    app.register_blueprint(main)

    return app
