from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


def get_db():
    return db


db = SQLAlchemy(model_class=Base)
