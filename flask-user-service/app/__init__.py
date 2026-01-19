from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.users import users_bp
    from app.errors.handlers import register_error_handlers

    app.register_blueprint(users_bp)
    register_error_handlers(app)

    return app