from flask import Blueprint, request, make_response, render_template, redirect, jsonify
from uuid import uuid4
from ..db import db, Answer, Question
import json

# I added this file to better categorise the routes

def create_blueprint() -> Blueprint:
    bp = Blueprint('general', __name__)

    @bp.route('/')
    def home():

        resp = make_response(render_template('home.html'))

        # user_token added so user can be identified if question relates to earlier question
        if request.cookies.get('user_token') is None:
            resp.set_cookie('user_token', str(uuid4()))

        return resp

    @bp.route('/survey', methods=['GET'])
    def survey():

        page = request.args.get('page')
        questions = Question.query.filter_by(page=page).order_by('order')

        if questions.count() == 0:
            return render_template('survey_complete.html')

        return render_template('survey.html', questions=questions)

    @bp.route('/create-question', methods=['GET'])
    def create_question():

        return render_template('admin/create_question.html')

    return bp

blueprint = create_blueprint()
