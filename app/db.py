from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models.base import Base
from flask_migrate import Migrate

db = SQLAlchemy(model_class=Base)
migrate = Migrate()