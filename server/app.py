from flask import Flask
from flask_cors import CORS
from server.config import db, migrate, jwt, Config
from dotenv import load_dotenv
load_dotenv()

from server.models import *  # make sure models are imported

# Import blueprints
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp
from server.controllers.auth_controller import auth_bp
from flask_migrate import Migrate, upgrade
from flask.cli import with_appcontext
import click

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)
    app.register_blueprint(auth_bp)

    # Add this route here
    @app.route("/")
    def index():
        return "Late Show API is running!"

    @app.cli.command("db-upgrade")
    @with_appcontext
    def db_upgrade():
        """Run database migrations."""
        upgrade()

    return app

app = create_app()
