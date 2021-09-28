from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer


db = SQLAlchemy()


class Survey(db.Model):
    id = Column(Integer, primary_key=True)
