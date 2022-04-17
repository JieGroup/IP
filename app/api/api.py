import sys
import string
import random
import numpy as np

from random import Random
from wtforms import RadioField
from wtforms.validators import InputRequired
from datetime import datetime, timezone

# from app import app
from app.api import api_bp
from app.mongoDB.SurveyAnswerOperator import SurveyAnswer
from app.utils import *
from app.utils import Constant
from app.mongoDB import select_mongoDB_operator
from app.form import FrontForm, DynammicForm, StaticForm

from flask import render_template, flash, redirect, url_for, request, session, make_response


# front page that introduces the survey and record user info
# @api_bp.route('/', methods=['GET', 'POST'])
# @api_bp.route('/front', methods=['GET', 'POST'])
@api_bp.route('/')
def ceshi():
    return 'test successfully'

@api_bp.route('/<string:typ>', methods=['GET', 'POST'])
def front(typ):

    # clean upon entry
    if '_flashes' in session:
            session.pop('_flashes', None)

    form = FrontForm()

    # make sure the voter submits only one time
    if 'submitted' in session:
        pass
        # flash(f"The survey of the link has been completed. Thank you!")
        # return render_template('front2.html', form=form)

    # equiv to check if request.method == 'POST' and if valid_login(request.form)
    if form.validate_on_submit():

        # initialize session once the voter submits basic info and starts survey
        session['start_time'] = datetime.now(timezone.utc)
        session['progress_bar'] = 0
        session['digits'] = obtain_unique_digits()
        session['entered_MTurk'] = False
        
        # generate a randseed specific for this voter
        randseed = int(session['digits']) * Constant.MAXREP

        # settle the type of the survey
        if typ == Constant.RAN:
            # randomly determine which survey way to use
            myRandom = Random(randseed)
            session['survey_way'] = myRandom.sample(Constant.SURVEY_WAY, 1)[0]

        elif typ == Constant.DYN:
            session['survey_way'] = 'dynamic'

        elif typ == Constant.STA:
            session['survey_way'] = 'static'

        else:
            debug('not the right type!')
        # return 'zheli'
        return redirect(url_for('api.question', randseed=randseed))

    # return 'wudi'
    return render_template('front2.html', form=form)


# end page that thanks the survey
@api_bp.route('/end', methods=['GET'])
def end():

    # create a session key-value that has 30min default expiration
    # to ensure the user does not submit immediately again
    session['submitted'] = True

    # create a cookie that lasts 12 hours, to ensure the voter cannot log in after restart browser
    # currently failed to work after restarting browser
    # resp = make_response(render_template('end.html'))
    # resp.set_cookie("voter-submitted", '1', 60*60*12)
    # return resp

    return render_template('end.html', digits=session['digits'])


# question page that asks a dynamically generated list of question
# conditional on the previous answers (by default stored in request)
# previously we used voter_id to query how many rounds the voter has answered a question, now we can use the
# digits (also unique) to identify the round
@api_bp.route('/question/<string:randseed>', methods=['GET', 'POST'])
def question(randseed):

    # debug(f'{voter_id}, {randseed}, {tok}', 'enter question')
    # debug(db.session.query(QandA).order_by(QandA.endtime).first(), 'current db->QandA')

    # fetch the set of feasible questions
    if session['survey_way'] == 'dynamic':
        questions = gen_dynamic_questions(randseed)
        form = DynammicForm(questions)

    elif session['survey_way'] == 'static':
        questions = gen_static_questions(randseed)
        form = StaticForm(questions)

    else:
        debug('Wrong survey_way!')

    # debug(questions.keys(), 'topics')

    if not questions:

        flash(f"Thanks, you have completed the survey!")

        return redirect(url_for('api.end'))

    # equiv to check if request.method == 'POST' and if valid_login(request.form)
    if form.validate_on_submit():
        
        # obtain corresponding mongoDB operator
        mongoDB_operator = select_mongoDB_operator('SurveyAnswer')
        # obtain unique survey_answer_id for each SurveyAnswer document
        survey_answer_id = mongoDB_operator.search_document(digits=session['digits'])['survey_answer_id']
        for topic, (param, sentence, choices) in questions.items():
            if topic == 'MTurk':
                session['entered_MTurk'] = True # one time lock

            answer = str(form.data[topic]) # we required str field in the database
            
            # rounds = db.session.query(QandA).filter_by(voter_id=voter_id, topic=topic).count()
            # rounds = db.session.query(QandA).filter_by(digits=session['digits'], topic=topic).count()

            # # debug(topic, 'topic')

            # # add time stamp
            # qa = QandA(
            #     starttime=session['start_time'],
            #     endtime=datetime.now(timezone.utc),
            #     way=session['survey_way'],
            #     topic=topic,
            #     param=param,
            #     answer=answer,
            #     rounds=rounds+1,
            #     digits=session['digits']
            #     )

            # db.session.add(qa)
            # db.session.commit()
            
            # 注意param
            # Insert new answer for current topic
            mongoDB_operator.update_document(survey_answer_id=survey_answer_id, survey_topic=topic, 
                                             survey_answer=answer, start_time=session['start_time'], 
                                             end_time=datetime.now(timezone.utc), answer_type=param)

        flash(f"Thanks, you have completed {session['progress_bar']}% of the survey!")

        # note that the randseed became string type because of @api_bp.route coercion
        return redirect(url_for('api.question', randseed=int(randseed)+1))

    # else:
    #     print('Jie debug logic', file=sys.stdout)

    return render_template('question.html', form=form)
