import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Enum, ForeignKey


db = SQLAlchemy()

class FieldType(enum.Enum):
    single_choice = 'single_choice'
    multi_choice = 'multi_choice'
    free_text = 'free_text'
    address = 'address'

class Question(db.Model):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    page = Column(Integer)
    order = Column(Integer)
    field_type = Column(Enum(FieldType))
    field_options = Column(String, nullable=True)

    def option_array(self):
        return self.field_options.split(';')

    def __repr__(self):
            return f'<Question {self.name}>'

class Answer(db.Model):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey(Question.id))
    page = Column(Integer)
    name = Column(String)
    user_token = Column(String)

    def __repr__(self):
            return f'<Answer {self.answer}>'

# This does not cover returning to a previous question but this came down to time constraints. This is something 
# The user_token would however allow this data to be fetched with the correct extra functionality added