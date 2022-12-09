from flask import Blueprint, request, make_response, render_template, redirect, jsonify
from uuid import uuid4
from ..db import db, Answer, Question
import json

def create_blueprint() -> Blueprint:
    bp = Blueprint('api', __name__)

    @bp.route('/questions', methods=['POST'])
    def questions():
        try:
            data = json.loads(request.data)

            if 'page' not in data or data['page'] == '':
                return "page is as required field", 400
            if 'order' not in data or data['order'] == '':
                return "order is as required field", 400
            if 'name' not in data or data['name'] == '':
                return "question name is as required field", 400
            if 'field_type' not in data or data['field_type'] == '':
                return "field_type is as required field", 400
            if '; ' in data['field_options']:
                return """
                    please do not leave spaces before or after ';' in field_options, 
                    
                    e.g. 1;2;3 instead of 1; 2; 3

                """, 400

            page = data['page']
            order = data['order']
            name = data['name']
            field_type = data['field_type']

            field_options=None
            if 'field_options' in data:
                field_options = data['field_options']

            question = Question(page=page, order=order, name=name, field_type=field_type, 
                field_options=field_options)

            db.session.add(question)
            db.session.commit()

            return f"Saved successfully with ID: {question.id}", 200

        except Exception as e:

            return f'failed to save question: {e}', 500

    @bp.route('/answers', methods=['POST'])
    def answers():

        try :

            if request.cookies.get('user_token') is not None:
                user_token = request.cookies.get('user_token')
                # this user token gives ownership of the answer allowing for the return to a users answer later in the survey
            else:
                return 'No user token supplied', 400

            data = json.loads(request.data)
            page = data['page']
            answers = data['answers']

            for row in answers:
                question_id = row['question_id']
                
                if 'answer' not in row or row['answer'] == '':
                    return "answers are required for all questions", 400

                name = row['answer']
                
                answer = Answer(question_id=question_id, page=page, name=name, user_token=user_token)
                db.session.add(answer)

            db.session.commit()

            return 'Answers saved successfully!', 201

        except Exception as e:
            return f"Error: {e}", 500

    return bp

blueprint = create_blueprint()
